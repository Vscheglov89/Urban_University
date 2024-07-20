# 1
my_dict = {'Galina': 1986, 'Vasilii': 1989, 'Lidia': 1999}
print(my_dict)
print(my_dict.get('Galina'))
print(my_dict.get('Kirill'))
my_dict.update({'Kirill': 1999, 'Nikita': 1997})
print(my_dict)
a= my_dict.pop('Kirill')
print(a)
print(my_dict)
# 2
my_set = {1, 2, 1, 2, 3, 3, 4, 'Aple', True, (7, 8)}
print(my_set)
my_set.add('trash')
my_set.discard(1)
print(my_set)