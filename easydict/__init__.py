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
    
    Still like a dict though
    
    >>> o = EasyDict({'clean':True})
    >>> o.items()
    [('clean', True)]
    
    And like a class
    
    >>> class Flower(EasyDict):
    ...     power = 1
    ...
    >>> f = Flower({'height': 12})
    >>> f.height
    12
    >>> f.power
    1
    >>> f['power']
    1
    >>> sorted(f.keys())
    ['height', 'power']
    """
    def __init__(self, d=None, **kwargs):
        if d is None:
            d = {}
        d.update(**kwargs)
        for k, v in d.items():
            setattr(self, k, v)
        # Class attributes
        for k in self.__class__.__dict__.keys():
            if not (k.startswith('__') and k.endswith('__')):
                setattr(self, k, getattr(self, k))

    def __setattr__(self, name, value):
        if isinstance(value, (list, tuple)):
            value = [EasyDict(x) if isinstance(x, dict) else x for x in value]
        else:
            value = EasyDict(value) if isinstance(value, dict) else value
        super(EasyDict, self).__setattr__(name, value)
        self[name] = value


if __name__ == "__main__":
    import doctest
    doctest.testmod()
