class house:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        floor = 0
        print(f'Здание {self.name} имеет {self.number_of_floors} этажей: Поднимаемся на {new_floor} этаж')
        if new_floor < 1 or new_floor > self.number_of_floors:
            print(f'{new_floor} - такого этажа не существует')
        else:
            for floor in range(new_floor):
                print(floor + 1)


h1 = house('ЖК Горский', 18)
h2 = house('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
