class Hero:
    jumlah = 0

    def __init__(self, x, y, j):
        # print("Arfan", x)
        self.name = x
        self.attack = y
        self.attacks = j
        Hero.jumlah += 1
        print("masukan nama " + x)


hero1 = Hero("Arfan ", "salman ", "Ramadhan")
print(Hero.jumlah)
hero2 = Hero("Arfan ", "salman ", "Ramadhan")
print(Hero.jumlah)
hero3 = Hero("Arfan ", "salman ", "Ramadhan")
print(Hero.jumlah)
