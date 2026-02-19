import random
import sys
def roll_dice(sides=6):
    return random.randint(1, sides) #
def get_user_input():
    while True:
        user_input = input("\nPress Enter to roll the dice, or type 'q' to quit: ") #
        if user_input.lower() == 'q':
            return 'quit'
        elif user_input == '':
            return 'roll'
        else:
            print("Invalid input. Please press Enter or type 'q'.")
def main():
    print("Welcome to the Roll the Dice Game!")
    while True:
        action = get_user_input()      
        if action == 'quit':
            print("Thanks for playing! Goodbye.")
            break     
        die1 = roll_dice() #
        die2 = roll_dice() #
        total = die1 + die2   
        print(f"\nYou rolled a {die1} and a {die2}. Total: {total}") #
        print("-" * 20) 
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGame interrupted. Goodbye.")
        sys.exit(0)

