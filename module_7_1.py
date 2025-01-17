class product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)


    def __str__(self):
        str_product = f'{self.name}, {self.weight}, {self.category}'
        return str_product

'''Объекты класса Shop будут создаваться следующим образом - Shop() и обладать следующими свойствами:
Инкапсулированный атрибут __file_name = 'products.txt'.
Метод get_products(self), который считывает всю информацию из файла __file_name, закрывает его
и возвращает единую строку со всеми товарами из файла __file_name.
Метод add(self, *products), который принимает неограниченное количество объектов класса Product.
Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию).
Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине'
'''

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r+')
        prod_str = file.read()
        file.close()
        return prod_str


    def add(self, *products):
        get_prod = self.get_products()
        for i in products:
            if self.get_products().find(f'{i.name},') == -1:
                file = open(self.__file_name, 'a')
                file.write(f'{i}\n')
                file.close()
            else:
                print(f'Продукт {i.name} уже есть в магазине')


s1 = Shop()
p1 = product('Potato', 50.5, 'Vegetables')
p2 = product('Spaghetti', 3.4, 'Groceries')
p3 = product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
