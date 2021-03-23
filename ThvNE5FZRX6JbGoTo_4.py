"""


Create a function that inverts words or the phrase depending on the value of
parameter `type`. A **"P"** means to invert the entire phrase, while a **"W"**
means to invert every word in the phrase. See the following examples for
clarity.

### Examples

    inverter("This is Valhalla", "P") ➞ "Valhalla is this"
    
    inverter("One fine day to start", "W") ➞ "Eno enif yad ot trats"
    
    inverter("Division by powers of two", "P") ➞ "Two of powers by division"

### Notes

  * The **first character** of the returned string should be in **uppercase** and the rest are in lowercase.
  * There will be no empty strings as inputs. Punctuation marks, though quite important for grammatical correctness, are discounted in the input phrases.

"""

def inverter(txt, type):
  txt = txt.lower().split()
  if type == 'W':
    ret = [i[::-1] for i in txt]
  else:
    ret = txt[::-1]
  return ' '.join([ret[0].capitalize()]+ret[1:])

