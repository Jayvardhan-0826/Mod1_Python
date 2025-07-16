def add_student():
    with open("students.txt", "a") as f:
        name = input("Enter student name: ").strip()
        marks = input("Enter student marks: ").strip()
        f.write(name + "," + marks + "\n")
        print("✅ Student added successfully.\n")


def search_student():
    query = input("Enter the student name to search for: ").strip().lower()
    found = False

    with open("students.txt", "r") as f:
        for line in f:
            name, marks = line.strip().split(",")  # split by comma
            if name.lower() == query:
                print(f"✅ Student Found: {name} - {marks} marks\n")
                found = True
                break

    if not found:
        print("❌ Student not found.\n")


def view_all():
    print("📄 All Student Records:")
    with open("students.txt", "r") as f:
        for line in f:
            name, marks = line.strip().split(",")
            print(f"{name} - {marks} marks")
    print()  # blank line


# Main CLI Loop
while True:
    print("**** CLI Student Marks Manager ****")
    print("1. Add Student")
    print("2. Search Student")
    print("3. View All Records")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice (1-4): "))
        print()  # newline for spacing

        if choice == 1:
            add_student()
        elif choice == 2:
            search_student()
        elif choice == 3:
            view_all()
        elif choice == 4:
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please choose a valid option.\n")
    except ValueError:
        print("⚠️ Please enter a valid number.\n")
