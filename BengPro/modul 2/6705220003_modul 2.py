thislist = ["apple", "banaa", "cherry"]
print(thislist[1])
print(thislist[-1])
a = ["JavaScript", "PHP", "Python", "C++"]
a[2:3] = ["C", "C#"]
print(a)
c = ["front end", "back end"]
b = ["Developer"]
c.append("Full strak")
c.extend(b)
print(c)
d = ["front end", "back end"]
d.pop(0)
print(d)
e = ["JavaScript", "PHP", "Python", "C++"]
e.clear()
print(e)
let = ["ARFAN", "SALMAN", "RAMADHAN"]
for i in range(len(let)):
    print(let[i])

fruits = ["JavaScript", "PHP", "Python", "C++"]
g = []
for i in fruits:
    if "a" in i:
        g.append(i)
print(g)

angka = [x for x in range(10)]
print(angka)
angkaa = []
for x in range(10):
    print(angka[x])

fruits = ["apple", "banana", "apel", "pisang"]
new = ['helo' for x in fruits]
print(new)
neww = ['helo']
for x in fruits:
    print(neww)

fruits = ["apple", "banana", "apel", "pisang"]
fruits.sort()
print(fruits)
kop = ["apple", "banana", "apel", "pisang"]
bila = kop.copy()
print(bila)
billa = list(kop)
print(billa)
z = ("apple", "banana", "apel", "pisang", "nanas")
y = list(z)
y[1] = "kiri"
z = tuple(y)
print(z)
thisdict = {
    "nama": "arfan",
    "asal": "Bandung"
}
thisdict["kuliah"] = "stt telkom"
print(thisdict)
s = (2, 4, 5, 10)
d = list(s)
print(d)
print(type(d))
d.insert(3, 11)
print(d)
s_insert = tuple(d)
print(s_insert)
print(type(s_insert))

c = (45, 33, 25, 64, 50)
d = list(c)
print(c)
print(type(c))
d.append(100)
d.append(10)
print(d)
c = tuple(d)
print(d)
# perkondinisian
bil1 = int(input("Masukkan bilangan pertama:"))
bil2 = int(input("Masukkan bilangan kedua:"))
x = bil1
z = bil2
while x != z:
    if x > z:
        z = bil2 + z
    else:
        x = bil1 + x
print("Nilai dari kpk dari", bil1, "dan", bil2, "Adalah", x)
nilai = int(input("Masukkan nilai: "))
usia = int(input("Masukkan usia: "))
if nilai >= 75:
    if (usia < 15):
        print('Selamat adek, kamu lulus!')
    else:
        print('Selamat kaka, kamu lulus')
else:
    if (usia < 15):
        print('Mohon maaf adek, coba lagi ya!')
    else:
        print('Mohon maaf kaka, coba lagi ya')
# functon


def pangkat(a, b):
    return a ** b


print(pangkat(2, 3))
