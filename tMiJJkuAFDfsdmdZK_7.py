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
def to_snake_case(string):
  return re.sub(r"([A-Z])" , lambda m : "_" + m.group().lower() , string);
​
def to_camel_case(string):
  return re.sub(r"_([a-zA-Z])" , lambda m : m.group(1).upper() , string);

