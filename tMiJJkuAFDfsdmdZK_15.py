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

def to_snake_case(txt):
  new_lst = []
  for i in range(0, len(txt)):
    if txt[i].upper() == txt[i]:
      new_lst.append('_' + txt[i].lower())
    else:
      new_lst.append(txt[i])
  return ''.join(new_lst)
​
def to_camel_case(txt):
  new_lst = []
  str_split = txt.split('_')
  for i in range(0, len(str_split)):
    if i > 0:
      new_lst.append(str_split[i].capitalize())
    else:
      new_lst.append(str_split[i])
  return ''.join(new_lst)

