try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='setuppy-generator',
    version='2019.10.24',
    install_requires=[
        'click',
        'public',
        'setupcfg',
        'setuptools',
    ],
    packages=[
        'setuppy_generator',
    ],
)
