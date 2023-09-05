# NGÔ VIỆT THÀNH-B19DCCN651
#8-1
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def open_restaurant(self):
        print(f"Restaurant {self.restaurant_name} open")
    def description_restaurant(self):
        descri = f"{self.restaurant_name} {self.cuisine_type}"
        return descri
    def served(self):
        print(f"Number served {self.number_served}")
    def set_number_served(self, xyz):
        self.number_served = xyz
    def increment(self, xyz):
        self.number_served += xyz
restaurant = Restaurant('DaSunGod', 'Mon VN')
print(f"Nha hang {restaurant.description_restaurant()}")
restaurant.open_restaurant()
print(f"Nha hang {restaurant.restaurant_name} co mon {restaurant.cuisine_type}")

#8-2
gara_restaurant = Restaurant('Widely,', 'Smart')
print(f"Garage: {gara_restaurant.description_restaurant()}")

menu = Restaurant('Rau muong xao,', 'Thit cho')
print(f"Menu:   {menu.description_restaurant()}")

sevice = Restaurant('Good,', 'Luxury')
print(f"Service:{sevice.description_restaurant()}")

#8-4
#restaurant.number_served = 50
restaurant.served()

restaurant.set_number_served(22)
restaurant.served()

restaurant.increment(150)
restaurant.served()

#8-3

class   Users:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.number_login = 0
    def fullname(self):
        long_name = f"{self.first_name} {self.last_name}"
        return long_name.title()
    def login(self):
        print(f"Number login {self.number_login}")
    def increment(self, abc):
        self.number_login += abc
user = Users('Nguyen' ,'T')
print(user.fullname())

#8-5
user.login()
user.increment(1)
user.login()



#8-8
class Users():
    def __init__(self,first_name,last_name,username,phone_number):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.phone_number = phone_number
        self.login_attempts = 0
    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name}")
        print(self.username)
        print(self.phone_number)
    def greet_user(self):
        print(f"Welcome {self.username} to my world.")
    def increment_login_attempts(self):
        self.login_attempts +=1
    def reset_login_attempts(self):
        self.login_attempts=0
class Admin(Users):
    def __init__(self,first_name,last_name,username,phone_number):
        super().__init__(first_name,last_name,username,phone_number)
        self.privileges = Privileges()
class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges
    def show_privileges(self):
        if self.privileges:
            for privilege in self.privileges:
                print(privilege)
        else:
            print("This user has no privileges.")
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)
XY = Admin('Nguyen','T','DaSunGod','0123456789')
XY.describe_user()
XY.privileges.show_privileges()
XY_privileges = ['can add post','can delete post', 'can ban user']
XY.privileges.privileges = XY_privileges
XY.privileges.show_privileges()

#8-11
class Users():
    def __init__(self,first_name,last_name,username,phone_number):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.phone_number = phone_number
        self.login_attempts = 0
    def describe_user(self):
        print(f"{self.first_name} {self.last_name}")
        print(self.username)
        print(self.phone_number)
    def greet_user(self):
        print(f"Welcome {self.username} to my world.")
    def increment_login_attempts(self):
        self.login_attempts +=1
    def reset_login_attempts(self):
        self.login_attempts=0
class Admin(Users):
    def __init__(self,first_name,last_name,username,phone_number):
        super().__init__(first_name,last_name,username,phone_number)
        self.privileges = Privileges([])
class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)