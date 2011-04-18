EasyDict
########

Access dict values as attributes (works recursively)

<https://github.com/leplatrem/easydict>

=====
USAGE
=====

::

    >>> from easydict import EasyDict
    >>> d = EasyDict({'foo':3, 'bar':{'x':1, 'y':2}})
    >>> d.foo
    3
    >>> d.bar.x
    1

Very useful when exploiting parsed JSON content ! ::

    >>> from easydict import EasyDict
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
    >>> d = EasyDict(loads(j))
    >>> d.Buffer
    12
    >>> d.List1[0].coordinates[1]
    54.9


=======
LICENSE
=======

* Lesser GNU Public License

=========
CHANGELOG
=========

1.0
---
* Initial version. Does what I need.

=======
AUTHORS
=======

* Mathieu Leplatre <mathieu.leplatre@makina-corpus.com>
