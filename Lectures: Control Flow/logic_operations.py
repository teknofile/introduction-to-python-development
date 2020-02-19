# https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not

# x or y
# x and y
# not x

# Not == the inverse operation of a boolean

>>> not 1 > 2
True

>> if not 1 > 2:
    print("no it isn't")

# or if either of things is a "true" then it'll give the first one that is truthy

first = ""
last = "lname"
if first or last:
    print("The user has a part of a name")

# above: frist is rturned as false, but last is returned as "lname" which when passed to if will be evaluated as true


first = "fname"
last = ""

if first and last:
    print("The user has a full name")

# Above: the inverse from or