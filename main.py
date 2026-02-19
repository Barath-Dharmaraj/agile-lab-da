import random
import sys

def roll_dice(sides):
    """Simulates rolling a die with a specific number of sides."""
    return random.randint(1, sides)

def main():
    print("--- Welcome to the Advanced Dice Simulator! ---")
    
    # Initialize session stats
    total_score = 0
    roll_count = 0
    
    # Allow user to choose dice type once, or default to 6
    try:
        sides_input = input("How many sides should the dice have? (Default is 6): ")
        sides = int(sides_input) if sides_input.strip() != "" else 6
        if sides < 1: raise ValueError
    except ValueError:
        print("Invalid input. Defaulting to 6-sided dice.")
        sides = 6

    while True:
        action = input(f"\n[Score: {total_score} | Rolls: {roll_count}] \nPress Enter to roll, or 'q' to quit: ").lower()
        
        if action == 'q':
            print(f"\nFinal Stats -> Total Score: {total_score} | Total Rolls: {roll_count}")
            print("Thanks for playing! Goodbye.")
            break
        elif action == '':
            # Roll two dice
            die1 = roll_dice(sides)
            die2 = roll_dice(sides)
            current_total = die1 + die2
            
            # Update stats
            total_score += current_total
            roll_count += 1
            
            print(f"Result: {die1} + {die2} = {current_total}")
            print("-" * 25)
        else:
            print("Invalid command. Please press Enter or 'q'.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGame closed. See you next time!")
        sys.exit(0)
