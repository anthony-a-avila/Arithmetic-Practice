"""
This program is designed to assist a tutor in helping a student build proficiency in fundamental arithmetic operations.
It generates random arithmetic problems involving addition, subtraction, multiplication, division, squares, and cubes.

The program is intended to be used in the following way:
1. The tutor reads each arithmetic expression aloud to the student.
2. The student responds by giving the answer aloud, without looking at the screen.
3. The tutor can press ENTER to reveal the correct answer, and move on to the next problem.
4. In later rounds, the tutor may ask the student to use pencil and paper to compute answers for more complex problems,
    such as multiplication of larger numbers or divisions that involve remainders.

This approach helps remediate gaps in the student's understanding by reinforcing mental arithmetic before progressing 
to more advanced topics like algebra.
"""

import random
import time
import operator

def generate_problems(count, min_val, max_val, operation, symbol):
    """Generates and displays math problems based on the operation passed."""
    for _ in range(count):
        num1 = random.randint(min_val, max_val)
        num2 = random.randint(min_val, max_val)
        
        # Handle division by zero for division
        if symbol == '/' and num2 == 0:
            product = num1
            correct_answer = "undefined"
        else:
            product = num1 * num2 if symbol == '/' else None
            correct_answer = operation(num1, num2) if product is None else product // num2
        
        # Display the math problem
        problem = f"{product} {symbol} ({num2})" if num2 < 0 else f"{product if symbol == '/' else num1} {symbol} {num2}"
        input(f"{problem} = ")
        
        print(correct_answer)
        print()

def generate_square_cube(count, min_val, max_val, power):
    """Generates and displays problems for squares and cubes."""
    for _ in range(count):
        num1 = random.randint(min_val, max_val)
        correct_answer = num1 ** power
        input(f"{num1}^{power} = ")
        print(correct_answer)
        print()

def run_tests(count, min_val, max_val):
    """Run a series of arithmetic tests based on the provided range."""
    generate_problems(count, min_val, max_val, operator.add, '+')
    generate_problems(count, min_val, max_val, operator.sub, '-')
    generate_problems(count, min_val, max_val, operator.mul, '*')
    generate_problems(count, min_val, max_val, operator.floordiv, '/')
    generate_square_cube(count, min_val, max_val, 2)  # Squares
    generate_square_cube(count, min_val, max_val, 3)  # Cubes

def get_valid_input(prompt):
    """Prompts the user for an integer input and retries if invalid."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.\n")

def main():
    random.seed(time.time())
    
    print("MENTAL ARITHMETIC WITH SMALL INTEGERS\n***")
    ranges = [(0,9), (0, 12), (-9, 9), (-12, 12), (-15, 15)]
    
    for min_val, max_val in ranges:
        print(f"\nRANGE: [{min_val},{max_val}]\n***")
        count = get_valid_input("How many problems do you want to practice? ")
        input("Press ENTER to start\n")
        run_tests(count, min_val, max_val)
        print("\n*** Test Complete ***\n")

if __name__ == "__main__":
    main()
    