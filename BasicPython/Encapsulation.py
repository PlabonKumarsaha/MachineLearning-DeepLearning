class Person:
    # __ is for encalpusaltion
    def __init__(self, person_name: str, date_of_birth, heigh: int):
        self.__name = person_name
        self.__date_of_birth = date_of_birth
        self.__height = height

    def getName(self):
        return self.__name

    def setName(self, updatedName):
        if(self.__has_any_number(updatedName)):
            print(" Person cant have number in their name")
            return
        self.__name = updatedName

    def __has_any_number(self, string):
        return "0" in string

    def getSummary(self):
        return f"Name : {self.name}, height : {self.height} dob : {self.date_of_birth}"


a_person = Person("Plabon", "1998", "6ft")
b_person = Person("Taraq", "1992", "7 ft")

print(a_person.getSummary())

a_person.setName("Plabon Kumar Saha")
print(a_person.getSummary())

print(b_person.getName())
