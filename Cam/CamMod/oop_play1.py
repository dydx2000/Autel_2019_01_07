class Person(object):  # 定义一个父类

    def talk(self):  # 父类中的方法
        print("person is talking....")


class Chinese(Person):  # 定义一个子类， 继承Person类

    def walk(self):  # 在子类中定义其自身的方法
        print('is walking...')


c = Chinese()
# c.talk()  # 调用继承的Person类的方法
# c.walk()  # 调用本身的方法

class Cantonese(Person):
    def eat(self):
        print("is eating...!")

class Shenzheness(Cantonese):
    def play(self):
        print("is playing...!")

can = Cantonese()
# can.eat()

sz=Shenzheness()
sz.play()
sz.eat()
sz.talk()

