'''Необходимо написать 3 класса:
Horse - класс описывающий лошадь. Объект этого класса обладает следующими атрибутами:
x_distance = 0 - пройденный путь.
sound = 'Frrr' - звук, который издаёт лошадь.
И методами:
run(self, dx), где dx - изменение дистанции, увеличивает x_distance на dx.

Eagle - класс описывающий орла. Объект этого класса обладает следующими атрибутами:
y_distance = 0 - высота полёта
sound = 'I train, eat, sleep, and repeat' - звук, который издаёт орёл (отсылка)
И методами:
fly(self, dy) где dy - изменение дистанции, увеличивает y_distance на dy.

Pegasus - класс описывающий пегаса. Наследуется от Horse и Eagle в том же порядке.
Объект такого класса должен обладать атрибутами классов родителей в порядке наследования.
Также обладает методами:
move(self, dx, dy) - где dx и dy изменения дистанции. В этом методе должны запускаться наследованные методы run и fly соответственно.
get_pos(self) возвращает текущее положение пегаса в виде кортежа - (x_distance, y_distance) в том же порядке.
voice - который печатает значение унаследованного атрибута sound.
Пункты задачи:
Создайте классы родители: Horse и Eagle с методами из описания.
Создайте класс наследник Pegasus с методами из описания.
Создайте объект класса Pegasus и вызовите каждый из ранее перечисленных методов, проверив их работу.'''



class Horse:
    x_distance = 0
    Horse_sound = 'Frrr'

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    y_distance = 0
    Eagle_sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def __init__(self):
        self.sound = super().Horse_sound
        self.sound = super().Eagle_sound

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        Pegasus_pos = (self.x_distance, self.y_distance)
        return Pegasus_pos

    def voice(self):
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
