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

import datetime
def data_type(value):
  d={type('fg'):'string',type(51):'integer',type(1.02):'float',type([1,2]):'list',type(True):'boolean',type(datetime.date(2018,1,1)):'date',type({'a':1}):'dictionary'}
  return d[type(value)]
