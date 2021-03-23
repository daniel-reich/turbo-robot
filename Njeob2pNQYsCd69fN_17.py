"""


I'm trying to watch some lectures to study for my next exam but I keep getting
distracted by meme compilations, vine compilations, anime, and more on my
favorite video platform.

Your job is to help me create a function that takes a string and checks to see
if it contains the following words or phrases:

  * "anime"
  * "meme"
  * "vines"
  * "roasts"
  * "Danny DeVito"

If it does, return `"NO!"`. Otherwise, return `"Safe watching!"`.

### Examples

    prevent_distractions("vines that butter my eggroll") ➞ "NO!"
    
    prevent_distractions("Hot pictures of Danny DeVito") ➞ "NO!"
    
    prevent_distractions("How to ace BC Calculus in 5 Easy Steps") ➞ "Safe watching!"

### Notes

N/A

"""

def prevent_distractions(txt):
  u = 0
  x = txt.split(" ")
  y = ["anime","meme","vine","roasts","Danny","vines"]
  for i in x:
    for n in y:
      if i.lower() == n.lower():
        u += 1
  if int(u) > 0:
    return 'NO!'
  if int(u) == 0:
    return "Safe watching!"

