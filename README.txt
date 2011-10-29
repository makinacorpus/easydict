EasyDict
########

Access dict values as attributes (works recursively). A Javascript-like 
properties dot notation for python dicts.

<https://github.com/makinacorpus/easydict>

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

Very useful when exploiting parsed JSON content ! ::

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

Can set attributes as easily as getting them ::

    >>> d = EasyDict()
    >>> d.foo = 3
    >>> d.foo
    3

=======
LICENSE
=======

* Lesser GNU Public License

=========
CHANGELOG
=========

1.2
---
* Renamed README.rst to README.txt

1.1
---
* Fix #1: README.rst was missing for setup install

1.0
---
* Initial version. Does what I need.

=======
AUTHORS
=======

* Mathieu Leplatre <mathieu.leplatre@makina-corpus.com>
