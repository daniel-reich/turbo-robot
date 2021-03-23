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
  att = {'Knight':120, 'Warrior':180, 'Fairy':71, 'Robot':160, 'Giant':160}
  dfn = {'Knight':140, 'Warrior':71, 'Fairy':100, 'Robot':120, 'Giant':200}
  spe = {'Knight':6, 'Warrior':8, 'Fairy':16, 'Robot':11, 'Giant':4}
  wea = {20:10, 40:20, 60:30, 80:40, 100:50}
  arm = {30:20, 60:40, 90:60, 120:80, 150:100}
  boo = {24:3, 48:6, 72:9, 96:12, 120:15}
  ans = [0,0,0]
  for i in wea:
    if gold >= i and wea[i]+att[character] > ans[0]:
      ans[0] = wea[i]+att[character]
  for i in arm:
    if gold >= i and arm[i]+dfn[character] > ans[1]:
      ans[1] = arm[i]+dfn[character]
  for i in boo:
    if gold >= i and boo[i]+spe[character] > ans[2]:
      ans[2] = boo[i]+spe[character]
  return ans

