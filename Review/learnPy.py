#Functions
def foo():
    x = "blah"
    return 1

print foo()
#Returns None if no return statement


#Scope
aString = "Global var"
def foo_scope():
    a = "Local var"
    print locals()
    
foo_scope()
print globals


#variable lifetime
#print x


#variable resolution
def foo_res():
    global aString  #<--assign global variable as global to change
    aString = "Local var"
    print aString
    
def bar():
    print aString
    
foo_res()
bar()


#Functional Arguments
#call with args
def foo_fun(x,y):
    print x + y
    
#call with kwargs
def bar(x = 5, y = 12):
    print x - y
    
#both
def foobar(x, y = 100):
    print x*y
    
foo_fun(5, 12)

bar(9, y = 7)

foobar(10)


#Nesting functions
x = 4
def outer():
    x = 1
    def inner():
        global x 
        x = 2
        print "Inner x=%d" %(x)
    inner()
    return x
    
print "Outer x=%d"%outer()
print "Global x=%d"%(x)        


#Classes
class foo_class():
    def __init__(self, arg1):
        self.arg1 = arg1
    def bar_in_class(self, arg2):
        self.arg2 = arg2
        
FOO = foo_class(7)
FOO.bar_in_class(5)

print FOO.arg2


#overriding class
class foo_override():
    def __init__(self, num):
        self.num = num
    def __call__(self):
        return self.num
        
d = foo_override(2)
d()


#numeric types
class foo_num():
    def __init__(self, num):
        self.num = num
    def __add__(self, new):
        self.num += new
        return self
    def __sub__(self, new):
        self.num -= new
        return self
    def __repr__(self):
        return self.__doc__
    def __getitem__(self, num):
        print "Nothing @ %d"%(num)
        
FOO = foo_num(5)
FOO -= 1 
print FOO.num
FOO[2]


#objects
a = 9
dir(a)

from pdb import set_trace

def add(x,y): return x+y
def sub(x,y): return x-y
def foo_inner(x, y, func=add):
    set_trace()
    return func(x,y)
    
#foo_inner(7, 4, sub)


#lambda
bar = lambda x,y: x**y

print bar(4,2)


#decorators
def outer_dec(func):
    def inner_dec(*args):
        "Inner"
        print "decorating ..."
        ret = func()
        ret += 1
        return ret
    return inner_dec
    
@outer_dec    
def foo_dec():
    "I am foo"
    return 1
    
print foo_dec()

    
        