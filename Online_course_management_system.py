# create a class
class Onlinecourse:
    def __init__(self,course_name,instructor):
        self.course_name=course_name
        self.instructor=instructor
        self.student_names=[]
    def Enroll_student(self,students):
        self.student_names.append(students)
        print(f"{students.name} has successfully enrolled in {self.course_name} course")
    def course_details(self):
        print(f"course name: {self.course_name}")
        print(f"Instructor name : {self.instructor}")
        print(f"enrolled student list: ")
        for student in self.student_names:
            print(student.name)

    def completed_course(self,name):
        for student in self.student_names:
            if student.name in name:
                self.student_names.remove(student)
                print(f"{name} has completed course")
        print(f"{name} is not enrolled in the course")
    def avggrades(self,grades):
        total=sum(students.grades)
        average=total/len(students.grades)
        print(f"the average grade of the student is : {average}")
class Student:
    def __init__(self,name,grades):
        self.name=name
        self.grades=grades


course_name=input("enter course name: ")
instructor=input("enter instructor name: ")

mycourse=Onlinecourse(course_name,instructor)
num_of_students=int(input("enter the number of students: "))
for _ in range(num_of_students):
    studentname=input("enter student name: ")
    grades=[]
    for i in range(5):
        grade=int(input("Enter student grade: "))
        grades.append(grade)
    students=Student(studentname,grades)
    mycourse.Enroll_student(students)
    mycourse.avggrades(students)
mycourse.course_details()
