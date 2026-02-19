import random
import time
import sys

# ASCII Art for quick visual feedback
DICE_FACES = {
    1: "[  .  ]", 2: "[ . . ]", 3: "[. . .]",
    4: "[: : ]", 5: "[: . :]", 6: "[: : :]"
}

def roll_dice():
    return random.randint(1, 6)

def main():
    wallet = 100  # Starting balance
    print("--- 🎰 Welcome to the Python High-Stakes Casino! 🎰 ---")
    print(f"You're starting with ${wallet} in virtual chips.")

    while wallet > 0:
        print(f"\n💰 Current Wallet: ${wallet}")
        action = input("Enter bet amount (or 'q' to cash out): ").lower()
        
        if action == 'q':
            break
        
        try:
            bet = int(action)
            if bet > wallet or bet <= 0:
                print("❌ Invalid bet! You can't bet more than you have.")
                continue
        except ValueError:
            print("❌ Please enter a valid number or 'q'.")
            continue

        # Player Rolls
        print("\nRolling for you...")
        time.sleep(0.7)
        p1, p2 = roll_dice(), roll_dice()
        player_total = p1 + p2
        print(f"You: {DICE_FACES[p1]} {DICE_FACES[p2]} -> Total: {player_total}")

        # Computer Rolls
        print("Dealer is rolling...")
        time.sleep(1)
        d1, d2 = roll_dice(), roll_dice()
        dealer_total = d1 + d2
        print(f"Dealer: {DICE_FACES[d1]} {DICE_FACES[d2]} -> Total: {dealer_total}")

        # Result Logic
        if player_total > dealer_total:
            win_amount = bet
            wallet += win_amount
            print(f"🎉 WIN! You gained ${win_amount}.")
            
            # Double or Nothing feature
            choice = input("🔥 Double or Nothing? (y/n): ").lower()
            if choice == 'y':
                print("Risking it all on one roll...")
                time.sleep(1)
                if roll_dice() > 3:
                    wallet += win_amount
                    print(f"✅ SUCCESS! You doubled your win to ${win_amount * 2}!")
                else:
                    wallet -= (win_amount * 2)
                    print(f"💀 BUST! You lost your winnings and the bet.")
        elif player_total < dealer_total:
            wallet -= bet
            print(f"💸 LOSS! You lost ${bet}.")
        else:
            print("🤝 TIE! Your bet is returned.")

    if wallet <= 0:
        print("\n💥 You're broke! Game over.")
    else:
        print(f"\nFinal Cash Out: ${wallet}. See you at the tables!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
