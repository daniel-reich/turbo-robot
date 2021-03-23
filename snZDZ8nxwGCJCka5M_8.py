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

def pyramidal_string(string, ttpe):
  lst=[1,3,6,10,15,21,28]
  result=[]
  if ttpe=="REG":
    if string=='':
      return []
    if len(string) not in lst:
      return "Error!"
    else:
      x=lst.index(len(string))
      for i in range(1,x+2):
        result.append(' '.join(string[:i]))
        string=string[i:]
      return result
  else:
    if len(string)==1:
      return [string]
    if len(string) not in lst:
      return "Error!"
    else:
      x=lst.index(len(string))
      for i in range(x+1,0,-1):
        result.append(' '.join(string[:i]))
        string=string[i:]
      return result

