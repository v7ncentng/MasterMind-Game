import random

# Constants for colors, # of tries, and code length
COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4

def generate_code():
    """
    Generate a random code consisting of colors.
    The code is a list of colors of length CODE_LENGTH.
    """
    code = []
    
    for _ in range(CODE_LENGTH):  # Repeat CODE_LENGTH times to generate code
        color = random.choice(COLORS)  # Randomly choose a color from COLORS
        code.append(color)  # Add the chosen color to the code list
        
    return code

def guess_code():
    """
    Prompt the user to guess a code. The guess is validated for length and color validity.
    Returns the valid guess as a list of colors.
    """
    while True:
        guess = input("Guess: ").upper().split(" ")  # Get user input, convert to uppercase, and split into a list
        
        if len(guess) != CODE_LENGTH:
            print(f"Please guess {CODE_LENGTH} colors.")  # Validate the length of the guess
            continue
        
        for color in guess: 
            if color not in COLORS:
                print(f"Invalid color: {color}. Try again.")  # Validate the colors in the guess
                break
        else:
            # If no invalid color was found, exit the loop
            break
    
    return guess

def check_code(guess, real_code):
    """
    Check the user's guess against the actual code.
    Returns the number of colors in the correct position and the number of correct colors in incorrect positions.
    """
    color_counts = {}  # Dictionary to keep track of color counts in the actual code
    correct_pos = 0  # Number of colors in the correct position
    incorrect_pos = 0  # Number of correct colors in incorrect positions
    
    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0  # Initialize the color count if not already present
        color_counts[color] += 1  # Count occurrences of each color in the actual code
        
    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1  # Increment count for correct color in correct position
            color_counts[guess_color] -= 1  # Decrease the count of this color
        
    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1  # Increment count for correct color in incorrect position
            color_counts[guess_color] -= 1  # Decrease the count of this color
    
    return correct_pos, incorrect_pos

def game():
    """
    Main function to run the Mastermind game.
    """
    print(f"Welcome to Mastermind, you have {TRIES} tries to guess the code...")
    print("The valid colors are", *COLORS)
    
    code = generate_code()  # Generate a random code
    for attempts in range(1, TRIES + 1):
        guess = guess_code()  # Prompt the user for a guess
        correct_pos, incorrect_pos = check_code(guess, code)  # Check the guess against the actual code
        
        if correct_pos == CODE_LENGTH:
            print(f"You guessed the code in {attempts} tries!") 
            break
        
        print(f"Correct Positions: {correct_pos} || Incorrect Positions: {incorrect_pos}")
    
    else:
        # If our loop completes without breaking user ran out of tries
        print("You ran out of tries, the code was:", *code)
    
if __name__ == "__main__":
    game() 
