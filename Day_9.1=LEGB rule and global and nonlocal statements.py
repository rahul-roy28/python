'''
LEGB
Local, Enclosing, Global, Built-in
'''
import builtins
print(dir(builtins))  # shows all the names in the builtins module.
def my_min():
    pass
m=min([5,1,4,2,3])   # Local variable min() is enclosed within this function and takes precedence over the global one.
print(m)
x='global x'

def test(z):
    global x
    y='local y'
    #print(y)  
    #print(x)
    print(z)
test('local z')    
print(x)


#Enclosing variable: a variable that is defined inside a function and used by another function.
x='global x'

def outer():
    x='outer x'
    
    def inner():
        nonlocal x
        x-'inner x'
        print(x)
    inner()
    print(x)
outer()        
print(x)