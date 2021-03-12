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


    Values extraction

    >>> d = EasyDict({'foo':0, 'bar':[{'x':1, 'y':2}, {'x':3, 'y':4}]})
    >>> isinstance(d.bar, list)
    True
    >>> from operator import attrgetter
    >>> map(attrgetter('x'), d.bar)
    [1, 3]
    >>> map(attrgetter('y'), d.bar)
    [2, 4]
    >>> d = EasyDict()
    >>> d.keys()
    []
    >>> d = EasyDict(foo=3, bar=dict(x=1, y=2))
    >>> d.foo
    3
    >>> d.bar.x
    1


    Still acts like a dict type

    >>> o = EasyDict({'clean':True})
    >>> o.items()
    [('clean', True)]


    Simple inheritance with dict attribute

    >>> class SimpleDict(EasyDict):
            def __init__(self):
                self.value = {'one': 'two'}
    ...
    >>> simple_dict = SimpleEasyDict()
    >>> simple_dict['value'].one
    'two'


    Static class attributes

    >>> class Flower(EasyDict):
    ...     power = 1
    ...     children = {'two': 2}
    ...
    >>> f = Flower()
    >>> f.power
    1
    >>> f.children.one
    2
    >>> f = Flower({'height': 12})
    >>> f.height
    12
    >>> f['power']
    1
    >>> sorted(f.keys())
    ['height', 'power']


    Instance class attributes

    >>> class SuperEasyDict(EasyDict):
    ...     __init__(self, value = None):
    ...         self.value = value
    ...
    >>> awesome_dict = SuperEasyDict()
    >>> awesome_dict = SuperEasyDict(1)
    >>> awesome_dict.value
    1
    >>> awesome_dict = SuperEasyDict({'gamma': 'delta', 'alpha': 'beta'})
    >>> awesome_dict['value']
    {'gamma': 'delta', 'alpha': 'beta'}
    >>> sorted(awesome_dict.value.keys())
    ['alpha', 'gamma']
    >>> awesome_dict.value.alpha
    'beta'
    >>> awesome_dict.epsilon = 'zeta'
    >>> awesome_dict['eta'] = 'theta'
    >>> sorted(awesome_dict.keys())
    ['epsilon', 'eta', 'value']


    Update and pop items

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
    """
    def __init__(self, d=None, **kwargs):
        if d is None:
            d = {}
        if kwargs:
            d.update(**kwargs)
        for k, v in d.items():
            setattr(self, k, v)
        # Class attributes
        for k in self.__class__.__dict__.keys():
            if not (k.startswith('__') and k.endswith('__')) and not k in ('update', 'pop'):
                setattr(self, k, getattr(self, k))

    def __setattr__(self, name, value):
        if isinstance(value, (list, tuple)):
            value = [EasyDict(x)
                     if isinstance(x, dict) else x for x in value]
        elif isinstance(value, dict) and not isinstance(value, EasyDict):
            value = EasyDict(value)
        super(EasyDict, self).__setattr__(name, value)
        super(EasyDict, self).__setitem__(name, value)

    __setitem__ = __setattr__

    def update(self, e=None, **f):
        d = e or dict()
        d.update(f)
        for k in d:
            setattr(self, k, d[k])

    def pop(self, k, d=None):
        delattr(self, k)
        return super(EasyDict, self).pop(k, d)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
