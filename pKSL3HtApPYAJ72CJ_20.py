"""


Create a function that takes a string (will be a person's first and last name)
and returns a string with the first and last name swapped.

### Examples

    name_shuffle("Donald Trump") ➞ "Trump Donald"
    
    name_shuffle("Rosie O'Donnell") ➞ "O'Donnell Rosie"
    
    name_shuffle("Seymour Butts") ➞ "Butts Seymour"

### Notes

  * There will be exactly one space between the first and last name.
  * If you get stuck on a challenge, find help in the **Resources** tab.
  * If you're _really_ stuck, unlock solutions in the **Solutions** tab.

"""

def name_shuffle(txt):
  l=txt.split(" ")
  return l[1]+" "+l[0]

