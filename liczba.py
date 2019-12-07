class Number:
    def __init__(self, v):
        self.value = v

    def wyzeruj(self):
        self.value = 0;

    def ustaw(self, wartosc):
        self.value = wartosc


number = Number(9)
print(number.value)
number.wyzeruj()
print(number.value)
number.ustaw(11)
print(number.value)