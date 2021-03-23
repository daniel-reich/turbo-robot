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

def data_type(value):
  s = str(type(value))[8:-2]
  if s=="dict": return "dictionary"
  if s == "str": return "string"
  if s=="int": return "integer"
  if s == "datetime.date": return "date"
  return s
