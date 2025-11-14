# math game (optimized version)
import random

# Function to handle checking the answer and asking to play again
def check_answer_and_continue(correct_answer):
    """
    Prompts the user for their answer, checks it, and handles the 'Play again' loop.
    Returns True to continue the main game loop, False to break (quit).
    """
    try:
        user_answer = int(input("= "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return False # Quit on invalid input for simplicity

    if user_answer == correct_answer:
        print(f"The answer is {correct_answer}")
        print("Yes, you got it!")
        
        while True:
            print("\nPlay again")
            print("1. Yes")
            print("2. No")
            try:
                again = int(input("= "))
            except ValueError:
                print("Error: Invalid choice.")
                return False # Quit on invalid choice
                
            if again == 1:
                print("Ok")
                return True # Continue the main while loop
            elif again == 2:
                print("Thanks for playing!")
                return False # Break the main while loop
            else:
                print("Error: Invalid choice.")
                return False # Break the main while loop
    else:
        print("Try again!")
        # For 'try again', we return True to go back to the main menu
        return True

# Main Game Loop
while True:
    # Generate new random numbers for each new round
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    
    print("\n--- Math Quiz ---")
    print("1. Main")
    print("2. Quit")
    
    try:
        cois = int(input("= "))
    except ValueError:
        print("Invalid input. Please choose 1 or 2.")
        continue # Restart the loop for a valid choice

    if cois == 1:
        print("--Level--")
        print("1. Easy (Addition)")
        print("2. Medium (Multiplication)")
        print("3. Hard (Order of Operations)")
        print("4. Extreme (Powers and Division)")
        
        try:
            play = int(input("= "))
        except ValueError:
            print("Invalid input. Please choose 1-4.")
            continue

        should_continue = True # Assume we continue unless a level choice dictates otherwise
        
        if play == 1:
            print("\nLevel Easy")
            # Expression: x + y
            expression = f"{x} + {y}"
            correct_answer = x + y
            print(expression)
            should_continue = check_answer_and_continue(correct_answer)
            
        elif play == 2:
            print("\nLevel Medium")
            # Expression: x * y
            expression = f"{x} * {y}"
            correct_answer = x * y
            print(expression)
            should_continue = check_answer_and_continue(correct_answer)
            
        elif play == 3:
            print("\nLevel Hard")
            # Expression: (x + y) * x - y  (A mix of all basic operations)
            expression = f"({x} + {y}) * {x} - {y}"
            correct_answer = (x + y) * x - y
            print(expression)
            should_continue = check_answer_and_continue(correct_answer)
            
        elif play == 4:
            print("\nLevel Extreme")
            # Expression: x^2 + (y * x) // y - x  (Involves power and integer division)
            # Use // for integer division to ensure the final result is an integer
            expression = f"({x} * {x}) + ({y} * {x}) // {y} - {x}"
            correct_answer = (x * x) + (y * x) // y - x
            print(expression)
            should_continue = check_answer_and_continue(correct_answer)

        else:
            print("Invalid level choice.")
            continue # Go back to the main menu

        if not should_continue:
            break # Break the main loop if the function returns False
            
    elif cois == 2:
        print("Thanks for playing!")
        break
        
    else:
        print("Invalid choice. Please choose 1 or 2.")
