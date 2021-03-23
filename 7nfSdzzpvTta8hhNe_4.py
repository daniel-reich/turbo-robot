"""


Write a function that maps a string into a dictionary of name, string, and
occupation pairs.

### Examples

    organize("Jameel Saeb, 15, CEO of facebook") ➞ {
      "name": "Jameel Saeb",
      "age": 15,
      "occupation": "CEO of facebook"
    }
    
    organize("John Mayer, 41, Singer, Emily Blunt, 36, Actor") ➞ {
      "name": "John Mayer",
      "age": 41,
      "occupation": "Singer"
    }
    
    organize("") ➞ {}

### Notes

  * Check **Resources** for more info.
  * Return an empty dictionary if given an empty string.

"""

def organize(txt):
  try: n,a,o = txt.split(',')
  except ValueError: return {}
  return {'name':n, 'age':int(a), 'occupation':o[1:]}

