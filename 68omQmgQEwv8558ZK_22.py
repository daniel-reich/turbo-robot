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
  Weapons = [20, 40, 60 ,80 , 100]
  Armor = [30, 60, 90, 120, 150]
  Boots = [24, 48, 72, 96, 120]
​
  if character=="Knight":
​
    x1 = [
      Weapons[i] / 2 + 120 if Weapons[i] <= gold and Weapons[i + 1] > gold else Weapons[-1] / 2 + 120 if Weapons[
                                                           -1] <= gold else 0
      for i in range(4)]
    x1 += [x1.remove(0) if 0 in x1 else 0 for i in range(len(x1) - 1)]
​
    x2 = [Armor[i] * 2 / 3 + 140 if Armor[i] <= gold and Armor[i + 1] > gold else Armor[-1] * 2 / 3 + 140 if Armor[
                                                           -1] <= gold else 0
        for i in range(4)]
    x2 += [x2.remove(0) if 0 in x2 else 0 for i in range(len(x2) - 1)]
​
    x3 = [Boots[i] / 8 + 6 if Boots[i] <= gold and Boots[i + 1] > gold else Boots[-1] / 8 + 6 if Boots[
                                                       -1] <= gold else 0
        for i in range(4)]
    x3 += [x3.remove(0) if 0 in x3 else 0 for i in range(len(x3) - 1)]
​
    return [x1[0], x2[0], x3[0]]
​
  elif character=="Warrior":
​
    x1 = [
      Weapons[i] / 2 + 180 if Weapons[i] <= gold and Weapons[i + 1] > gold else Weapons[-1] / 2 + 180 if Weapons[
                                                           -1] <= gold else 0
      for i in range(4)]
    x1 += [x1.remove(0) if 0 in x1 else 0 for i in range(len(x1) - 1)]
​
    x2 = [Armor[i] * 2 / 3 + 71 if Armor[i] <= gold and Armor[i + 1] > gold else Armor[-1] * 2 / 3 + 71 if Armor[
                                                           -1] <= gold else 0
        for i in range(4)]
    x2 += [x2.remove(0) if 0 in x2 else 0 for i in range(len(x2) - 1)]
​
    x3 = [Boots[i] / 8 + 8 if Boots[i] <= gold and Boots[i + 1] > gold else Boots[-1] / 8 + 8 if Boots[
                                                       -1] <= gold else 0
        for i in range(4)]
    x3 += [x3.remove(0) if 0 in x3 else 0 for i in range(len(x3) - 1)]
​
    return [x1[0], x2[0], x3[0]]
​
  elif character=="Fairy":
​
    x1 = [
      Weapons[i] / 2 + 71 if Weapons[i] <= gold and Weapons[i + 1] > gold else Weapons[-1] / 2 + 71 if Weapons[
                                                           -1] <= gold else 0
      for i in range(4)]
    x1 += [x1.remove(0) if 0 in x1 else 0 for i in range(len(x1) - 1)]
​
    x2 = [Armor[i] * 2 / 3 + 100 if Armor[i] <= gold and Armor[i + 1] > gold else Armor[-1] * 2 / 3 + 100 if Armor[
                                                           -1] <= gold else 0
        for i in range(4)]
    x2 += [x2.remove(0) if 0 in x2 else 0 for i in range(len(x2) - 1)]
​
    x3 = [Boots[i] / 8 + 16 if Boots[i] <= gold and Boots[i + 1] > gold else Boots[-1] / 8 + 16 if Boots[
                                                       -1] <= gold else 0
        for i in range(4)]
    x3 += [x3.remove(0) if 0 in x3 else 0 for i in range(len(x3) - 1)]
​
    return [x1[0], x2[0], x3[0]]
​
  elif character=="Robot":
​
    x1 = [
      Weapons[i] / 2 + 160 if Weapons[i] <= gold and Weapons[i + 1] > gold else Weapons[-1] / 2 + 160 if Weapons[
                                                           -1] <= gold else 0
      for i in range(4)]
    x1 += [x1.remove(0) if 0 in x1 else 0 for i in range(len(x1) - 1)]
​
    x2 = [Armor[i] * 2 / 3 + 120 if Armor[i] <= gold and Armor[i + 1] > gold else Armor[-1] * 2 / 3 + 120 if Armor[
                                                           -1] <= gold else 0
        for i in range(4)]
    x2 += [x2.remove(0) if 0 in x2 else 0 for i in range(len(x2) - 1)]
​
    x3 = [Boots[i] / 8 + 11 if Boots[i] <= gold and Boots[i + 1] > gold else Boots[-1] / 8 + 11 if Boots[
                                                       -1] <= gold else 0
        for i in range(4)]
    x3 += [x3.remove(0) if 0 in x3 else 0 for i in range(len(x3) - 1)]
​
    return [x1[0], x2[0], x3[0]]
​
  elif character=="Giant":
​
    x1 = [
      Weapons[i] / 2 + 160 if Weapons[i] <= gold and Weapons[i + 1] > gold else Weapons[-1] / 2 + 160 if Weapons[
                                                           -1] <= gold else 0
      for i in range(4)]
    x1 += [x1.remove(0) if 0 in x1 else 0 for i in range(len(x1) - 1)]
​
    x2 = [Armor[i] * 2 / 3 + 200 if Armor[i] <= gold and Armor[i + 1] > gold else Armor[-1] * 2 / 3 + 200 if Armor[
                                                           -1] <= gold else 0
        for i in range(4)]
    x2 += [x2.remove(0) if 0 in x2 else 0 for i in range(len(x2) - 1)]
​
    x3 = [Boots[i] / 8 + 4 if Boots[i] <= gold and Boots[i + 1] > gold else Boots[-1] / 8 + 4 if Boots[
                                                       -1] <= gold else 0
        for i in range(4)]
    x3 += [x3.remove(0) if 0 in x3 else 0 for i in range(len(x3) - 1)]
​
    return [x1[0], x2[0], x3[0]]

