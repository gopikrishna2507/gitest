"""
Main application entry point.
Demonstrates calculator module usage.
"""

from calculator import add, subtract, multiply, divide, power

def run_demo():
    print("========================================")
    print("   [+] Python Git Demo Calculator")
    print("========================================")
    
    num1, num2 = 10, 5
    
    print(f"{num1} + {num2} = {add(num1, num2)}")
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
    print(f"{num1} / {num2} = {divide(num1, num2)}")
    print(f"{num1} ^ {num2} = {power(num1, num2)}")
    print("========================================")


if __name__ == "__main__":
    run_demo()
