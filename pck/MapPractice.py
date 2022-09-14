person = {
        'first_name': 'John',
        'last_name': 'Doe',
        'age': 25,
        'favorite_colors': ['blue', 'green'],
        'active': True
    }

# var = person.get('var')
# print(var)
person['age'] = '1'    # For adding data in pair formate
# del person['active']           # To delete data
# print(person['first_name'])
# print(person['age'])
print(person.items())
print(person.get(3))
# # There is key and value name method need to utilize it
# for value in person.values():  ## same for key
#     print(value)

