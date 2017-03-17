"""A setuptools based setup module for knowledgeowl"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from distutils.command.install import INSTALL_SCHEMES
# To use a consistent encoding
from codecs import open
from os import path

for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

name = 'knowledgeowl'
version_file = open(path.join(name, 'VERSION'))
version = version_file.read().strip()
setup(
    name=name,
    version=version,
    description='Library for accessing KnowledgeOwl',
    long_description=long_description,
    url='https://github.com/blade2005/knowledgeowl',
    author='Craig Davis',
    license='GPLv3',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GPLv3 License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='knowledgeowl',
    packages=find_packages(),
    install_requires=['hammock'],
    extras_require={},
    package_data={},
    data_files=[],
    entry_points={},
    scripts=[],
)