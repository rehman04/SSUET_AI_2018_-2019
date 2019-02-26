'''clcty=['karachi','lahore','hyderabad']
usin=''
while True:
    usin=input('eneter city ')
    if usin !='q':
        for l in clcty:
            if usin==l:
                print(l+ " this is the cleanest")
                break
    else:
        print('u didnt choose a city')
        break'''
'''def a(*toppings):
    for t in toppings:
        print('u have entered this topping '+ t)
while True:
    user=input('enter toppings to add')
    if not user:
        print('\nu havent choose more toppings thank u')
        break
    else:
        a(user)'''
'''while True:
    age=int(input("What is your age? "))
    if not age:
        break
    else:
        if age <3:
            print('ur ticket is free')
        elif age >= 3 and age <=12:
            print('ur ticket price is $10')
        elif age >12:
            print('ur ticket price is $13')'''
'''y=[]
while True:
  size=input('please enter ur pizza size or q to cut').upper()
  if size=='q':
    break
  else:
    print('ur pizza size ',size)
  flavour=input('enter ur pizza flavour or press q to cut ').upper()
  if flavour=='q':
    break
  else:
    print('ur pizza flavour ',flavour)
  toppings=''
  while toppings!='q':
    toppings=input('enter ur topping ')
    if toppings=='q':
      break
    else:
      y.append(toppings)
  print('ur toppings list',y.upper())
  order=input('would u like to order more pizza?')
  if order=='yes':
    continue
  else:
    print('thank u for ur order ')
    break'''

'''print('enter ur schedule today')

print('enter done when done with scheduling')

todo=[]

while True:

  list=inpur('> ')

  todo.append(list)

print('here is ur all day schedule')

for t in todo:
  print(t)
'''

