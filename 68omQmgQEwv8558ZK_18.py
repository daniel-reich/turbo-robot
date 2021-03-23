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
def check_stats(name):
  print("Challo")
  print(name)
  if name == "Knight":
    stats = [120, 140, 6]
  if name == "Warrior":
    stats = [180, 71, 8]
  if name == "Fairy":
    stats = [71, 100, 16]
  if name == "Robot":
    stats = [160, 120, 11]
  if name =="Giant":
    stats = [160, 200, 4]
  return stats
stats = []
weapons = [ [10, 20] , [20, 40] , [30, 60] , [40, 80] , [50,100] ]
armor = [ [20,30,] , [40,60] , [60,90] , [80, 120] , [100,150] ]
boots = [ [3,24] , [6,48] , [9,72] , [12,96] , [15,120] ]
def max_stats(character, gold):
  return_array = []
  stats = check_stats(character)
  print(character)
  print(stats)
  max_choice = 0;
  for choice in weapons:
    if choice[1] <= gold:
      max_choice = choice[0]
  return_array.append(stats[0]+max_choice)
  max_choice = 0;
  print(return_array)
  for choice in armor:
    if choice[1] <= gold:
      max_choice = choice[0]
  return_array.append(stats[1]+max_choice)
  max_choice = 0;
  print(return_array)
  for choice in boots:
    if choice[1] <= gold:
      max_choice = choice[0]
  return_array.append(stats[2]+max_choice)
  print(return_array)
  return return_array

