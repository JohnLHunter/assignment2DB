import sqlite3
from pandas import DataFrame
#From StudentClass import(studentclass)

conn = sqlite3.connect('assignment2')
# cursor is something that performs an action
c = conn.cursor()

def displayall(self):
    if self == 1:
        c.execute("""
                SELECT *
                FROM Student""")
        allRows = c.fetchall()
        df = DataFrame(allRows, columns=['StudentID', 'FirstName','LastName','GPA','Major','Advisor','isDeleted'])
        print(df)
        self = 0

def updatestudent(self):
    while self == "y" or self == "Y":
        StuIDW = input("Please enter the student ID of which student you want to update: ")
        if not isinstance(StuIDW, int):
            print("What you entered was not an int")
            StuIDW = input("Please enter the student ID of which student you want to update: ")
        Major = input("Enter the new Major: ")
        if not isinstance(Major, str):
            print("What you entered was not a string")
            Major = input("Enter the new Major: ")
        Adviosr = input("Enter the new Advisor: ")
        if not isinstance(Adviosr, str):
            print("What you entered was not a string")
            Major = input("Enter the new Advisor: ")
        c.execute("""
        UPDATE Student
        SET Major = ?, FacultyAdvisor = ?
        WHERE StudentId = ? """, (Major, Adviosr, StuIDW))
        self = input("Would you like to update another Student? (Y or N)")


def createstudent(self):
    while self == "y" or self == "Y":
        StuID = input("Please enter the student's id: ")
        FirstN = input("please enter the student's first name: ")
        LastN = input("please enter the student's last name: ")
        GPA_in = input("Please enter their GPA: ")
        major = input("Please enter their Major: ")
        FacAdvisor = input("please enter the last name of their advisor: ")
        isDeleted = False
        c.execute("""
        INSERT INTO Student(StudentId, FirstName, LastName, GPA, Major, FacultyAdvisor)
        VALUES (?,?,?,?,?,?)""",(StuID, FirstN, LastN, GPA_in, major, FacAdvisor,))
        self = input("Would you like to create another Student? (Y or N)")


def Deletestudent(self):
    while self == "y" or self == "Y":
        StuIDW = input("Please enter the student ID of which student you want to delete: ")
        c.execute("""
        UPDATE Student
        SET isDeleted = TRUE 
        WHERE StudentId = ? """, (StuIDW,))
        conn.commit()
        self = input("Would you like to delete another Student? (Y or N)")


def FindStudent(self):
    while self == "y" or self == "Y":
        type = input("What criteria do you wish to search for students? Pick between GPA, Major, and Advisor: ")
        if type == "GPA" or type == "gpa":
            GPA = input("Enter GPA: ")
            rows = c.execute("""
                            SELECT *
                            FROM Student
                            WHERE GPA = ?""",(GPA,))
            df = DataFrame(rows,
                           columns=['StudentID', 'FirstName', 'LastName', 'GPA', 'Major', 'Advisor', 'isDeleted'])
            print(df)
        elif type == "Major" or type == "major":
            Major = input("Enter Major: ")
            rows = c.execute("""
                            SELECT *
                            FROM Student
                            WHERE Major = ?""",(Major,))
            df = DataFrame(rows,
                           columns=['StudentID', 'FirstName', 'LastName', 'GPA', 'Major', 'Advisor', 'isDeleted'])
            print(df)
        elif type == "Advisor"or type == "advisor":
            Advisor = input("Enter the Advisor's Name: ")
            rows = c.execute("""
                            SELECT *
                            FROM Student
                            WHERE FacultyAdvisor = ?""",(Advisor,))
            df = DataFrame(rows,
                           columns=['StudentID', 'FirstName', 'LastName', 'GPA', 'Major', 'Advisor', 'isDeleted'])
            print(df)
        else:
            print("That was not an option")
        self = input("Would you like to search for more students? (Y or N): ")


go = 1
while go == 1:
    print("Student Database options:")
    print("Display all")
    print("Create")
    print("Update")
    print("Delete")
    print("Search")
    print("Exit")
    choice = input("Please type which option you'd like to pick: ")
    if choice == 'Display all' or choice == 'display all' or choice == 'display' or choice == 'Display':
        displayall(self=1)
        self=0
        conn.commit()
    elif choice == 'Create' or choice == 'create':
        createstudent(self="Y")
        self="n"
        conn.commit()
    elif choice == 'Update' or choice == 'update':
        updatestudent(self="Y")
        self="n"
        conn.commit()
    elif choice == 'Delete' or choice == 'delete':
        Deletestudent(self="Y")
        self="n"
        conn.commit()
    elif choice == 'Search' or choice == 'search':
        FindStudent(self="Y")
        self="n"
        conn.commit()
    elif choice == 'exit' or choice == 'Exit':
        self="n"
        go =2
    else:
        print("Im sorry that was not an option")









