# app/cli.py
from app.calculator import sqrt, factorial, ln, power
import sys

MENU = """
Scientific Calculator
Choose operation:
1) sqrt(x)
2) factorial(n)
3) ln(x)
4) x^b
5) Exit
"""
#prompt
def prompt():
    while True:
        print(MENU)
        choice = input("Enter choice [1-5]: ").strip()
        if choice == "1":
            x = float(input("Enter x: "))
            try:
                print("Result:", sqrt(x))
            except Exception as e:
                print("Error:", e)
        elif choice == "2":
            n = int(input("Enter n (integer >= 0): "))
            try:
                print("Result:", factorial(n))
            except Exception as e:
                print("Error:", e)
        elif choice == "3":
            x = float(input("Enter x (x>0): "))
            try:
                print("Result:", ln(x))
            except Exception as e:
                print("Error:", e)
        elif choice == "4":
            x = float(input("Enter x: "))
            b = float(input("Enter b: "))
            try:
                print("Result:", power(x, b))
            except Exception as e:
                print("Error:", e)
        elif choice == "5":
            print("Exiting.")
            sys.exit(0)
        else:
            print("Invalid choice")

if __name__ == "__main__":
    prompt()
