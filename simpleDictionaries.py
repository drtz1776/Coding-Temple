my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

print(my_dict['name'])
print(my_dict.get('age'))

# Insert new value into dict, define key = value
my_dict['Job'] = 'Sales'
print(my_dict.get('Job'))

# delete values in a dict, define the key
del my_dict['some value']

# remove this value but lets you use it elsewhere in code
removed_value = my_dict.pop('Job')
print(removed_value)

# method to return all keys in a dict, .keys(), .values(), .items()
print(list(my_dict.keys()))

# print all items in a dict
for key, value in my_dict.items():
    print(f"{key}: {value}")