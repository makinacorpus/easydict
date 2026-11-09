#!/usr/bin/python
import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

long_desc = ""
with open(os.path.join(here, 'README.rst')) as f:
    long_desc += f.read() + '\n\n'
with open(os.path.join(here, 'CHANGES')) as f:
    long_desc += f.read()

setup(
    name='easydict',
    version='1.13',
    author='Mathieu Leplatre',
    author_email='mathieu.leplatre@makina-corpus.com',
    url='https://github.com/makinacorpus/easydict',
    download_url="http://pypi.python.org/pypi/easydict/",
    description="Access dict values as attributes (works recursively).",
    long_description=long_desc,
    license='LGPL-3.0',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    keywords=['Tools'],
    classifiers=['Topic :: Utilities',
                 'Natural Language :: English',
                 'Operating System :: OS Independent',
                 'Intended Audience :: Developers',
                 'Development Status :: 5 - Production/Stable',
                 'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
                 'Programming Language :: Python :: 2.5',
                 'Programming Language :: Python :: 3.6'],
)
