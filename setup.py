from setuptools import setup

setup(
    name = 'pymeboot',
    packages = ['pymeboot'],
    version = '0.0.1',
    description = "Maximum entropy bootstrap for time series",
    author = 'Kira Huselius Gylling',
    author_email = 'kira.gylling@gmail.com',
    url = 'https://github.com/kirahg/pymeboot',
    download_url = 'https://github.com/kirahg/pymeboot/tarball/0.0.1',
    install_requires = ['requests>=2.12.4'],
    license = 'MIT',
    keywords = ['data', 'statistics', 'time series', 'bootstrap'],
    classifiers = [],
)
