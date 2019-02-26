'''def greeting(names):
    for name in names:
        print('hello',name,'!')
usernames=['hannah','danish','sohail']
greeting(usernames)'''

'''def names(first_name,middle_name,last_name):
    print('full name is : '+first_name+' '+middle_name+' '+last_name)
s=input('enter first name ')
t=input('enter middle_name ')
f=input('enter last_name ')
names(s,t,f)'''
'''def make_pizza(*toppings):
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')'''
'''def make_pizza(size,*toppings):
    print(size,toppings[0])
make_pizza('small','pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')'''

'''def make_pizza(size,*toppings,**drinks):
    print(size,toppings[0],drinks)
make_pizza('small','pepperoni',drinks='pepsi')
make_pizza('mushrooms','green peppers','extra cheese')'''

'''def greeet(**name):
    for k,v in name.items():
        print("{0}={1}" .format(k,v))
greeet(name='shifa',name1='jamali')'''
