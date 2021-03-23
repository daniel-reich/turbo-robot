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

def buy_best(gold):
    weapons = ((100, 50), (80, 40), (60, 30), (40, 20), (20, 10))
    armour = ((150, 100), (120, 80), (90, 60), (60, 40), (30, 20))
    boots = ((120, 15), (96, 12), (72, 9), (48, 6), (24, 3))
  
    boosts = []
    for shop in (weapons, armour, boots):
        for cost, boost in shop:
            if cost <= gold:
                boosts.append(boost)
                break
    return boosts
        
​
def max_stats(character, gold): 
    base = {'Knight': [120, 140, 6], 'Warrior': [180, 71, 8], 
            'Fairy': [71, 100, 16], 'Robot': [160, 120, 11], 
            'Giant': [160, 200, 4]}
    
    return [sum(i) for i in zip(base[character], buy_best(gold))]

