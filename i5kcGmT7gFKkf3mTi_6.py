"""


Create a function that returns the data type of a given variable. These are
the seven data types this challenge will be testing for:

  * List
  * Dictionary
  * String
  * Integer
  * Float
  * Boolean
  * Date

### Examples

    data_type([1, 2, 3, 4]) ➞ "list"
    
    data_type({'key': "value"}) ➞ "dictionary"
    
    data_type("This is an example string.") ➞ "string"
    
    data_type(datetime.date(2018,1,1)) ➞ "date"

### Notes

Return the name of the data type as a lowercase string.

"""

from datetime import date 
​
def data_type(value):
  value_type=type(value)
  types=["list","dictionary","string","integer","float","boolean","date"]
  if value_type == list:
    return types[0]
  elif value_type == dict:
    return types[1]
  elif value_type == str:
    return types[2]
  elif value_type == int:
    return types[3]
  elif value_type == float:
    return types[4]
  elif value_type == bool:
    return types[5]
  elif value_type == datetime.date:
    return types[6]

