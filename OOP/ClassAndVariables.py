# class creation
class Student:
    # class variable
    num_of_students =0
    def __init__(self, fname, lname, id, section):
        # instance variable
        self.fname = fname
        self.lname =lname
        self.id = id
        self.section = section
        # increments once a new instance is created
        Student.num_of_students +=1;
    def fullName(self):
        print(self.fname + ' '+self.lname)


# Object creation
student = Student('Plabon','Kumar', 10, "A")
print(student.fname)
print(student.id)

student.fullName()
student1 = Student('Hi','HU', 11, "A")

print(Student.num_of_students)