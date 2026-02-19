import random
import time
import sys

def roll_dice(sides=6):
    return random.randint(1, sides)

def main():
    print("--- 🛡️ Welcome to Dice Roguelike v7.0 🛡️ ---")
    
    # Player Stats
    p_hp = 30
    p_max_hp = 30
    gold = 10
    level = 1
    xp = 0
    inventory = {"Health Potion": 1}

    # Shop Items
    shop_items = {
        "1": {"name": "Health Potion", "cost": 15, "desc": "Heals 15 HP"},
        "2": {"name": "Sharp Whetstone", "cost": 30, "desc": "+2 to all attack rolls (Permanent)"}
    }
    attack_bonus = 0

    while p_hp > 0:
        print(f"\n[LVL {level} | HP {p_hp}/{p_max_hp} | Gold: {gold} | XP: {xp}/50]")
        choice = input("What will you do? (1: Battle, 2: Shop, 3: Inventory, q: Quit): ")

        if choice == 'q': break

        # --- SHOP SYSTEM ---
        if choice == '2':
            print("\n--- 💰 THE TRAVELING MERCHANT 💰 ---")
            for k, v in shop_items.items():
                print(f"{k}. {v['name']} - {v['cost']} Gold ({v['desc']})")
            buy = input("Buy something? (Number or 'n' to leave): ")
            if buy in shop_items:
                item = shop_items[buy]
                if gold >= item['cost']:
                    gold -= item['cost']
                    if buy == "1": inventory["Health Potion"] += 1
                    if buy == "2": attack_bonus += 2
                    print(f"Purchased {item['name']}!")
                else:
                    print("You can't afford that!")
            continue

        # --- INVENTORY SYSTEM ---
        if choice == '3':
            print(f"\nYour Items: {inventory}")
            use = input("Use Health Potion? (y/n): ")
            if use == 'y' and inventory["Health Potion"] > 0:
                p_hp = min(p_max_hp, p_hp + 15)
                inventory["Health Potion"] -= 1
                print(f"Healed! Current HP: {p_hp}")
            continue

        # --- COMBAT & LEVELING ---
        if choice == '1':
            m_hp = 10 + (level * 5)
            print(f"\nA Level {level} Monster blocks your path! (HP: {m_hp})")
            
            while m_hp > 0 and p_hp > 0:
                p_dmg = roll_dice(6) + attack_bonus
                m_hp -= p_dmg
                print(f"You hit for {p_dmg}!")
                
                if m_hp > 0:
                    m_dmg = roll_dice(4) + (level // 2)
                    p_hp -= m_dmg
                    print(f"Monster hits for {m_dmg}!")
                    time.sleep(0.5)

            if p_hp > 0:
                reward = random.randint(10, 25)
                gold += reward
                xp += 25
                print(f"Victory! Gained {reward} Gold and 25 XP.")
                
                # Level Up logic
                if xp >= 50:
                    level += 1
                    xp = 0
                    p_max_hp += 10
                    p_hp = p_max_hp
                    print(f"⭐ LEVEL UP! You are now Level {level}. HP fully restored.")

    print("\nGame Over. You reached Level", level)

if __name__ == "__main__":
    main()
