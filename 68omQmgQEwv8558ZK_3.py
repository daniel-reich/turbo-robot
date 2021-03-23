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

#Look at the Resources tab for the list of characters and items.
def max_stats(character, gold):
  charatk = {"Knight" : 120, "Warrior" : 180, "Fairy" : 71, "Robot" : 160, "Giant" : 160}
  chardef = {"Knight" : 140, "Warrior" : 71, "Fairy" : 100, "Robot" : 120, "Giant" : 200}
  charspd = {"Knight" : 6, "Warrior" : 8, "Fairy" : 16, "Robot" : 11, "Giant" : 4}
  array = [gold // 20 * 10 + charatk[character], gold // 30 * 20 + chardef[character], gold // 24 * 3 + charspd[character]]
  if gold // 20 * 10 > 50:
    array[0] = 50 + charatk[character]
  if gold // 30 * 20 > 100:
    array[1] = 100 + chardef[character]
  if gold // 24 * 3 > 15:
    array[2] = 15 + charspd[character]
  return array

