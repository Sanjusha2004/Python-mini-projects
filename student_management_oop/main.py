class Student:

    def __init__(self, name, roll, marks,branch, location):
        self.name = name
        self.roll = roll
        self.marks = marks

students = []

while True:

    print("\n----- Student Management System -----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            name = input("Enter student name: ")

            if not name.isalpha():
                raise ValueError("Name should contain only alphabets!")


            roll = input("Enter roll number: ")

            if not roll.isdigit():
                raise ValueError("Roll number must contain digits!")
            
            marks = input("Enter marks: ")

            if not marks.isdigit():
                raise ValueError("Marks should contain only numbers!")

            s = Student(name, roll, marks)
            students.append(s)

            print("Student added successfully!")

        except ValueError as e:
            print("Error:", e)

    elif choice == "2":

        if len(students) == 0:
            print("No students found.")

        else:
            print("\nStudent List:")
            for s in students:
                print("Name:", s.name, "| Roll:", s.roll, "| Marks:", s.marks)

    elif choice == "3":

        search_roll = input("Enter roll number to search: ")
        found = False

        for s in students:
            if s.roll == search_roll:
                print("\nStudent Found!")
                print("Name:", s.name)
                print("Marks:", s.marks)
                found = True
                break

        if found == False:
            print("Student not found.")

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")