import setuptools

setuptools.setup(
    name='setuppy-generator',
    version='2020.12.2',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
