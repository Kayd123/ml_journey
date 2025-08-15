#creating a class
class Person:#person is a class
    def __init__(self, name, age):#__init__() assigns values or other operations
        self.name = name
        self.age = age
    def myfunc(self):#functions that belong to the object
        print('hello my name is {}'.format(self.name)+', age is {}'.format(self.age))
    def __str__(self):#The __str__() method controls what should be returned when the class object is represented as a string.
        return f"{self.name}({self.age})"

    pass
p1 = Person("John", 25)#p1 is an object
#p1.age =40
print(p1)
class Person1:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p2 = Person1("John", 36)
p2.myfunc()