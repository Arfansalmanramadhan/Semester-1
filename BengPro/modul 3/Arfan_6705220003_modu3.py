# python arrays
# import re
# import json
# import math
# import datetime
# import platform
# import mymodule
cars = ["Food", "volvo", "BMW"]
print(cars)
cars = ["Food", "volvo", "BMW"]
cars[0] = "Toyota"
print(cars)
# claaa /objek


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"


p1 = Person("Arfan", 20)
print(p1)


class Mahasiswa:
    def __init__(self, nama="", nim=0, kelas=""):
        self.nama = input(str("Masukan nama :"))
        self.nim = input(str("Masukan nim :"))
        self.kelas = input(str("Masukan kelas :"))


mhs1 = Mahasiswa()

print(mhs1.nama)
print(mhs1.nim)
print(mhs1.kelas)

# python inhentace


class Person:
    def __init__(self, fname, iname):
        self.depan = fname
        self.belakang = iname

    def printname(self):
        print(self.depan, self.belakang)


x = Person("Arfan", "Salman")
x.printname()


class Person:
    def __init__(self, fname, iname):
        self.depan = fname
        self.belakang = iname

    def printname(self):
        print(self.depan, self.belakang)


class Student(Person):
    def __init__(self, fname, iname):
        super().__init__(fname, iname)
        self.graduationyeart = 2022


x = Student("Arfan", "Salman")
print(x.graduationyeart)


# python iterator
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))


mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


class MyNumbers:
    def __iter__(self):
        self.a = 0
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


# python scope
def funct():
    x = 300
    print(x)


funct()

x = 300


def funct():
    print(x)


funct()
print(x)

mymodule.greeting("Arfan")


x = platform.system()
print(x)


x = datetime.datetime.now()
print(x)
x = datetime.datetime(2022, 11, 20)
print(x)

x = min(5, 10, 25)
y = max(5, 10, 25)
print(x)
print(y)

x = abs(-7.20)
print(x)
x = pow(-7, 20)
print(x)

x = math.sqrt(64)
print(x)

x = math.ceil(1.4)
y = math.floor(1.4)
print(x)
print(y)

x = math.pi
print(x)

x = '{"name": "jhon", "age":45, "city":"New york"}'

y = json.loads(x)
print(x)

x = {
    "name": "jhon",
    "age": 45,
    "city": "New York"
}

y = json.dumps(x)
print(y)

print(json.dumps({"name": "jojo", "age": 67}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(["apple", "bananas"]))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

txt = "The rain in Spain"
x = re.search("Portugal", txt)
if x:
    print("Yes! We have a match!")
else:
    print("No match")
