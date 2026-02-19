import random
import sys
import time

# ASCII representation of dice faces
DICE_ART = {
    1: ("┌─────────┐", "│         │", "│    ●    │", "│         │", "└─────────┘"),
    2: ("┌─────────┐", "│  ●      │", "│         │", "│      ●  │", "└─────────┘"),
    3: ("┌─────────┐", "│  ●      │", "│    ●    │", "│      ●  │", "└─────────┘"),
    4: ("┌─────────┐", "│  ●   ●  │", "│         │", "│  ●   ●  │", "└─────────┘"),
    5: ("┌─────────┐", "│  ●   ●  │", "│    ●    │", "│  ●   ●  │", "└─────────┘"),
    6: ("┌─────────┐", "│  ●   ●  │", "│  ●   ●  │", "│  ●   ●  │", "└─────────┘")
}

def display_dice(d1, d2):
    """Prints two dice side-by-side using ASCII art."""
    for i in range(5):
        print(f"{DICE_ART[d1][i]}   {DICE_ART[d2][i]}")

def roll_dice():
    return random.randint(1, 6)

def main():
    print("=== Welcome to Visual Dice! ===")
    score = 0
    
    while True:
        action = input(f"\n[Total Score: {score}] Press Enter to roll (q to quit): ").lower()
        if action == 'q': break
        
        print("Rolling...")
        time.sleep(0.5) # Adds a small delay for suspense
        
        die1, die2 = roll_dice(), roll_dice()
        display_dice(die1, die2)
        
        current_total = die1 + die2
        score += current_total
        print(f"You rolled a total of {current_total}!")

        # Double Bonus Logic
        if die1 == die2:
            print("✨ DOUBLE BONUS! You rolled a pair. Have a free extra roll!")
            # The loop continues immediately without asking for input again
            bonus = roll_dice()
            print(f"Bonus roll: {bonus}")
            score += bonus

    print(f"\nFinal Score: {score}. Thanks for playing!")

if __name__ == "__main__":
    main()
