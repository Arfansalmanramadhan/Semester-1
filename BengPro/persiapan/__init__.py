class Hero:
    def __init__(self, x, y, j):
        # print("Arfan", x)
        self.name = x
        self.attack = y
        self.attacks = j


# hero1 = Hero(10)
hero2 = Hero("Arfan ", "salman ", "Ramadhan")
# print(hero1.name)
print(hero2.__dict__)
# print(hero2.attack)
# print(hero2.attacks)
