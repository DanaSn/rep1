class Ksiazka:
    def __init__(self, tytul, autor, rok):
        self.tytul = tytul
        self.autor = autor
        self.rok = rok

object1 = Ksiazka("coś", "John W. Campbell", "1938 r.")
object2 = Ksiazka("harry potter", "fordX", "1999 r.")
object3 = Ksiazka("kicia  kocia", "kia8", "2022 r.")

print ("Object 1 (tytul, autor, rok):", object1.tytul, "," ,object1.autor,"," ,object1.rok)
print ("Object 2 (tytul, autor, rok):", object2.tytul, "," ,object2.autor,"," ,object2.rok)
print ("Object 3 (tytul, autor, rok):", object3.tytul, "," ,object3.autor,"," ,object3.rok)