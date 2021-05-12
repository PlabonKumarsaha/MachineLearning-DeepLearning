class Person:
    def __init__(self, person_name, date_of_birth, height):
        self.name = person_name
        self.date_of_birth = date_of_birth
        self.height = height

    def getName(self):
        return self.name

    def setName(self, updatedName):
        self.name = updatedName

    def getSummary(self):
        return f"Name : {self.name}, height : {self.height} dob : {self.date_of_birth}"


a_person = Person("Plabon", "1998", "6ft")
b_person = Person("Taraq", "1992", "7 ft")

print(a_person.getSummary())

a_person.setName("Plabon Kumar Saha")
print(a_person.getSummary())

print(b_person.getName())
