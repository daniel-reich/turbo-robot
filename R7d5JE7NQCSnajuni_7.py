"""


You prepare a list to send to the insurance company. As you finish, you notice
you misformatted it. Given a dictionary with at least one key/value pair,
convert all the values to numbers.

### Examples

    convert_to_number({ "piano": "200" }) ➞ { "piano": 200 }
    
    convert_to_number({ "piano": "200", "tv": "300" }) ➞ { "piano": 200, "tv": 300 }
    
    convert_to_number({ "piano": "200", "tv": "300", "stereo": "400" }) ➞ { "piano": 200, "tv": 300, "stereo": 400 }

### Notes

  * You will only be tested for numbers (ints), not strings or floats.
  * Look at the **Resources** tab if you need help.

"""

def convert_to_number(dictionary):
  
  Revised = {}
  
  Fronts = []
  Backs = []
  
  for key, value in dictionary.items():
    Fronts.append(key)
    Backs.append(value)
    
  Counter = 0
  Length = len(Fronts)
  
  while (Counter < Length):
    Key = str(Fronts[Counter])
    Value = int(Backs[Counter])
    Revised[Key] = Value
    Counter += 1
    
  return Revised

