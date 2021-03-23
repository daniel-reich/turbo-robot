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
  mystr = ""
  for i in range (len(txt)):
    if (txt[i].isupper()):
      mystr += "_" + txt[i].lower()
    else:
      mystr += txt[i]
  return mystr
​
def to_camel_case(txt):
  mystr = ""
  Flag = False
  for i in range (len(txt)):
    if (Flag==True):
      mystr += txt[i].upper()
      Flag = False
    elif (txt[i]=="_"):
      Flag = True
    else:
      mystr += txt[i]
  return mystr

