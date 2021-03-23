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
  return {'name':txt.split(',')[0],'age':int(txt.split(',')[1]),'occupation':txt.split(',')[2].strip()} if len(txt) > 0 else {}

