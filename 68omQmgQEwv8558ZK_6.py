"""


You were bored, so you decided to try out a new game you recently downloaded.
There are five types of characters, each with their own level of attack power,
defense, and speed. There are also five types of armor, weapons, and boots.
Each type of item has a different cost of gold and a different level of attack
power, defense or speed.

Create a function that takes the type of character and the amount of gold. The
function should return the maximum amount of attack power possible, the
maximum amount of defense possible, and the maximum speed possible in a list,
in that order.

### Examples

    max_stats("Robot", 160) ➞ [210, 220, 26]
    
    max_stats("Fairy", 50) ➞ [91, 120, 22]
    
    max_stats("Warrior", 70) ➞ [210, 211, 14]

### Notes

  * Calculate the attack power, defense, and speed seperately. Do not calculate combinations of items.
  * Check the **Resources** tab for the list of characters and items.
  *  **Hint:** Add the character's stats to the items' stats for the result.

"""

def max_stats(character, gold):
    characters = {
        'Knight' : [120, 140, 6],
        'Warrior' : [180, 71, 8],
        'Fairy' : [71, 100, 16],
        'Robot' : [160, 120, 11],
        'Giant' : [160, 200, 4]
    }
    weapons = {
        'Simple Sword': [10, 20],
        'Katana': [20, 40],
        'Sharpened Sword': [30, 60],
        'Great Sword': [40, 80],
        'Forgotten Sword': [50, 100]
    }
    armor = {
        'Bronze Armor': [20, 30],
        'Iron Armor': [40, 60],
        'Steel Armor': [60, 90],
        'Obsidian Armor': [80, 120],
        'Dragonhide Armor': [100, 150]
    }
    boots = {
        'Simple Boots': [3, 24],
        'Leather Boots': [6, 48],
        'Strong Boots': [9, 72],
        'Compound Boots': [12, 96],
        'Soft Boots': [15, 120]
    }
    add_attack =  [i[0] for i in weapons.values() if i[1]==max([i[1] for i in weapons.values() if i[1] <= gold])]
    add_defense = [i[0] for i in armor.values() if i[1]==max([i[1] for i in armor.values() if i[1] <= gold])]
    add_speed = [i[0] for i in boots.values() if i[1]==max([i[1] for i in boots.values() if i[1] <= gold])]
    return [
    characters[character][0] + add_attack[0],
    characters[character][1] + add_defense[0],
    characters[character][2] + add_speed[0]
    ]

