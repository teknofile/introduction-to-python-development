# The most common immutable sequence type that we're going to work
# with is going to be tuple. We'll also look at the range type as an alternative
# to a seuential list.

# https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
# https://docs.python.org/3/library/stdtypes.html#tuple
# https://docs.python.org/3/library/stdtypes.html#range

#point = (x, y)
point = (2.0, 3.0)
point[0] # 2.0
point[0] = 1 # TypeError, typle doesn't support assignment

point_3d = point + (4.0,) # need the common to define it as a tuple with one item
point_3d # = (2.0, 3.0, 4.0)

x, y, z = point_3d
# x= 2.0
# y= 3.0
# z= 4.0

print("My name is: %s %s" % ("Foo", "Bar"))

range(10) # range(0, 10)
list(range(10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

range(0, 10000)
range(1, 12, 2) # = [1, 3, 5, 7, 9, 11]

