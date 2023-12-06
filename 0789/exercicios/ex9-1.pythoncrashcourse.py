from dataclasses import dataclass
print("9.1\n")

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        return print(f"{self.restaurant_name}\t{self.cuisine_type}")

    def open_restaurant(self):
        return print("The restaurant is open")

    def set_number_served(self, n_costumers_served):
        self.number_served = n_costumers_served
        return self.number_served

    def increment_number_served(self, increment):
        self.number_served += increment
        return self.number_served
class User:
    def __init__(self, first_name, last_name, country, hobby):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.hobby = hobby
        self.login_attempts = 0

    def describe_user(self):
        return print(f'{self.first_name} {self.last_name}, from {self.country} loves {self.hobby}')

    def greet_user(self):
        return print(f'Hello, {self.first_name}')

    def increment_login_attempts(self):
        self.login_attempts += 1
        return self.login_attempts

    def reset_login_attempts(self):
        self.login_attempts = 0
        return self.login_attempts



restaurant1 = Restaurant("Joyannes","Mediterrânio")
restaurant2 = Restaurant("HHae","Tibete")
restaurant3 = Restaurant("Imuqqs","Mexico")
print(restaurant1.restaurant_name)
print(restaurant1.cuisine_type)
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
print("-"*200)
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

p1 = User("Joao","Americo","Canada","Hockey")
p2 = User("Fernando","Leao","Mexico","Bullfight")

p1.greet_user()
p1.describe_user()
p2.greet_user()
p2.describe_user()
print("-"*20)
print("ex9.4\n")
restaurant4 = Restaurant("Cache","French")
print(restaurant4.number_served)
restaurant4.number_served = 100
print(restaurant4.number_served)
restaurant4.set_number_served(150)
print(restaurant4.number_served)
restaurant4.increment_number_served(100)
print(restaurant4.number_served)

user10 = User("Raul", "Gomes", "Portugal","Tocar guitarra")

print(user10.login_attempts)
user10.increment_login_attempts()
user10.increment_login_attempts()
user10.increment_login_attempts()
print(user10.login_attempts)
user10.reset_login_attempts()
print(user10.login_attempts)

