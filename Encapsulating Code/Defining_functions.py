# https://docs.python.org/3/tutorial/controlflow.html#defining-functions

def hello_world():
    print("hello, world!")

def print_name(name):
    print(f"Name is {name}")

output = print_name("tkf")

def add_two(num):
    return num + 2

result = add_two(2)

def add(num1, num2):
    return num1 + num2

result = add(1, 5)

def contact_card(name, age, car_model):
    return f"{name} is {age} and drives a {car_model}"

def can_drive(age, driving_age=16):
    return age >= driving_age