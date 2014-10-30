dicts = [
    {'name': 'Michelangelo',
     'food': 'PIZZA'},
    {'name': 'Garfield',
     'food': 'lasanga'},
    {'name': 'Walter',
     'food': 'pancakes'},
    {'name': 'Galactus',
     'food': 'worlds'}
]

string = "Hi, I'm {name} and I love to eat {food}!"



def string_factory(dict_factory, string_format):
    # Create our empty list
    return_list = []

    for item in dict_factory:
        # So we can go ahead and append this to our return_list
        return_list.append(string_format.format(**item))

    print (return_list)

# Call the function
string_factory(dicts, string)
