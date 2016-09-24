from types import MethodType


class Student(object):
    __slot__ = ('name','age')
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayHi(self):
        print("I am {name}".format(name=self.name))

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    # def __len__(self):
    #     return 66


if __name__ == '__main__':
    oc = Student('oc', 18)
    dd = Student('dd', 22)

    def xx(self):
        return 5
    Student.xx = MethodType(xx,Student)

    print(Student.__slot__)

