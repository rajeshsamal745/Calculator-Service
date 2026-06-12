# Backend addition logic
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

if __name__ == "__main__":
    print("Addition Example:", add(5, 3))
    print("Subtraction Example:", subtract(5, 3))
    print("Multiplication Example:", multiply(5, 3))
    print("Division Example:", divide(5, 0))
