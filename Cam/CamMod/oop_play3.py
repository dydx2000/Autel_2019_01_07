class Person(object):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def print_title(self):
        if self.sex == "male":
            print("Boy")
        elif self.sex == "female":
            print("Girl")


class Child(Person):  # Child 继承 Person
    def __init__(self,name,sex,hob,mum,dad):
        Person.__init__(self,name,sex)
        # super(Child,self).__init__(name,sex)
        self.hob = hob
        self.mother =mum
        self.father =dad
    def descMyself(self):
        print('My name is %s ,I like %s,my father is %s,my mother is %s!'%(self.name,self.hob,self.father,self.mother))

May = Child("May", "female",'Play Game',"Merry",'Bob')
# Peter = Person("Peter", "male")

# print(May.name, May.sex, Peter.name, Peter.sex)  # 子类继承父类方法及属性
May.print_title()
# Peter.print_title()
May.descMyself()