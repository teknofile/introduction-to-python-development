# https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

# Dictionaries
# Associated or hashes from other langs
# Dicts are indexed by names

ages = { 'foo': 29, 'bar': 30, 'tkf': 42 }
ages['foo'] # = 29

# Keys are immutable types


ages['lsadfj'] # = KeyError

ages['lsadf'] = 4208 # now it's appended (as of python 3.6)
ages['lsadf'] = 4 # updated value to 4

del ages['lsadf'] # deletes key
del ages # deletes the variable

# Del works on a lot more than just dicts

ages = { 'kevin': 59, 'alex': 29, 'bob': 40 }
ages.pop('alex') # retuns 59
ages # no longer has alex

ages.get('kevin') # returns 59
ages.get('alex') # reutns None, 

ages.keys() # returns dict_keys as keys can be cast to a list
ages.values() # returns dict_values object can be cast to a list

weights = dict(kevin=160, bob=240) # returns a dict

colors = dict([('kevin', 'blue'), ('bob', 'green')]) # can use tuples too