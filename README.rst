*EasyDict* allows to access dict values as attributes (works recursively). 
A Javascript-like properties dot notation for python dicts.

=====
USAGE
=====

::

    >>> from easydict import EasyDict as edict
    >>> d = edict({'foo':3, 'bar':{'x':1, 'y':2}})
    >>> d.foo
    3
    >>> d.bar.x
    1
    
    >>> d = edict(foo=3)
    >>> d.foo
    3


Very useful when exploiting parsed JSON content ! 

::

    >>> from easydict import EasyDict as edict
    >>> from simplejson import loads
    >>> j = """{
    "Buffer": 12,
    "List1": [
        {"type" : "point", "coordinates" : [100.1,54.9] },
        {"type" : "point", "coordinates" : [109.4,65.1] },
        {"type" : "point", "coordinates" : [115.2,80.2] },
        {"type" : "point", "coordinates" : [150.9,97.8] }
    ]
    }"""
    >>> d = edict(loads(j))
    >>> d.Buffer
    12
    >>> d.List1[0].coordinates[1]
    54.9

Can set attributes as easily as getting them :

::

    >>> d = EasyDict()
    >>> d.foo = 3
    >>> d.foo
    3

It is still a ``dict`` !

::

    >>> d = EasyDict(log=False)
    >>> d.debug = True
    >>> d.items()
    [('debug', True), ('log', False)]

Instance and class attributes are accessed like usual objects...

::

    >>> class Flower(EasyDict):
    ...     power = 1
    ...
    >>> f = Flower({'height': 12})
    >>> f.power
    1
    >>> f['power']
    1

=======
LICENSE
=======

* Lesser GNU Public License

=======
AUTHORS
=======

* Mathieu Leplatre <mathieu.leplatre@makina-corpus.com>

|makinacom|_

.. |makinacom| image:: http://depot.makina-corpus.org/public/logo.gif
.. _makinacom:  http://www.makina-corpus.com

Similar tools
=============

* `TreeDict <http://pypi.python.org/pypi/treedict>`_, a fast and full-featured dict-like tree container.
