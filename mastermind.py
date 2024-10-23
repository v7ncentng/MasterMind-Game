import random

COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4

def generate_code():
    code = []
    
    for _ in range(CODE_LENGTH): # _ as placeholder; similar to i
        color = random.choice(COLORS)
        code.append(color)
        
    return code

def guess_code():
    
    while True:
        guess = input("Guess: ").upper().split(" ")
        
        if len(guess) != CODE_LENGTH:
            print(f"Please guess {CODE_LENGTH} colors.")
            continue
        
        for color in guess: 
            if color not in COLORS:
                print(f"Invalid color: {color}. Try again.")
                break
        else:
            break
    
    return guess

def check_code(guess, real_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0
    
    # Count colors in real_code
    for color in real_code:
        if color not in color_counts: 
            color_counts[color] = 0
        color_counts[color] += 1
        
    # First pass: Check for correct positions
    for i in range(CODE_LENGTH):
        if guess[i] == real_code[i]:
            correct_pos += 1
            color_counts[guess[i]] -= 1  # Decrease count for matched color
            
    # Second pass: Check for incorrect positions
    for i in range(CODE_LENGTH):
        if guess[i] != real_code[i] and color_counts.get(guess[i], 0) > 0:
            incorrect_pos += 1
            color_counts[guess[i]] -= 1  # Decrease count for matched color
            
    return correct_pos, incorrect_pos

def game():
    print(f"Welcome to mastermind, you have {TRIES} tries to guess the code...")
    print("The valid colors are", *COLORS)
    
    code = generate_code()
    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)
        
        if correct_pos == CODE_LENGTH:
            print(f"You guessed the code in {attempts} tries!")
            break
        
        print(f"Correct Positions: {correct_pos} || Incorrect Positions: {incorrect_pos}")
    
    else:
        print("You ran out of tries, the code was:", *code)
    
if __name__ == "__main__":
    game()
