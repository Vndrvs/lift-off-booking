from abc import ABC, abstractmethod

# currently these are only samples

class Jarat(ABC):
    def __init__(self, number, destination, ticket_fare):
        self._number = number
        self.destination = destination
        self.ticket_fare = ticket_fare

class BelfoldiJarat(Jarat):
    def __init__(self, number, destination, ticket_fare):
        super().__init__(number, destination, ticket_fare)

class NemzetkoziJarat(Jarat):
    def __init__(self, number, destination, ticket_fare):
        super().__init__(number, destination, ticket_fare)

class LegiTarsasag():
    def __init__(self, name, headquarters_location):
        self.name = name
        self.headquarters = headquarters_location

class JegyFoglalas():
    def __init__(self, booking_id, date, jarat, first_name, surname, email):
        self.id = booking_id
        self.date = date
        self.jarat = jarat
        self.first_name = first_name
        self.surname = surname
        self.email = email

'''
Járat (absztrakt osztály): Definiálja a járat alapvető attribútumait (járatszám, célállomás, jegyár).
BelföldiJarat: Belföldi járatokra vonatkozó osztály, amelyek olcsóbbak és rövidebbek.
NemzetkoziJarat: Nemzetközi járatokra vonatkozó osztály, magasabb jegyárakkal.
LégiTársaság: Tartalmazza a járatokat és saját attribútumot, mint például a légitársaság neve.
JegyFoglalás: A járatok foglalásához szükséges osztály, amely egy utazásra szóló jegy foglalását tárolja.

Funkciók
Jegy foglalása: A járatokra jegyet lehet foglalni, és visszaadja a foglalás árát.
Foglalás lemondása: A felhasználó lemondhatja a meglévő foglalást.
Foglalások listázása: Az összes aktuális foglalás listázása.
Adatvalidáció

Ellenőrzi, hogy a járat elérhető-e foglalásra, és hogy a foglalás időpontja érvényes-e.
Biztosítja, hogy csak létező foglalásokat lehessen lemondani.

Felhasználói interfész
Egyszerű felhasználói interfész, amely lehetővé teszi a következő műveleteket:
Jegy foglalása
Foglalás lemondása
Foglalások listázása

Előkészítés
A rendszer indulásakor egy légitársaság, 3 járat és 6 foglalás előre be van töltve a rendszerbe, így a felhasználó azonnal használatba veheti a rendszert.
'''