"""


Create a function that takes a list of names of superheroes and superheroines
and returns a list of only the names of superheroes ending in _"man"_ in
alphabetical order.

### Examples

    superheroes(["Batman", "Superman", "Spider-man", "Hulk", "Wolverine", "Wonder-Woman"])
    ➞ ["Batman", "Spider-man", "Superman"]
    
    superheroes(["Catwoman", "Deadpool", "Dr.Strange", "Captain-America", "Aquaman", "Hawkeye"])
    ➞ ["Aquaman"]
    
    superheroes(["Wonder-Woman", "Catwoman", "Invisible-Woman"])
    ➞ []

### Notes

Wonder-Woman, Catwoman and Invisible-Woman are superheroines.

"""

def superheroes(heroes):
  man = [x for x in heroes if x.lower().endswith('man')]
  only = [x for x in man if not x.lower().endswith('woman')]
  return sorted(only)

