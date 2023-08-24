import random

def generate_random_number(): # generate a random number for the game
    return random.randint(1000, 9999)

def get_user_guess():
    while True:
        guess = input("Enter a 4-digit number or 'q' to quit: ") # require player in put a 4-digit number or 'q'
        if guess.lower() == 'q':
            return None
        if len(guess) != 4 or not guess.isdigit(): # if the input is not a number or a 4 digital number, it's invalid input 
            print("Invalid input.")
        else:
            return guess

def compare_numbers(secret_number, user_guess): # compare the random number and the number from player
    O_count = 0
    x_count = 0

    for i in range(4):
        if user_guess[i] == secret_number[i]: # if number and position is correct, represent O
            O_count += 1
        elif user_guess[i] in secret_number: # if only number is correct, represent X
            x_count += 1

    return O_count, x_count

def main():
    play_again = True 

    while play_again:
        secret_number = str(generate_random_number())
        play_times = 0

        while True:
            user_guess = get_user_guess()
            if user_guess is None: # if the input is 'q', break the program
                break
            
            play_times += 1
            O_count, x_count = compare_numbers(secret_number, user_guess)

            print(f"Hints: {'O' * O_count} {'X' * x_count}")

            if O_count == 4:
                print(f"You've guessed the number {secret_number} in {play_times} play times.")
                break

        play_again_input = input("play again? (yes/no): ")
        play_again = play_again_input.lower() == 'yes'

    print("game finish")

if __name__ == "__main__":
    main()