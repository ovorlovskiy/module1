my_dict = {'Oleg': 53, 'Rimma': 40, 'Vlada': 16, 'Yaroslav': 12}
print(my_dict)
print(my_dict['Rimma'])
print(my_dict.get('Elen'))
my_dict.update({'Elen': 59,
                'Vladimir': 62})
print(my_dict)
a = my_dict.pop('Vladimir')
print(my_dict)
print(a)
print(my_dict.items())
my_set = {3, 2, 6, 3, 1, 6, 3, 'park', (1, 2, 3, 4.2, 5)}
print(my_set)
list_ = ('cofe', 9.9)
my_set.update(list_)
print(my_set)
my_set.remove('park')
print(my_set)
