print('you are hearing me talk')

class Member():
    def __init__(self, name):
        self.fullname = name
    def introduce(self):
        print(f"Hi I am {self.fullname}")

class Student(Member):
    def __init__(self, name, reason):
        super().__init__(name)
        self.reason = reason
        self.type = "Student"

class Instructor(Member):
    def __init__(self, name, bio):
        super().__init__(name)
        self.bio = bio
        self.type = "Instructor"
        self.skills = []
    def add_skill(self, skill):
        self.skills.append(skill)

class Workshop():
    def __init__(self, date, subject):
        self.date = date
        self.subject = subject
        self.bullpen = []
        self.roster = []
    def add_participant(self, newmember):
        if newmember.type == "Student":
            self.roster.append(newmember)
        if newmember.type == "Instructor":
            self.bullpen.append(newmember)


    def print_workshop(self):
        print("Workshop:")
        print("Date: "+self.date)
        print("Subject: "+self.subject)

    def print_students(self):
        print("Students:")
        for student in self.roster:
            print("Name: "+student.fullname)
            print("Reason: "+student.reason)

    def print_instructors(self):
        print("Instructors")
        for teacher in self.bullpen:
            print("Name: "+teacher.fullname)
            print("Bio: "+teacher.bio)
            for skill in teacher.skills:
                print(skill)

    def print_details(self):
        print('Details:')
        self.print_workshop()
        self.print_students()
        self.print_instructors()




workshop = Workshop("12/03/2014", "Shutl")

jane = Student("Jane Doe", "I am trying to learn programming and need some help")
lena = Student("Lena Smith", "I am really excited about learning to program!")
vicky = Instructor("Vicky Python", "I want to help people learn coding.")
vicky.add_skill("HTML")
vicky.add_skill("JavaScript")
nicole = Instructor("Nicole McMillan", "I have been programming for 5 years in Python and want to spread the love")
nicole.add_skill("Python")

workshop.add_participant(jane)
workshop.add_participant(lena)
workshop.add_participant(vicky)
workshop.add_participant(nicole)

# print(workshop.subject)
# print(jane.fullname)
# print(lena.fullname)
# print(vicky.fullname)
# print(nicole.fullname)

#workshop.print_workshop()
#workshop.print_students()
#workshop.print_instructors()
workshop.print_details()

