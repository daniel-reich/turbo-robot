"""


Create a function that flips M's to W's (all uppercase).

### Examples

    wumbo("I LOVE MAKING CHALLENGES") ➞ "I LOVE WAKING CHALLENGES"
    
    wumbo("MEET ME IN WARSAW") ➞ "WEET WE IN WARSAW"
    
    wumbo("WUMBOLOGY") ➞ "WUWBOLOGY"

### Notes

N/A

"""

def wumbo(words):
  for letter in words:
    if letter == "M":
      words = words.replace(letter,"W")
  return words

