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
    'Knight':[120,140,6],
    'Warrior':[180,71,8],
    'Fairy':[71,100,16],
    'Robot':[160,120,11],
    'Giant':[160,200,4]
    }
  items = [[20,40,60,80,100],[30,60,90,120,150],[24,48,72,96,120]]
  mods = [2,1.5,8]
​
  player = characters[character]
  for i in range(3):
    player[i] += int(max([j for j in items[i] if j <= gold])/mods[i])
  return player

