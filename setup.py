import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name = "easydict",
    version = "1.0",
    description="Access dict values as attributes (works recursively)",
    long_description=open(os.path.join(here, 'README.rst')).read(),
    packages = find_packages(),
    classifiers  = ['Topic :: Utilities', 
                    'Natural Language :: English',
                    'Operating System :: OS Independent',
                    'Intended Audience :: Developers',
                    'Development Status :: 5 - Production/Stable',
                    'Programming Language :: Python :: 2.5'],
    author = 'Mathieu Leplatre',
    author_email = 'mathieu.leplatre@makina-corpus.com',
)
