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
  
  if (txt == ""):
    return {}
  
  Dictionary = {}
  
  Sample = str(txt)
  Sample = Sample.replace(", ",",")
  Blocks = Sample.split(",")
  
  Key1 = "name"
  Value1 = Blocks[0]
  Dictionary[Key1] = Value1
  
  Key2 = "age"
  Value2 = int(Blocks[1])
  Dictionary[Key2] = Value2
  
  Key3 = "occupation"
  Value3 = Blocks[2]
  Dictionary[Key3] = Value3
  
  return Dictionary

