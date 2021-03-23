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

def superheroes(h ):
  return sorted(s for s in h if not s.lower().endswith("woman") if s.endswith("man"))

