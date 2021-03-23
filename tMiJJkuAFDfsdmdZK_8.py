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

import re
​
def to_snake_case(txt):
  upperCase = re.sub(r'[^A-Z]', '', txt)
  if len(upperCase) == 0: return txt
  adjusted = re.sub(r'[A-Z]', '_`', txt)
  adjusted = list(adjusted)
  i = 0
  for count, elem in enumerate(adjusted): 
    if elem == '`':
      adjusted[count] = upperCase[i].lower()
      i += 1
  return "".join(adjusted)
​
def to_camel_case(txt):
  txt = list(txt)
  el = []
  for count, elem in enumerate(txt): 
    if elem == '_': el.append(txt[count] + txt[count + 1])
  if len(el) == 0: return "".join(txt)
  newString = "".join(txt)
  for i in el: 
    newString = re.sub(i, i[1].upper(), newString)
  return newString

