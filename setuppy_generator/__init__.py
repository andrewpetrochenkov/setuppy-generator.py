__all__ = ['BaseGenerator', 'Generator']


import ast
import os
import setupcfg
import setuptools


class raw(str):
    pass


class BaseGenerator:
    """abstract generator class"""
    kwargs = None

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def get_keys(self):
        return setupcfg.metadata.KEYS + setupcfg.options.KEYS

    def format_bool(self, value):
        return str(value)

    def format_dict(self, value):
        lines = []
        for k, v in value.items():
            s = str(v) if isinstance(v, list) else "'%s'" % v
            lines.append("'%s': %s" % (k, s))
        return """{
%s
}""" % "\n".join(map(lambda l: "    %s," % l, lines))

    def format_list(self, value):
        return """[
%s
]""" % "\n".join(map(lambda l: "    '%s'," % l, value))

    def format_raw(self, value):
        return str(value)

    def format_str(self, value):
        return "'%s'" % str(value)

    def get_value(self, key):
        if key in self.kwargs:
            value = self.kwargs[key]
        else:
            if not hasattr(self, 'get_%s' % key):
                return
            value = getattr(self, 'get_%s' % key)()
        if not value:
            return
        func_name = 'format_%s' % type(value).__name__
        if hasattr(self, func_name):
            return getattr(self, func_name)(value)
        raise TypeError('unsupported type - %s' % type(value))

    def get_header(self):
        if os.getenv('SETUP_DISTUTILS'):
            return 'from distutils.core import setup'
        if os.getenv('SETUP_SETUPTOOLS') or self.get_value('install_requires'):
            return 'from setuptools import setup'
        return """
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
"""

    def get_bottom(self):
        return ""

    def get_body(self):
        lines = []
        keys = self.get_keys()
        if not keys:
            raise ValueError('unknown keys')
        for key in keys:
            value = self.get_value(key)
            if value not in [None, '', []]:
                out = "%s=%s," % (key, value)
                for l in out.splitlines():
                    lines.append('    %s' % l)
        return """setup(
%s
)
""" % "\n".join(lines)

    def render(self):
        return "\n\n".join(filter(None,
                                  [self.get_header(), self.get_body(),
                                   self.get_bottom()]
                                  )).strip()

    def validate(self):
        ast.parse(self.render())

    def create(self, path=None):
        """create `setup.cfg`"""
        if not path:
            path = "setup.py"
        dirname = os.path.dirname(path)
        if dirname and not os.path.exists(dirname):
            os.makedirs(dirname)
        out = self.render()
        open(path, "w").write(out)

    def __str__(self):
        return self.render()


def getenv(key):
    value = os.environ.get(key)
    return raw(value) if 'open(' in value and '.read()' in value else value


def getenvlist(key):
    value = os.environ.get(key)
    return value.replace(',', ' ').replace('  ', ' ').split(' ') if value else []


class Generator(BaseGenerator):
    """generator class"""

    def get_name(self):
        """return `name` string - working dir name without extension"""
        if 'SETUP_NAME' in os.environ:
            return os.environ.get('SETUP_NAME')
        return os.path.basename(os.getcwd()).split(".")[0].lower()

    def get_version(self):
        if 'SETUP_VERSION' in os.environ:
            return getenv('SETUP_VERSION')

    def get_url(self):
        return os.environ.get('SETUP_URL', None)

    def get_keywords(self):
        """return `name` string - working dir name without extension"""
        if 'SETUP_KEYWORDS' in os.environ:
            return getenv('SETUP_KEYWORDS')

    def get_description(self):
        if 'SETUP_DESCRIPTION' in os.environ:
            return getenv('SETUP_DESCRIPTION')

    def get_license(self):
        if 'SETUP_LICENSE' in os.environ:
            return getenv('SETUP_LICENSE')

    def get_long_description(self):
        if 'SETUP_LONG_DESCRIPTION' in os.environ:
            path = os.environ.get('SETUP_LONG_DESCRIPTION')
            return raw("open('%s').read()" % path) if path else None
        for path in ['README.md', 'README.rst']:
            if os.path.exists(path):
                return raw("open('%s').read()" % path)

    def get_long_description_content_type(self):
        long_description = self.get_long_description()
        if long_description and '.md' in long_description:
            return "text/markdown"

    def get_classifiers(self):
        path = 'classifiers.txt'
        if 'SETUP_CLASSIFIERS' in os.environ:
            path = os.environ.get('SETUP_CLASSIFIERS')
        if os.path.exists(path):
            return open(path).read().splitlines()

    def get_packages(self):
        """return `packages` list - `setuptools.find_packages()`"""
        if 'SETUP_PACKAGES' in os.environ:
            return getenvlist('SETUP_PACKAGES')
        return setuptools.find_packages()

    def get_install_requires(self):
        """return `install_requires` list. content of `requirements.txt`"""

        path = 'requirements.txt'
        if 'SETUP_INSTALL_REQUIRES' in os.environ:
            path = os.environ.get('SETUP_INSTALL_REQUIRES')
        if os.path.exists(path):
            return list(map(
                lambda l: l.split("#")[0].lstrip().rstrip(),
                open(path).read().splitlines()
            ))

    def get_scripts(self):
        """return `scripts` list. `bin/`, `scripts/` files"""
        if 'SETUP_SCRIPTS' in os.environ:
            return getenvlist('SETUP_SCRIPTS')
        result = []
        exclude = ['.DS_Store', 'Icon\r']
        for path in ["scripts"]:
            if os.path.exists(path) and os.path.isdir(path):
                files = list(
                    filter(lambda f: f not in exclude, os.listdir(path)))
                result += list(map(lambda f: os.path.join(path, f), files))
        return result
