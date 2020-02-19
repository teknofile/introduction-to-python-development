# https://docs.python.org/3/tutorial/introduction.html#first-steps-towards-programming

while CONDITION:
    pass


count = 1
while count <= 4:
    print("looping")
    count += 1

count = 0
while count < 10:
    if count % 2 == 0:
        count += 1
        continue # if it's even, we don't do anything
    print(f"We're counting odd numbers: {count}")
    count += 1