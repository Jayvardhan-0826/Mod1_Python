while True:
    print("\n--- Simple Calculator ---")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Choose operation (+, -, *, /): ")

    if op == '+':
        print(f"Result: {a + b}")
    elif op == '-':
        print(f"Result: {a - b}")
    elif op == '*':
        print(f"Result: {a * b}")
    elif op == '/':
        if b != 0:
            print(f"Result: {a / b}")
        else:
            print("Division by zero not allowed!")
    else:
        print("Invalid operation")

    cont = input("Do you want to continue? (y/n): ")
    if cont.lower() != 'y':
        break
