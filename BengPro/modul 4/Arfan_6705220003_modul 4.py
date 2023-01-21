import os
import camelcase
c = camelcase.CamelCase()
txt = "Halo Dunia"
print(c.hump(txt))


try:
    print(x)
except:
    print("anda selesai")


try:
    print(x)
except NameError:
    print("Variable x")
except:
    print("anda selesai")

try:
    print("halo")
except:
    print("anda selesai")
else:
    print("ada")
try:
    print("halo")
except:
    print("anda selesai")
finally:
    print("selesai")


namapeguna = input("Masukan nama anda :")
print("Nama anda: " + namapeguna)

price = 50
txt = "the peice {} dollars"
print(txt.format(price))

quant = 50
itemo = 100
price = 40
txt = "I WANT {} pieces of item number {} for {:.3f} dollars"
print(txt.format(quant, itemo, price))

umur = 20
nama = "Arfan"
kelas = "D3TT 45-03"
txt = "Hai nama saya {1}. {1} saya umur {0} tahun saya kelas {2}"
print(txt.format(umur, nama, kelas))


myoder = " I Have a {campuran},it is A {MODEL}"
print(myoder.format(campuran="Arfan", MODEL="salman"))

# f = open("model.txt")
f = open("model.txt", "r")
print(f.read())
f.close()
f = open("D:\\arfan\kuliah\semester 1\pemrograman 1\perkodean\modul 4\model.txt", "r")
print(f.read())
f.close()

f = open("model.txt", "r")
print(f.readline(2))

f = open("model.txt", "r")
print(f.readline())
print(f.readline())
f = open("model.txt", "r")
for x in f:
    print(x)

f = open("model.txt", "r")
print(f.readline())
f.close()

f = open("model1.xt", "a")
f.write("Selamat bwlajar CSS")
f.close()
f = open("model1.xt", "r")
print(f.read())

os.remove("modul2.txt")


if os.path.exists("modul2.txt"):
    os.remove("modul2.txt")
else:
    print("file ini tidak ada")


os.mkdir("ARFAN")
os.rmdir("ARFAN")
