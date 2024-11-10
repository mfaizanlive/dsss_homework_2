import random

def generate_random_integer(min_value, max_value):
    """
    Generate a random integer within a specified range.

    Args:
        min_value (int): Minimum value of the range.
        max_value (int): Maximum value of the range.

    Returns:
        int: Random integer within the given range.
    """
    return random.randint(min_value, max_value)

def get_random_operator():
    """
    Select a random operator from ('+', '-', '*').

    Returns:
        str: Chosen operator.
    """
    return random.choice(['+', '-', '*'])

def create_math_problem(first_number, second_number, operator):
    """
    Formulate a math problem and determine the correct answer.

    Args:
        first_number (int): First operand.
        second_number (int): Second operand.
        operator (str): Arithmetic operator.

    Returns:
        tuple: Problem as string and correct answer.
    """
    problem_statement = f"{first_number} {operator} {second_number}"
    
    # Calculate the answer based on the operator used
    if operator == '+':
        correct_answer = first_number + second_number
    elif operator == '-':
        correct_answer = first_number - second_number
    else:
        correct_answer = first_number * second_number
    
    return problem_statement, correct_answer

def math_quiz():
    """
    Run the math quiz game with randomly generated questions.
    """
    score = 0  # Track the user's score
    total_questions = 3  # Total number of questions in the quiz

    print("Welcome to the Math Quiz Game!")
    print("Answer the math problems to earn points.")

    for _ in range(total_questions):
        # Generate random numbers and an operator
        first_number = generate_random_integer(1, 10)
        second_number = generate_random_integer(1, 5)
        operator = get_random_operator()

        # Create problem and get the correct answer
        problem_statement, correct_answer = create_math_problem(first_number, second_number, operator)
        print(f"\nQuestion: {problem_statement}")

        try:
            # Get user input and check if it's correct
            user_answer = int(input("Your answer: "))
            if user_answer == correct_answer:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {correct_answer}.")
        except ValueError:
            print("Invalid input! Please enter an integer.")

    # Display the final score after the game ends
    print(f"\nGame over! Your score is: {score}/{total_questions}")

# Start the game if this script is executed directly
if __name__ == "__main__":
    math_quiz()
