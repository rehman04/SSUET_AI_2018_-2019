class car_categories:
    def __init__(self, listt):
        x = {}
        self.listt = listt
        n = []
        for t in listt:
            n.append(listt.index(t))
        zipped = list(zip(listt, n))
        self.x = dict(zipped)

    def removed_carr(self, sad):
        self.listt.remove(sad)

    def returned_car(self, sd):
        for k in self.x.keys():
            if sd is k:
                self.listt.insert(self.x[k], k)

d = ['hatchback', 'sedan', 'suv']
cars = car_categories(d)
e = {'hatchback': ['$', 30], 'sedan': ['$', 50], 'suv': ['$', 100]}
print('here is car list and fares per day')
for k in e.keys():
    print(k+': '+e[k][0]+str(e[k][1]))
while True:
    user1=input('u want to returned or borrow?')
    if not user1:
        break
    if user1=='returned':
        user2 = input('please enter type car u want to returned')
        cars.returned_car(user2)
    else:
        user3 = input('please choose type car u want to borrow?')
        cars.removed_carr(user3)
        user4 = input('for how many days u want to borrow?')
        h = e[user3][1] * int(user4)
        print('ur fare details are\n'+user3+': $'+str(h))

