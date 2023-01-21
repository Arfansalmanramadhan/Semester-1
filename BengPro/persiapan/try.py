try:
    print(x)
except:
    print("anda selesai")

try:
    print(x)
except NameError:
    print("xa")
except:
    print("anda selesai")

try:
    print("Hai")
except:
    print("anda Selesai")
else:
    print("ada")

try:
    print("Halo")
except:
    print("mau pergi?")
finally:
    print("sampai jumpa")


nama = input("Masukan nama")
print("Hai nama ku " + nama)

nama = "Arfan"
umur = 20
hobi = "Coding"

text = "Hai nama saya {0} saya berumur {1} hobi saya {2}"
print(text.format(nama, umur, hobi))
# def Fizzbuzz(a, b):
#     for a in range(a, b+1):
#         if a % 3 == 0 and a % 5 == 0:
#             print("FizzBuzz")
#         elif a % 3 == 0:
#             print("fizz")
#         elif a % 5 == 0:
#             print("Buzz")
#         else:
#             print(a)


# Fizzbuzz(1, 21)
