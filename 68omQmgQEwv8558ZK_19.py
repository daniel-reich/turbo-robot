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
    myans =[0,0,0]
    c = [['Knight',120,140,6],['Warrior',180,71,8],['Fairy',71,100,16],['Robot',160,120,11],['Giant',160,200,4]]
    w = [['Simple Sword',10,20],['Katana',20,40],['Sharpened Sword',30,60],['Great Sword',40,80],['Forgotten Sword',50,100]]
    a = [['Bronze Armor',20,30],['Iron Armor',40,60],['Steel Armor',60,90],['Obsidian Armor',80,120],['Dragonhide Armor',100,150]]
    b = [['Simple Boots',3,24],['Leather Boots',6,48],['Strong Boots',9,72],['Compound Boots',12,96],['Soft Boots',15,120]]
​
    for i in range(len(c)):
        if c[i][0] == character:
            myans[0] = c[i][1]
            myans[1] = c[i][2]
            myans[2] = c[i][3]
    for i in range(len(w)-1,-1,-1):
        if w[i][2] <= gold:
            myans[0] += w[i][1]
            break
    for i in range(len(a)-1,-1,-1):
        if a[i][2] <= gold:
            myans[1] += a[i][1]
            break
    for i in range(len(b)-1,-1,-1):
        if b[i][2] <= gold:
            myans[2] += b[i][1]
            break
    return myans

