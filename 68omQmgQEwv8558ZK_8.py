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
def max_stats(character,gold):
  if character=="Knight":
      attack,defense,speed=120,140,6
​
  elif character=="Warrior":
      attack,defense,speed=180,71,8
​
  elif character=="Fairy":
      attack,defense,speed=71,100,16
​
  elif character=="Robot":
      attack,defense,speed=160,120,11
​
  elif character=="Giant":
      attack,defense,speed=160,200,4
      
  if 20<=gold<24:
      attack+=10
  elif 24<=gold<30:
      attack+=10
      speed+=3
  elif 30<=gold<40:
      attack+=10
      speed+=3
      defense+=20
  elif 40<=gold<48:
      attack+=20
      speed+=3
      defense+=20
  elif 48<=gold<60:
      attack+=20
      speed+=6
      defense+=20
  elif 60<=gold<72:
      attack+=30
      speed+=6
      defense+=40
  elif 72<=gold<80:
      attack+=30
      speed+=9
      defense+=40
  elif 80<=gold<90:
      attack+=40
      speed+=9
      defense+=40
  elif 90<=gold<96:
      attack+=40
      speed+=9
      defense+=60
  elif 96<=gold<100:
      attack+=40
      speed+=12
      defense+=60        
  elif 100<=gold<120:
      attack+=50
      speed+=12
      defense+=60
  elif 120<=gold<150:
      attack+=50
      speed+=15
      defense+=80
  elif gold>=150:
      attack+=50
      speed+=15
      defense+=100
​
  return [attack,defense,speed]

