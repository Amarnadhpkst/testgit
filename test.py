from enum import Enum

# Enum for operations
class Operation(Enum):
    ADD = 1
    SUBTRACT = 2
    MULTIPLY = 3

# Function to perform calculation
def calculate(op, a, b):
    if op == Operation.ADD:
        return a + b
    elif op == Operation.SUBTRACT:
        return a - b
    elif op == Operation.MULTIPLY:
        return a * b
    else:
        return None

# Main program
def main():
    print("Select Operation:")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")

    try:
        choice = int(input("Enter your choice (1/2/3): "))
        
        # Validate enum choice
        if choice not in [1, 2, 3]:
            print("❌ Invalid choice! Please enter 1, 2, or 3.")
            return
    try:
        choice = int(input("Enter your choice (1/2/3/4): "))

        # Validate enum choice
        if choice not in [1, 2, 3, 4]:
            print("❌ Invalid choice! Please enter 1, 2, 3, or 4.")
            return
        
        # Inputs for numbers
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        
        # Perform calculation
        operation = Operation(choice)
        result = calculate(operation, a, b)

        print(f"Result: {result}")

    except ValueError:
        print("❌ Invalid input! Please enter only numbers.")

# Run program
if __name__ == "__main__":
    main()
     

except ValueError:
    print("❌ Invalid input! Please enter only numbers.")
