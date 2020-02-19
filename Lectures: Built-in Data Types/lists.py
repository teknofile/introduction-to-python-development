# https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
# https://docs.python.org/3/library/stdtypes.html#list

# Lists are going to be the most widely used sequence type

# A list is a ordered sequence of items.
list('abc') returns [ 'a', 'b', 'c' ]

my_list = [ 1, 2, 3, 4, 5 ]

my_list[0] # = 1
my_list[3] # = 4


my_list[7] # = error (IndexError)
len(my_list) # = 5
len("string") # = 6

my_list[len(my_list) - 1] # Will alwys give the last item in the list

# slicing

my_list[0:2] # = [ 1, 2 ]    Gives a range

# With a negative step, you can reverse a list, like:
my_list[::-1] # = [5, 4, 3, 2, 1]

my_list[0] = "a" # assigns a to the zero index, [ 'a', 1, 2, 3, 4, 5 ]

my_list[0:2] = 'a' # ['a', 3, 4, 5]

my_list.remove(6) # Error, not in the list

my_list.remove(4) # = [3, 5]

my_list.pop() # returns 5, returns thelast item but takes it off the list
my_list.pop() # returns 3,
my_list.pop() # errors, it's empty

my_list = [1, 2, 3, 4]
my_list.pop(0) # makes a list work like a queue,

my_list.append(5) #adds to the end
my_list.insert(1, 3) # inserts a 3 at position 1