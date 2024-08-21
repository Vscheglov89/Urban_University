def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
    print()
print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = ['Vasilii', 35, False]
list_ = ['string', 22]
values_dict = {'c':11}
print_params(*values_list)
print_params(*list_, 99)
print_params(*list_,**values_dict)
values_list_2 = [3/15, 'Строка']
print_params(*values_list_2, 35)

