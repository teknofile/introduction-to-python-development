# https://docs.python.org/3/library/stdtypes.html#comparisons
# https://docs.python.org/3/tutorial/controlflow.html#if-statements

>>> 1 < 2
True
>>> 0 > 2
False
>>> 2 == 1
False
>>> 2 != 1
True
>>> 3.0 >= 3.0
True
>>> 3.1 <= 3.0
False


>>> 2 in [1, 2, 3] # The value of 2 is in the list
True

>>> 4 in [1, 2, 3] 
False

2 not in [1, 2, 3]
False

if True:
    print("was true")

if 1> 2:
    print("was true")
else:
    print('was false')

name = 'tkf'
if len(name) >= 4:
    print("name is long")
elif len(name) == 3:
    print("name is 3 chars")
elif len(name) >= 2:
    print('name is 2 or more')
else:
    print("name is short")

