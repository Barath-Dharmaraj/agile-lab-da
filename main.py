import random
import time
import sys

def roll_dice():
    return random.randint(1, 6)

def main():
    print("--- ⚔️ Welcome to the Dice Battle! ⚔️ ---")
    player_wins = 0
    computer_wins = 0

    while True:
        print(f"\nScore -> You: {player_wins} | Computer: {computer_wins}")
        action = input("Press Enter to roll for your turn (or 'q' to quit): ").lower()
        
        if action == 'q':
            break
            
        # Player's Turn
        player_roll = roll_dice()
        print(f"🎲 You rolled a {player_roll}!")
        
        # Computer's Turn with suspense
        print("Computer is rolling...", end="", flush=True)
        for _ in range(3):
            time.sleep(0.5)
            print(".", end="", flush=True)
        
        comp_roll = roll_dice()
        print(f"\n🤖 Computer rolled a {comp_roll}!")
        
        # Determine Winner
        if player_roll > comp_roll:
            print("🎉 You win this round!")
            player_wins += 1
        elif comp_roll > player_roll:
            print("💀 Computer wins this round!")
            computer_wins += 1
        else:
            print("🤝 It's a tie!")
            
        print("-" * 30)

    print(f"\nFinal Result -> You: {player_wins} | Computer: {computer_wins}")
    print("Thanks for playing!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
