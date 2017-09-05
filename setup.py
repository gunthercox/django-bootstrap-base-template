#!/usr/bin/env python
"""
Template module setup file.
"""
from setuptools import setup, find_packages


# Dynamically retrieve the version information from the module
TEMPLATE = __import__('django_bootstrap_base_template')
VERSION = TEMPLATE.__version__
AUTHOR = TEMPLATE.__author__
AUTHOR_EMAIL = TEMPLATE.__email__
URL = TEMPLATE.__url__
DOWNLOAD_URL = TEMPLATE.__download__
DESCRIPTION = TEMPLATE.__doc__
LONG_DESCRIPTION = '''
Template module
===============
'''

with open('requirements.txt') as requirements:
    REQUIREMENTS = requirements.readlines()

setup(
    name='django_bootstrap_base_template',
    version=VERSION,
    url=URL,
    download_url=DOWNLOAD_URL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    packages=find_packages(),
    package_dir={
        'django_bootstrap_base_template': 'django_bootstrap_base_template'
    },
    include_package_data=True,
    install_requires=REQUIREMENTS,
    license='MIT',
    zip_safe=True,
    platforms=['any'],
    keywords=['django', 'bootstrap'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests'
)
