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
    datee = datetime.date(2018,1,1)
    lst = [ 1,3,4,5]
    strr = "killl"
    booll = True
    dictt = {"k":1}
    intt = 3
    floatt = 9.0
    d = {type(strr) : "string" , type(booll):"boolean" , type(dictt) : "dictionary",  type(intt):"integer" , type(floatt):"float" , type(lst) : "list" , type(datee) : "date" }
​
    
    for key in d:
        if key == type(value):
            return(d[key])
    
value = [1, 2, 3, 4]     
print(data_type(value))

