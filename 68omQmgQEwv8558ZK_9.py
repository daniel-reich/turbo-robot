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
  stats = {'K': [120, 140, 6], 'W': [180, 71, 8], 
       'F': [71, 100, 16], 'R': [160, 120, 11], 
       'G': [160, 200, 4]}[character[0]]
       
  weapon = next(i for i in [50, 40, 30, 20, 10, 0] if i*2 <= gold)
  armor = next(i for i in [100, 80, 60, 40, 20, 0] if i*1.5 <= gold)
  boots = next(i for i in [15, 12, 9, 6, 3, 0] if i*8 <= gold)
  
  return [a+b for a, b in zip(stats, [weapon, armor, boots])]

