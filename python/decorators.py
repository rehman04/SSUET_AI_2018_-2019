'''def hello(name= 'jamali'):
    return 'hello '+name
print(hello())
greet=hello
print(greet())
del hello
print(greet())
print(hello())'''
'''def hello(name='jamali'):
    print('we are in hello func')
    def greet():
        return '\t we r in greet'
    def did():
        return '\t we are in did func'
    print(greet(),' ',did())
    print('we are back in hello')
    print(name)
    if name=='jamali':
        return greet
    else:
        return did
x=hello('nasir')
print(x())'''
'''def hello():
    return 'hi jamali'
def other(func):
    print('this is how it works')
    return func()
print(other(hello))'''
'''def decorator_new(func):
    print('we r in dec_new')
    def wrap_func():
        print('code will be bfore func')
        func()
        print('code after func')
    return wrap_func()
def dec_neweee():
    print('we r in de_newee')
dec_neweee= decorator_new(dec_neweee)
print(dec_neweee)

@decorator_new
def dec_neweee():
    print('we r in de_newee')'''
#we use these concepts while using web frameworks django and flask etc
'''a=['hail','swiming','do']
for l in a:
    if len(l)>2:
        if l[-3:]=='ing':
            l=l+'ly'
            print(l)
        else:
            l=l+'ing'
            print(l)
    else:
        print(l)'''


def deco_fun(sa_hel_fun):
    def wrap_fun(hel_var,wor_var):
        hel='hello'
        wor='world'
        if not hel_var:
            hel_var=hel
        if not wor_var:
            wor_var=wor
        return sa_hel_fun(hel_var,wor_var)
    return wrap_fun

@deco_fun
def say_hel(hel_var,wor_var):
    print(hel_var+" "+wor_var)

say_hel('','')