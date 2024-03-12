class Osoba:
    def __init__(self,name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

osoba1 = Osoba("John", "Kowalski", "20")

print(osoba1.name)