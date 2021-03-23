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

def to_snake_case(string):
  i = 0
  result = ""
  while(i < len(string)):
    if(string[i] == string[i].upper()):
      result = result + "_" + string[i].lower()
    else:
      result = result + string[i]
    i = i + 1
  return(result)
def to_camel_case(string):
  i = 0
  result = ""
  while(i < len(string)):
    if(string[i] == "_"):
      result = result + string[i + 1].upper()
      i = i + 1
    else:
      result = result + string[i]
    i = i + 1
  return(result)
#Code By Cool Programmer

