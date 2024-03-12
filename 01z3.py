class Samochod:
    def __init__(self, marka, model, rok):
        self.marka = marka
        self.model = model
        self.rok = rok

object1 = Samochod("audi", "audi1", "2001 r.")
object2 = Samochod("ford", "fordX", "1999 r.")
object3 = Samochod("kia", "kia8", "3002 r.")

print ("Object 1 (marka, model, rok):", object1.marka, "," ,object1.model,"," ,object1.rok)
print ("Object 2 (marka, model, rok):", object2.marka, "," ,object2.model,"," ,object2.rok)
print ("Object 3 (marka, model, rok):", object3.marka, "," ,object3.model,"," ,object3.rok)