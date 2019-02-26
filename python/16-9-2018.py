class restaurant():
    def __init__(self,restaurant_name,cuisine_type,prices,menu):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.prices = prices
        self.menu = menu

    def describe_retaurant(self):
        print(self.restaurant_name.title()+" restaurant")
        print(self.cuisine_type.title()+" cuisine")
        print(self.prices , " prices")
        print(self.menu.title() + " menu")

    def open_restaurant(self):
        print('restaurant is open')

rest=restaurant('nawab rajput','chinese',42,'ffssadfsd')
rest.open_restaurant()
rest.describe_retaurant()