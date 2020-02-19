# https://docs.python.org/3/tutorial/controlflow.html#for-statements

for TEMPT_VAR in SEQUENCE:
    pass

colors = [ 'blue', 'green', 'red', 'purple' ]
for colors in colors:
    print(color)

colors = ['blue', 'green', 'red', 'purple']
for color in colors:
    if color == 'blue':
        continue
    if color == 'red':
        break
    print(color)


point = (2.1, 3.2, 7.6)
for value in point:
    print(value)


ages = { 'kevin': 59, 'bob': 40, 'kayla': 21 }
for key in ages:
    print(key)

for letter in "my_string":
    print(letter)

list_of_points = [ (1,2), (2,3), (3,4) ]
for x, y in list_of_points:
    print(f"x: {x}, y: {y}")


for name, age in ages.items():
    print(f"Person Named: {name}")
    print(f"Age of: {age}")

