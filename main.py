import random
import time
import json
import os

# --- FILE UTILITIES ---
SAVE_FILE = "savegame.json"
LEADERBOARD_FILE = "leaderboard.txt"

def save_game(data):
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f)
    print("💾 Game saved successfully!")

def load_game():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            return json.load(f)
    return None

def update_leaderboard(name, level):
    with open(LEADERBOARD_FILE, "a") as f:
        f.write(f"{name}:{level}\n")

def show_leaderboard():
    if not os.path.exists(LEADERBOARD_FILE):
        print("\n🏆 No records yet!")
        return
    
    print("\n--- 🏆 ALL-TIME HALL OF FAME 🏆 ---")
    scores = []
    with open(LEADERBOARD_FILE, "r") as f:
        for line in f:
            parts = line.strip().split(":")
            if len(parts) == 2:
                scores.append((parts[0], int(parts[1])))
    
    # Sort by level descending
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    for i, (name, lvl) in enumerate(sorted_scores[:5], 1):
        print(f"{i}. {name} - Level {lvl}")

# --- GAME LOGIC ---
def main():
    print("--- ⚔️ Welcome back to Dice Roguelike v8.0 ⚔️ ---")
    
    # Try loading existing character
    saved_data = load_game()
    if saved_data:
        confirm = input(f"Found {saved_data['name']} (LVL {saved_data['level']}). Resume? (y/n): ")
        if confirm.lower() == 'y':
            p = saved_data
        else:
            p = None
    else:
        p = None

    # Create new character if no load
    if not p:
        name = input("Enter your hero's name: ")
        p = {"name": name, "hp": 30, "max_hp": 30, "gold": 10, "level": 1, "xp": 0}

    while p["hp"] > 0:
        print(f"\n[{p['name']} | LVL {p['level']} | HP {p['hp']}/{p['max_hp']} | Gold: {p['gold']}]")
        choice = input("1: Battle, 2: Save & Quit, 3: Hall of Fame: ")

        if choice == '2':
            save_game(p)
            break
        
        if choice == '3':
            show_leaderboard()
            continue

        if choice == '1':
            m_hp = 10 + (p["level"] * 5)
            print(f"\nA Monster appears! (HP: {m_hp})")
            
            while m_hp > 0 and p["hp"] > 0:
                p_dmg = random.randint(1, 6)
                m_hp -= p_dmg
                print(f"You deal {p_dmg} damage!")
                
                if m_hp > 0:
                    m_dmg = random.randint(1, 4)
                    p["hp"] -= m_dmg
                    print(f"Monster deals {m_dmg} damage!")
                    time.sleep(0.4)

            if p["hp"] > 0:
                p["gold"] += 15
                p["xp"] += 25
                print("Victory!")
                if p["xp"] >= 50:
                    p["level"] += 1
                    p["xp"] = 0
                    p["max_hp"] += 10
                    p["hp"] = p["max_hp"]
                    print(f"⭐ Level Up! You are now Level {p['level']}")

    if p["hp"] <= 0:
        print(f"\n💀 {p['name']} has fallen.")
        update_leaderboard(p["name"], p["level"])
        if os.path.exists(SAVE_FILE):
            os.remove(SAVE_FILE) # Permadeath!
        show_leaderboard()

if __name__ == "__main__":
    main()
