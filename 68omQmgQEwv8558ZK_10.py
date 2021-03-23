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
  lowest_prices_and_increments =  [ [20 , 10] , [30 , 20]  ,[24 , 3]];
  character_to_stats_dict = dict([["Knight" , [120 ,140,6]],
                             ["Warrior" , [180,71,8]],
                             ["Fairy" , [71,100,16]],
                             ["Robot" , [160,120,11]],
                             ["Giant" , [160 ,200,4]]]);
  charcter_stats =  character_to_stats_dict[character];
  return [charcter_stats[idx] + best_equip(gold , *lowest_prices_and_increments[idx] ) for idx in range(0 , len(charcter_stats))]
  
def best_equip(gold , lowest_price , smallest_increment):
  return min(gold//lowest_price , 5) * smallest_increment;

