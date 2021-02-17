# __slots__
# allow incapsulation
# in slots we specify attributes of class what could be used ( in object of this class). 

# jupiter 
# https://jupyter.org/try


class RegularClass:
    pass
obj = RegularClass()
obj.__dict__  #=> # {}
obj.foo = 5
obj.__dict__   #=> # {'foo': 5}


class SlotsClass:
    __slots__ = ('foo', 'bar')
obj = SlotsClass()
obj.foo = 5
obj.__slots__   # => # ('foo', 'bar')
obj.__dict__  # => Traceback (most recent call last):   
    #File "python", line 8, in <module>  AttributeError: 'SlotsClass' object has no attribute '__dict__'


#abstract classes: