import os
from distutils.core import setup

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name='easydict',
    version='1.4',
    author='Mathieu Leplatre',
    author_email='mathieu.leplatre@makina-corpus.com',
    packages=['easydict'],
    url='https://github.com/makinacorpus/easydict',
    classifiers  = ['Topic :: Utilities', 
                    'Natural Language :: English',
                    'Operating System :: OS Independent',
                    'Intended Audience :: Developers',
                    'Development Status :: 5 - Production/Stable',
                    'Programming Language :: Python :: 2.5'],
    description="Access dict values as attributes (works recursively)",
    long_description=open(os.path.join(here, 'README.rst')).read(),
)
