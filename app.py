def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def calculator():
    print("Welcome to the Calculator!")
    
    operations = {
        '1': ('Addition', add),
        '2': ('Subtraction', subtract),
        '3': ('Multiplication', multiply),
        '4': ('Division', divide)
    }
    
    while True:
        print("\nAvailable operations:")
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")
        print("5. Quit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '5':
            print("Thank you for using the Calculator!")
            break
        
        if choice not in operations:
            print("Invalid choice. Please try again.")
            continue
        
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            operation_name, operation_func = operations[choice]
            result = operation_func(num1, num2)
            
            print(f"{operation_name} result: {result}")
        
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    calculator()
