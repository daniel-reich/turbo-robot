"""


Create two functions `to_camel_case()` and `to_snake_case()` that each take a
single string and convert it into either camelCase or snake_case. If you're
not sure what these terms mean, check the **Resources** tab above.

### Examples

    to_camel_case("hello_edabit") ➞ "helloEdabit"
    
    to_snake_case("helloEdabit") ➞ "hello_edabit"
    
    to_camel_case("is_modal_open") ➞ "isModalOpen"
    
    to_snake_case("getColor") ➞ "get_color"

### Notes

Test input will always be appropriately formatted as either camelCase or
snake_case, depending on the function being called.

"""

import string
def to_snake_case(txt):
  newstring = ""
  for i in txt:
    if i in string.ascii_uppercase:
      newstring += "_"
      newstring += i.lower()
    else:
      newstring += i
  return newstring
  
def to_camel_case(txt):
  splitstr = txt.split("_")
  newstring = ""
  c2 = 0
  for i in splitstr:
    c = 0
    for x in i:
      print(":")
      if c == 0 and c2 != 0:
        print(x.upper())
        newstring += x.upper()
      else:
        print(x)
        newstring += x
      c += 1
    c2 += 1
  return newstring

