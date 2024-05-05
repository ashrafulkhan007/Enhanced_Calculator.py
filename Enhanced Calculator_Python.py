# Annotation is important for readability and maintainability only.
def addition(x: float, y: float) -> float: 
    """Perform addition operation."""
    return x + y

def subtraction(x: float, y: float) -> float:
    """Perform subtraction operation."""
    return x - y

def multiplication(x: float, y: float) -> float:
    """Perform multiplication operation."""
    return x * y

def division(x: float, y: float) -> float:
    """Perform division operation."""
    if y == 0:
        raise ValueError("Division by zero is not allowed.")
    return x / y

def modulus(x: float, y: float) -> float:
    """Perform modulus operation."""
    if y == 0:
        raise ValueError("Modulus by zero is not allowed.")
    return x % y

def is_number(value: str) -> bool:
    """Check if the input string can be converted to a number."""
    try:
        float(value)
        return True
    except ValueError:
        return False

def get_number_input(prompt: str) -> float:
    """Prompt the user for a number input and validate it."""
    while True:
        user_input = input(prompt)
        if is_number(user_input):
            return float(user_input)
        else:
            print("\n This is not a number. Please enter a valid number. \n")

def enhanced_calculator():
    """Main function to execute the calculator program."""
    
    while True:
        # Take the choice of operation from the user
        operation = input("Input Operator ('+', '-', '*', '/', '%' 'Exit'): ")

        if operation in ('+', '-', '*', '/', '%'):
            num1 = get_number_input("Enter first number: ")
            num2 = get_number_input("Enter second number: ")

            if operation == '+':
                print("Result:", addition(num1, num2))
            elif operation == '-':
                print("Result:", subtraction(num1, num2))
            elif operation == '*':
                print("Result:", multiplication(num1, num2))
            elif operation == '/':
                try:
                    print("Result:", division(num1, num2))
                except ValueError as e:
                    print(e)
            elif operation == '%':
                try:
                    print("Result:", modulus(num1, num2))
                except ValueError as e:
                    print(e)
        elif operation.lower() == 'exit':
            """converts the user input to lowercase before checking if it matches 'Exit', 
            allowing the user to type 'Exit', 'EXIT', or 'exit' in any case."""
            print("Exiting...")
            break 
        else:
            print("\n Invalid input. Please enter a valid operator. \n")

# Execute the enhanced_calculator program
enhanced_calculator()
