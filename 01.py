class Kalkulator:
    def dodawanie(self, x, y):
        return x + y
    
    def odejmowanie(self, x, y):
        return x - y

    def mnozenie(self, x, y):
        return x * y

object1 = Kalkulator()

print("Dodawanie: ", object1.dodawanie(7, 2))
print("Odejmowanie: ", object1.odejmowanie(7, 2))
print("Mnozenie: ", object1.mnozenie(7, 2))


object2 = Kalkulator()
print("Mnozenie: ", object2.mnozenie(7, 2))