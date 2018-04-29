class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def __repr__(self):
        return 'Point({}, {})'.format(self.x, self.y)
    def __add__(self, other):
        assert isinstance(other, Point)
        return Point(self.x+other.x, self.y+other.y)
p=Point(1, 2)+Point(3, 4)
print(p)

class MyDict(dict):
    def __getattr__(self, item):
        return self.get(item)
d=MyDict(a='b')
print(d['a'])
print(d.a)

'''
magic method:
__new__, __init__  --->   construct and initialize instance
__getattr__, setattr__   --->   attribute visit control
__get__, __set__   --->   attribute related
__getitem__, __setitem__   --->   manipulate container
__enter__, __exit__   --->   context manage
__cmp__, __eq__, __It__, __gt__   --->   comparison operators
__add__, __sub__, __mul__, __div__   --->   arithmatic operators
'''