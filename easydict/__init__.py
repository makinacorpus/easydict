class EasyDict(dict):
    """
    Get attributes

    >>> d = EasyDict({'foo':3})
    >>> d['foo']
    3
    >>> d.foo
    3
    >>> d.bar
    Traceback (most recent call last):
    ...
    AttributeError: 'EasyDict' object has no attribute 'bar'

    Works recursively

    >>> d = EasyDict({'foo':3, 'bar':{'x':1, 'y':2}})
    >>> isinstance(d.bar, dict)
    True
    >>> d.bar.x
    1

    Bullet-proof

    >>> EasyDict({})
    {}
    >>> EasyDict(d={})
    {}
    >>> EasyDict(None)
    {}
    >>> d = {'a': 1}
    >>> EasyDict(**d)
    {'a': 1}
    >>> EasyDict((('a', 1), ('b', 2)))
    {'a': 1, 'b': 2}
    
    Set attributes

    >>> d = EasyDict()
    >>> d.foo = 3
    >>> d.foo
    3
    >>> d.bar = {'prop': 'value'}
    >>> d.bar.prop
    'value'
    >>> d
    {'foo': 3, 'bar': {'prop': 'value'}}
    >>> d.bar.prop = 'newer'
    >>> d.bar.prop
    'newer'
    >>> d.lst = [1, 2, 3]
    >>> d.lst
    [1, 2, 3]
    >>> d.tpl = (1, 2, 3)
    >>> d.tpl
    (1, 2, 3)
    >>> d.lst = [{'a': 1}, {'b': 2}]
    >>> type(d.lst).__name__, type(d.lst[0]).__name__, d.lst[0].a, d.lst[1].b
    ('list', 'EasyDict', 1, 2)
    >>> d.tpl = ({'a': 1}, {'b': 2})
    >>> type(d.tpl).__name__, type(d.tpl[0]).__name__, d.tpl[0].a, d.tpl[1].b
    ('tuple', 'EasyDict', 1, 2)

    Subclasses of list, tuple and dict are left untouched

    >>> class CustomList(list): pass
    >>> class CustomTuple(tuple): pass
    >>> class CustomDict(dict): pass
    >>> d = EasyDict()
    >>> d.lst = CustomList([{'a': 1}])
    >>> type(d.lst).__name__, type(d.lst[0]).__name__
    ('CustomList', 'dict')
    >>> d.tpl = CustomTuple(({'a': 1},))
    >>> type(d.tpl).__name__, type(d.tpl[0]).__name__
    ('CustomTuple', 'dict')
    >>> d.dct = CustomDict({'key': 'value'})
    >>> type(d.dct).__name__
    'CustomDict'
    >>> d.dct == {'key': 'value'}
    True

    Values extraction

    >>> d = EasyDict({'foo':0, 'bar':[{'x':1, 'y':2}, {'x':3, 'y':4}]})
    >>> isinstance(d.bar, list)
    True
    >>> from operator import attrgetter
    >>> list(map(attrgetter('x'), d.bar))
    [1, 3]
    >>> list(map(attrgetter('y'), d.bar))
    [2, 4]
    >>> d = EasyDict()
    >>> list(d.keys())
    []
    >>> d = EasyDict(foo=3, bar=dict(x=1, y=2))
    >>> d.foo
    3
    >>> d.bar.x
    1

    Still like a dict though

    >>> o = EasyDict({'clean':True})
    >>> list(o.items())
    [('clean', True)]

    And like a class

    >>> class Flower(EasyDict):
    ...     power = 1
    ...     mean = {}
    ...     color = {"r": 100, "g": 0, "b": 0}
    ...
    >>> f = Flower()
    >>> f.power
    1
    >>> f.color.r
    100
    >>> f.mean.x = 10
    >>> f.mean.x
    10
    >>> f = Flower({'height': 12})
    >>> f.height
    12
    >>> f['power']
    1
    >>> sorted(f.keys())
    ['color', 'height', 'mean', 'power']

    update and pop items
    >>> d = EasyDict(a=1, b='2')
    >>> e = EasyDict(c=3.0, a=9.0)
    >>> d.update(e)
    >>> d.c
    3.0
    >>> d['c']
    3.0
    >>> d.get('c')
    3.0
    >>> d.update(a=4, b=4)
    >>> d.b
    4
    >>> d.pop('a')
    4
    >>> d.a
    Traceback (most recent call last):
    ...
    AttributeError: 'EasyDict' object has no attribute 'a'
    >>> d.pop('a', 8)
    8
    >>> d.pop('b', 100)
    4
    >>> d
    {'c': 3.0}

    Set defaults through attributes, including nested mappings

    >>> d = EasyDict()
    >>> d.setdefault('count', 2)
    2
    >>> d.count
    2
    >>> settings = d.setdefault('settings', {'enabled': True})
    >>> settings is d.settings
    True
    >>> settings.enabled
    True
    >>> d.setdefault('count', 9)
    2
    >>> d.count
    2
    >>> d.setdefault('optional') is None
    True
    >>> d.optional is None
    True
    >>> sorted(d)
    ['count', 'optional', 'settings']

    Keys that cannot be ordinary attributes remain dictionary entries

    >>> for key in (1, None, ('item',), '__class__', '__dict__', '__weakref__'):
    ...     d = EasyDict()
    ...     value = {'enabled': True}
    ...     assert d.setdefault(key, value) is value
    ...     assert d[key] is value
    ...     assert d.setdefault(key, 'replacement') is value
    ...     assert type(d) is EasyDict
    ...     assert vars(d) == {}

    update does not mutate its argument

    >>> src = {'a': 1}
    >>> d = EasyDict()
    >>> d.update(src, b=2)
    >>> src == {'a': 1}
    True
    """
    def __init__(self, d=None, **kwargs):
        if d is None:
            d = {}
        else:
            d = dict(d)        
        if kwargs:
            d.update(**kwargs)
        for k, v in d.items():
            setattr(self, k, v)
        # Class attributes
        for k in self.__class__.__dict__:
            if not (k.startswith('__') and k.endswith('__')) and k not in ('update', 'pop', 'setdefault'):
                setattr(self, k, getattr(self, k))

    def __setattr__(self, name, value):
        if type(value) in (list, tuple):
            value = type(value)(self.__class__(x)
                     if isinstance(x, dict) else x for x in value)
        elif type(value) == dict and not isinstance(value, EasyDict):
            value = EasyDict(value)
        super().__setattr__(name, value)
        super().__setitem__(name, value)

    __setitem__ = __setattr__

    def update(self, e=None, **f):
        d = dict(e) if e else {}
        d.update(f)
        for k in d:
            setattr(self, k, d[k])

    def setdefault(self, key, default=None):
        if not isinstance(key, str) or (key.startswith('__') and key.endswith('__')):
            return dict.setdefault(self, key, default)
        if key not in self:
            self[key] = default
        return self[key]

    def pop(self, k, *args):
        if hasattr(self, k):
            delattr(self, k)
        return super().pop(k, *args)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
