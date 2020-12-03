<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/setuppy-generator.svg?maxAge=3600)](https://pypi.org/project/setuppy-generator/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/setuppy-generator.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/setuppy-generator.py/actions)

### Installation
```bash
$ [sudo] pip install setuppy-generator
```

#### Pros
+   `setup.py` generator
+   create multiple setup.py files - dev/prod, github/pypi, etc
+   python classes/cli

#### Features
`key`|file/environment variable
-|-
`name`|current directory basename or `$SETUP_NAME`
`version`|`$SETUP_VERSION`
`url`|`$SETUP_URL`
`classifiers`|`classifiers.txt`, `$SETUP_CLASSIFIERS`
`description`|`$SETUP_DESCRIPTION`
`keywords`|`$SETUP_KEYWORDS`
`long_description`|`README.md`/`README.rst`, `$SETUP_LONG_DESCRIPTION`
`long_description_content_type`|`text/markdown` if `long_description` is `.md` file
`install_requires`|`requirements.txt`, `$SETUP_INSTALL_REQUIRES`
`packages`|`setuptools.find_packages()`, `$SETUP_PACKAGES`
`py_modules`|python files in a current directory, `$SETUP_PY_MODULES`
`scripts`|`scripts/*` files, `$SETUP_SCRIPTS`

#### Examples
```
project-name.py/
├── classifiers.txt
├── module.py
├── package
|   └── __init__.py
├── README.md
├── requirements.txt
└── scripts
    └── script
```

```bash
$ cd path/to/project-name.py
$ export SETUP_VERSION="1.0.0"
$ python -m setuppy_generator > setup.py
```

```python
setup(
    name='project-name',
    version='1.0.0',
    classifiers = [...],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=['req1','req2'],
    packages=['pkgname'],
    py_modules=['module'],
    scripts=['scripts/script']
)
```

example #2 - environment variables
```bash
$ export SETUP_URL="https://github.com/owner/repo"
$ export SETUP_CLASSIFIERS="classifiers.txt"
$ export SETUP_DESCRIPTION="description ..."
$ export SETUP_KEYWORDS="key1 key2"
$ export SETUP_LONG_DESCRIPTION="README.md"
$ export SETUP_INSTALL_REQUIRES="requirements.txt"
$ export SETUP_PACKAGES="package1 package2"
$ export SETUP_PY_MODULES="module1 module2"
$ export SETUP_SCRIPTS="scripts/script1 scripts/script2"
$ python -m setuppy_generator > setup.py
```

```python
setup(
    name='project-name',
    version='1.0.0',
    url='https://github.com/owner/repo',
    classifiers = [...],
    description='description ...',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords='key1 key2',
    install_requires=['req1','req2'],
    packages=['package1','package2'],
    py_modules=['module1','module2'],
    scripts=['scripts/script1','scripts/script2']
)
```

`open(path).read()` function:
```bash
$ export SETUP_VERSION="open('.config/version.txt').read().split()"
$ export SETUP_DESCRIPTION="open('.config/description.txt').read().split()"
$ export SETUP_KEYWORDS="open('.config/keywords.txt').read().split(' ')"
$ python -m setuppy_generator > setup.py
```

```python
setup(
    ...
    version=open('.config/version.txt').read().split(),
    description=open('.config/description.txt').read().split(),
    keywords=open('.config/keywords.txt').read().split(' '),
    ...
)
```

example #3 - minimal `setup.py`
```bash
$ export SETUP_CLASSIFIERS=""
$ export SETUP_DESCRIPTION=""
$ export SETUP_KEYWORDS=""
$ export SETUP_LONG_DESCRIPTION=""
$ export SETUP_URL=""
$ python -m setuppy_generator > setup.py
```

```python
setup(
    name='project-name',
    version='1.0.0',
    install_requires=['req1','req2'],
    packages=['pkgname'],
    py_modules=['module'],
    scripts=['scripts/script']
)
```

#### Related
+   [`setupcfg-generator` - `setup.cfg` generator](https://pypi.org/project/setupcfg-generator/)

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>
