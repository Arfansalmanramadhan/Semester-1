# class Hero:
#     jumlah = 0

#     def __init__(self, x, y, j, z):
#         self.name = x
#         self.umur = y
#         self.alamat = j
#         self.kulia = z
#         Hero.jumlah += 1

#     def siapa(self):
#         print("Nameku " + self.name)


# halo = print("Arfan", 20, "Bandung", "stt Telkom")
# halo2 = print("Salman", 20, "Bandung", "stt Telkom")

# halo.siapa()
# import modul
# import datetime
# import json


class Orang:
    def __init__(self, nama, tahu):
        self.name = nama
        self.tahu = tahu

    def print(self):
        print(self.name, self.tahu)


halo = Orang("Arfan", 20)
halo.print()


# class Orang:
#     def __init__(self, depan, belakang):
#         self.depan = depan
#         self.belakang = belakang

#     def peint(self):
#         print(self.depan, self.belakang)


# class Siswa(Orang):
#     def __init__(self, depan, belakang):
#         super().__init__(depan, belakang)
#         self.lulus = 2025


# a = Siswa("Arfan", " Salman")
# print(a)
# print(a.lulus)
# buah = ["apel", "pisang", "nanas"]
# buah[2] = "anggur"
# print(buah)

# buahh = "Apell"
# s = iter(buahh)
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))


# class Nomber:
#     def __iter__(self):
#         self.a = 1
#         return self

#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x


# kelasku = Nomber()
# kelas = iter(kelasku)
# print(next(kelas))
# print(next(kelas))
# print(next(kelas))
# print(next(kelas))
# print(next(kelas))
# print(next(kelas))


# def fungsi():
#     x = 200
#     print(x)


# fungsi()
# x = 200
# fungsi()
# # print(x)

# print(modul.halo(3, 3))

# x = datetime.datetime.now()
# print(x)


# a = open("dataku.json")

# data = json.loads(a.read())
# print(f"Nama: {data['name']}")
# print(f"Website: {data['web']}")
# print("Sosial Media:")
# print(f"- Facebook: {data['social_media']['facebook']}")
# print(f"- Twitter: {data['social_media']['twitter']}")
# print(f"- Instagram: {data['social_media']['instagram']}")

# username = str(input("masukan username:"))
# password = str(input("masukan password:"))

# if username == ("admin"):
#     if password == ("admin"):
#         print("login berhasil")
#     else:
#         print("password salah")
# else:
#     if password == ("admin"):
#         print("username salah")
#     else:
#         print("Gagal masuk")

# # # versi variabel
# a = float(input("Tulis nilai alas: "))
# b = float(input("Tulis nilai tinggi: "))
# luas = 0.5*a*b
# print("Jumlah luas segitiga: ", luas)

# # versi fungsi


# def segitiga(a, b):
#     return 0.5*a*b


# print(segitiga(10, 15))
