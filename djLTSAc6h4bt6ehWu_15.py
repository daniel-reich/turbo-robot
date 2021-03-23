"""


Using Camel Case (or camelCase) is where the first word is in lower case, and
all words after it have their first letter capitalised. Note that there are no
spaces in between words!

Create a function that takes a string and returns it back in camelCase.

### Examples

    camelCasing("Hello World") ➞ "helloWorld"
    
    camelCasing("snake_case") ➞ "snakeCase"
    
    camelCasing("low high_HIGH") ➞ "lowHighHigh"

### Notes

  * You need to remove all spaces and underscores.
  * There will be no numbers in inputs.

"""

import re
def camelCasing(s):
  pattern = '[a-zA-Z]+'
  res = re.findall(pattern, s)
​
  res = [res[i].title() if i != 0 else res[i].lower() for i in range(len(res))]
  return "".join(res)

