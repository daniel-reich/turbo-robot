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

# Check the Resources tab for the list of characters and items.
def max_stats(character, gold):
    '''
    Returns a list of the attack power, defence and speed based on this
    character's starting values and the amount of gold input, based on the list
    of characters and items above.
    '''
    CHARACTERS = {
                  'Knight': (120, 140, 6),
                  'Warrior' : (180, 71, 8),
                  'Fairy' : (71, 100, 16),
                  'Robot' : (160, 120, 11),
                  'Giant' : (160, 200, 4)
                 } # Character and their innate attack, defence and speed powers
    
    WEAPONS = {
               'Simple Sword': (10, 20),
         'Katana': (20, 40),
         'Sharpened Sword': (30, 60),
         'Great Sword': (40, 80),
         'Forgotten Sword': (50, 100)
              }   # weapons and their attack strength, cost.
​
    ARMOUR = {
              'Bronze Armor': (20, 30),
        'Iron Armor': (40, 60),
        'Steel Armor': (60, 90),
        'Obsidian Armor': (80, 120),
        'Dragonhide Armor': (100, 150)
             }  # defensive armour and their defensive power, cost
​
    BOOTS = {
             'Simple Boots': (3, 24),
       'Leather Boots': (6, 48),
       'Strong Boots': (9, 72),
       'Compound Boots': (12, 96),
       'Soft Boots': (15, 120)
            }  # footwear and their speed and cost
​
    attack, defence, speed = CHARACTERS[character]
    starters = (attack, defence, speed)  # innate attack, defence, speed
    items = (WEAPONS, ARMOUR, BOOTS)
​
    return [starters[i] + max(items[i][item][0] for item in items[i] \
                              if items[i][item][1] <= gold) \
                              for i in range(len(starters))]

