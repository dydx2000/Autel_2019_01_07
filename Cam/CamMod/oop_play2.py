class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.weight = 'weight'

    def talk(self):
        print("person is talking....")


class Chinese(Person):

    def __init__(self, name, age, language):  # 先继承，在重构
        Person.__init__(self, name, age)  # 继承父类的构造方法，也可以写成：super(Chinese,self).__init__(name,age)
        self.language = language  # 定义类的本身属性

    def walk(self):
        print('is walking...')


class American(Person):
    def __init__(self,name,age,language):
        super(American,self).__init__(name,age)
        # Person.__init__(self,name,age)
        self.language =language
    def prininfo(self):
        print("My name is %s,I am %s years old! I'am speaking %s!"%(self.name,self.age,self.language))



c = Chinese('bigberg', 22, 'Chinese')

a = American('Bob',15,'American English')
a.prininfo()
b = American('Denies',25,'English')
b.prininfo()