class User:
    def __init__(self,user_id,name):
        self.user_id = user_id
        self.name = name 


    def get_id(self):
        return self.user_id
    
    def get_name(self):
        return self.name
    
    def dislay_details(self):
        print(f"ID: {self.get_id}, Name: {self.get_name}")
    
class Student(User):
    def __init__(self,user_id,name):
        super().__init__(self,user_id,name)
        self._course = None 

    def enroll_course(self,course):
        self.course = course

    def dislay_details(self):
        print(f"Student's Name: {self.get_name}, Student's ID: {self.get_id}")
        print(f"Course Enrolled: {self._course}")

class Mentor(User):
    def __init__(self,user_id,name):
        super().__init__(self,user_id,name)
        self._students = []

    def assign_students(self,students):
        self._students.append(students)

    def dislay_details(self):
        print(f"Mentor Name: {self.get_name}, Mentoe ID: {self.get_id}")
        print("Assigned Students ", [s.get_name() for s in self._students])

class Admin(User):
    def display_all(self,students,mentors):
        print("\n---Students---")
        for s in students:
            s.display_details()

        print("\n---Mentors---")
        for m in mentors:
            m.dislay_details()
        
students = []
mentors = []
admin = Admin("A1", "Admin")
while True:
    print("\n===== EDTECH MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Add Mentor")
    print("3. Enroll Student in Course")
    print("4. Assign Student to Mentor")
    print("5. Mentor View Students")
    print("6. Admin View All Details")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        sid = input("Enter Student ID: ")
        name = input("Enter Name: ")
        students.append(Student(sid, name))

    elif choice == "2":
        mid = input("Enter Mentor ID: ")
        name = input("Enter Name: ")
        mentors.append(Mentor(mid, name))

    elif choice == "3":
        sid = input("Student ID: ")
        course = input("Course Name: ")
        for s in students:
            if s.get_id() == sid:
                s.enroll_course(course)

    elif choice == "4":
        sid = input("Student ID: ")
        mid = input("Mentor ID: ")
        stu = next((s for s in students if s.get_id() == sid), None)
        men = next((m for m in mentors if m.get_id() == mid), None)
        if stu and men:
            men.assign_student(stu)

    elif choice == "5":
        mid = input("Mentor ID: ")
        for m in mentors:
            if m.get_id() == mid:
                m.display_details()

    elif choice == "6":
        admin.display_all(students, mentors)

    elif choice == "7":
        break

    else:
        print("Invalid choice!")
