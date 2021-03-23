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
​
def camelCasing(txt):
    string_split = re.split('_| ',txt)
    string_split[0] = string_split[0].lower()
​
    for word in range(1, len(string_split)):
        string_split[word] = string_split[word].capitalize()
    camelCase_string = "".join(string_split)
​
    return camelCase_string

