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
  
  class Character:
    
    def __init__(self, ap, dp, sp, gold):
      self.ap = ap
      self.dp = dp
      self.sp = sp
      self.g = gold
    
    def buy(self, lst, typ):
      
      possibles = []
      pid = {}
      
      if typ == 'A':
        for item in lst:
          possibles.append(self.ap + item.p)
          pid[self.ap + item.p] = item.cost
          
      elif typ == 'D':
        for item in lst:
          possibles.append(self.dp + item.p)
          pid[self.dp + item.p] = item.cost
      
      elif typ == 'S':
        for item in lst:
          possibles.append(self.sp + item.p)
          pid[self.sp + item.p] = item.cost
      
      possibles = list(reversed(sorted(possibles)))
      
      for possible in possibles:
        price = pid[possible]
        if self.g - price >= 0:
          return possible
  
  class Item:
  
    def __init__(self, p, price):
      self.p = p
      self.cost = price
    
  #Create each character!
  knight = Character(120, 140, 6, gold)
  warrior = Character(180, 71, 8, gold)
  fairy = Character(71, 100, 16, gold)
  robot = Character(160, 120, 11, gold)
  giant = Character(160, 200, 4, gold)
  
  #Store each character!
  characters = {'Knight': knight, 'Warrior': warrior, 'Fairy': fairy, 'Robot': robot, 'Giant': giant}
  
  #Create each item!
  
  #Weapons
  simp_sword = Item(10, 20)
  katana = Item(20, 40)
  sharp_sword = Item(30, 60)
  great_sword = Item(40, 80)
  forg_sword = Item(50, 100)
  
  #Store by type!
  weapons = [simp_sword, katana, sharp_sword, great_sword, forg_sword]
  
  #Armour
  bronze = Item(20, 30)
  iron = Item(40, 60)
  steel = Item(60, 90)
  obsid = Item(80, 120)
  dragon = Item(100, 150)
  
  #Store by type!
  armour = [bronze, iron, steel, obsid, dragon]
  
  #Boots
  simple = Item(3, 24)
  leather = Item(6, 48)
  strong = Item(9, 72)
  compound = Item(12, 96)
  soft = Item(15, 120)
  
  #Store by type!
  boots = [simple, leather, strong, compound, soft]
  
  #Finds the correct character!
  cor_character = characters[character]
  
  #def buy(self, lst, typ):
  attck_points = cor_character.buy(weapons, 'A')
  defense_points = cor_character.buy(armour, 'D')
  speed_points = cor_character.buy(boots, 'S')
  
  return [attck_points, defense_points, speed_points]

