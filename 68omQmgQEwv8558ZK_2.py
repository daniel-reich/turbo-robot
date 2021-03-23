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
    cha = {'Knight': (120, 140, 6), 'Warrior': (180, 71, 8), 'Fairy': (71, 100, 16), 'Robot': (160, 120, 11), 'Giant': (160, 200, 4)}
    wea = {'sis': (10, 20), 'kat': (20, 40), 'shs': (30, 60), 'grs': (40, 80), 'fos': (50, 100)}
    arm = {'bra': (20, 30), 'ira': (40, 60), 'sta': (60, 90), 'oba': (80, 120), 'dra': (100, 150)}
    boo = {'sib': (3, 24), 'lea': (6, 48), 'stb': (9, 72), 'cob': (12, 96), 'sob': (15, 120)}
    sta = tuple([i for i in cha[character]])
    max_wea = sorted([(wea[i][0], gold-wea[i][1]) for i in wea if gold-wea[i][1] >= 0], key = lambda x: x[1])[0][0]
    max_arm = sorted([(arm[i][0], gold-arm[i][1]) for i in arm if gold-arm[i][1] >= 0], key = lambda x: x[1])[0][0]
    max_boo = sorted([(boo[i][0], gold-boo[i][1]) for i in boo if gold-boo[i][1] >= 0], key = lambda x: x[1])[0][0]
    return [sta[0]+max_wea, sta[1]+max_arm, sta[2]+max_boo]

