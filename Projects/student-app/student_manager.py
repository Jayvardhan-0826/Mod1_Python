def add_student():
    #ADD student code
        with open("students.txt", "a") as f:
            name = input("Enter student name:").strip()
            marks =input("Enter student marks:").strip()
            f.write(name + "," + marks + "\n")
            print("Student added successfully")
def search_student():
    #SEARCH student code
    query=input("enter the student name to search for: ").strip().lower()
    found =False
    
    with open("students.txt",'r') as f:
            for line in f:
               name, marks =line.strip().split(",") #split by comma
               if query == name.lower():
                    print(f"student found: {name}- {marks} marks\n")
                    found = True
                    break
    if not found :
         print("student not found")
def view_all():
    with open("students.txt", "r") as f:
          for line in f:
               name, marks =line.strip().split(",")
               print(name, " ",marks,"marks")
    print()
while True:
    print("****CLI Student Marks Manager****")
    print("1. ADD student")
    print("2. Search Student")
    print("3. View all records")
    print("4. Exit")

    choice = int(input("Enter your choice(1-4): "))
    if choice ==1:
       add_student()
    elif choice==2:
       search_student()
    elif choice==3:
         view_all()
    elif choice ==4:
         print("Goodbye")
         break
    else:
         print("Invalid choice. Please choose a valid option.")



