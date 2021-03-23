"""


Create a function that checks if the argument is an integer or a string.
Return `"int"` if it's an integer and `"str"` if it's a string.

### Examples

    int_or_string(8) ➞ "int"
    
    int_or_string("Hello") ➞ "str"
    
    int_or_string(9843532) ➞ "int"

### Notes

Input will either be an integer or a string.

"""

from typing import Any, Union
​
​
def get_type(var: Any) -> str:
  return type(var).__name__
​
​
def int_or_string(var: Union[int, str]) -> str:
  return get_type(var)

