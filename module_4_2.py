def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

        inner_function() #не работает, ничего не возвращает

inner_function() # Ошибка: 'inner_function' is not defined. Did you mean: 'test_function'?
# Возникла из-за разницы пространства имен, написана внутри inner_function(),






