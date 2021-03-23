"""


In this challenge, you have to obtain a pyramidal version of a given string,
transforming the string into a list containing a series of string slices that
progressively increase or decrease **steadily** from the left to the right.
Every slice containing two or more characters must have **a space between
every pair of characters** , to permit a hypothetical vertical alignment. See
the example below:

    # REGULAR pyramidal version of "EDABIT"
    
    [ "E",
     "D A",
    "B I T" ]

Depending on the given `_type`, you have to obtain a **regular** pyramid
starting from its vertex (`_type === "REG"`) as in the example above, or a
**reversed** pyramid starting from its base (`_type === "REV"`) as in the
example below:

    # REVERSED pyramidal version of "EDABIT"
    
    ["E D A",
      "B I",
       "T"  ]

Every pyramid must follow the same steadily increment/decrement of its slices
(or rows) by exactly one character (excluding spaces), so that not every
string can be transformed in a pyramid! See the example below:

    # Regular pyramidal version of "PYRAMID"
    
    [ "P",
     "Y R",
    "A M I" ]
    
    # Letter "D" can't be placed in the pyramid

Given as parameters a `string` and a `_type`, implement a function that
returns:

  * A string `"Error!"` if the pyramidal version can't be obtained from the given `string`.
  * A list containing the regular pyramidal version of the `string` if the given `_type` is equal to `"REG"`.
  * A list containing the reversed pyramidal version of the `string` if the given `_type` is equal to `"REV"`.

### Examples

    pyramidal_string("EDABIT", "REG") ➞ ["E", "D A", "B I T"]
    
    pyramidal_string("EDABIT", "REV") ➞ ["E D A", "B I", "T"]
    
    pyramidal_string("PYRAMID", "REG") ➞ "Error!"
    
    pyramidal_string("!", "REV") ➞ ["!"]
    
    pyramidal_string("", "REG") ➞ []

### Notes

  * If the given `string` has just one character, the returned list will contain that single character. If the given `string` is empty, the returned list will be empty.
  * Remember to insert a space between every character inside the rows containing two or more characters.
  * The increment and the decrement of the rows in a pyramidal string are equal to one character more or less than the previous, depending on the given `_type`.
  * You have to find a discriminant rule to establish if a string can be transformed into a pyramid, without creating single exceptions for every given case. What is suggesting to you the shape of a pyramid seen frontally?

"""

def pyramidal_string(string, _type):
  # special cases
  if string == '':
    return []
  if len(string) == 1:
    return [string]
​
  pyramid_lines = calculate_pyramid_lines(string)
  if pyramid_lines == -1:
    return 'Error!'
​
  if _type == 'REV':
    return pyramidal_string_reverse(string, pyramid_lines)
  else:
    return pyramidal_string_regular(string)
  
def pyramidal_string_regular(string):
  str_len = len(string)
  result = []
  i = 0
  j = 1
  while i < str_len:
    result.append(adjust_line(string[i:i + j]))
    i += j
    j += 1
  return result
​
def pyramidal_string_reverse(string, pyramid_lines):
  str_len = len(string)
  result = []
  i = 0
  j = pyramid_lines - 1
  while i < str_len:
    result.append(adjust_line(string[i:i + j]))
    i += j
    j -= 1
  return result
​
def calculate_pyramid_lines(string):
  str_len = len(string)
  i = 0
  j = 1
  while i < str_len:
    i += j
    j += 1
  return j if str_len == i else -1
​
def adjust_line(string):
  str_len = len(string)
  str_final = ''
  for i in range(str_len):
    if i < str_len - 1:
      str_final += string[i] + ' '
    else:
      str_final += string[i]
  return str_final

