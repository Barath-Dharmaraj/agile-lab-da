import random
import time
import sys

def roll_dice(sides=6):
    return random.randint(1, sides)

def main():
    print("--- ⚔️ Welcome to Dice Dungeon RPG ⚔️ ---")
    
    # Character Setup
    classes = {
        "1": {"name": "Warrior", "hp": 25, "die": 8, "ability": "Shield: Blocks 2 dmg"},
        "2": {"name": "Mage", "hp": 15, "die": 12, "ability": "Fireball: High dmg potential"}
    }
    
    print("\nSelect your class:")
    for key, val in classes.items():
        print(f"{key}. {val['name']} ({val['hp']} HP, D{val['die']} Dice)")
    
    choice = input("Choice (1 or 2): ")
    player = classes.get(choice, classes["1"])
    
    p_hp = player["hp"]
    m_hp = 20  # Monster HP
    
    print(f"\nA wild Goblin appears! (HP: {m_hp})")

    while p_hp > 0 and m_hp > 0:
        print(f"\nYour HP: {p_hp} | Goblin HP: {m_hp}")
        input("Press Enter to Attack!")
        
        # Player Turn
        p_attack = roll_dice(player["die"])
        print(f"You strike for {p_attack} damage!")
        m_hp -= p_attack
        
        if m_hp <= 0:
            print("✨ The Goblin has been defeated!")
            break
            
        # Monster Turn
        print("Goblin is attacking...")
        time.sleep(1)
        m_attack = roll_dice(6)
        
        # Apply Class Ability (Warrior Passive)
        if player["name"] == "Warrior":
            m_attack = max(0, m_attack - 2)
            print(f"🛡️ Your shield blocked some damage!")
            
        print(f"Goblin hits you for {m_attack} damage!")
        p_hp -= m_attack

    if p_hp > 0:
        print("\n🏆 Victory! You cleared the dungeon.")
    else:
        print("\n💀 You fell in battle... Game Over.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)

