"""


Luke Skywalker has family and friends. Help him remind them who is who. Given
a string with a name, return the relation of that person to Luke.

Person| Relation  
---|---  
Darth Vader| father  
Leia| sister  
Han| brother in law  
R2D2| droid  
  
### Examples

    relation_to_luke("Darth Vader") ➞ "Luke, I am your father."
    
    relation_to_luke("Leia") ➞ "Luke, I am your sister."
    
    relation_to_luke("Han") ➞ "Luke, I am your brother in law."

### Notes

N/A

"""

def relation_to_luke(name):
  relation = ""
  
  if(name == "Darth Vader"):
    relation = "father."
  elif(name == "Leia"):
    relation = "sister."
  elif(name == "Han"):
    relation = "brother in law."
  elif(name == "R2D2"):
    relation = "droid."
  
  return "Luke, I am your " + relation

