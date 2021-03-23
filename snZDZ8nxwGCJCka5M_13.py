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
    is_inverted = _type == "REV"
    return build_pyramid(string, is_inverted)
​
def build_pyramid(string, is_inverted):
    return build_pyramid_recursive([], list(string), 1, is_inverted)
​
def build_pyramid_recursive(pyramid, blocks, height, is_inverted):
    does_not_have_blocks = len(blocks) == 0
    if (does_not_have_blocks):
        return pyramid
    
    if (is_inverted):
        pyramid_top = blocks[-height:]
        rest_of_blocks = blocks[:-height]
        pyramid = [' '.join(pyramid_top)] + pyramid
        pyramid_top_is_different_from_height = height != len(pyramid_top)
        if (pyramid_top_is_different_from_height):
            return "Error!"
    else:
        pyramid_base = blocks[:height]
        rest_of_blocks = blocks[height:]
        pyramid = pyramid + [' '.join(pyramid_base)]
        pyramid_base_is_different_from_height = height != len(pyramid_base)
        if (pyramid_base_is_different_from_height):
            return "Error!"
​
    return build_pyramid_recursive(pyramid, rest_of_blocks, height + 1, is_inverted)

