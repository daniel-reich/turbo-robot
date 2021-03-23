"""


In this challenge you are given a string and a slice made from that string.
Make a function that returns an expression that can be used to make that
slice. Your answer must contain only the minimum number of keystrokes needed
to make the slice.

### Examples

    slicer("abcd", "b") ➞ "[1]"
    
    slicer("abcdefg", "cb") ➞ "[2:0:-1]"
    
    slicer("abcdefg", "be") ➞ "[1::3]"
    
    slicer("abcdefgh", "bdf") ➞ "[1:6:2]"

### Notes

  * Test cases are slices that can be made with the `[start:end:step]` type expression.
  * The strings are composed of unique characters (no repeats).

"""

def slicer(string, slic):
  # Single character
  if len(slic) == 1:
    return "[{}]".format(string.find(slic))
  
  # Substring
  begin_substr = string.find(slic)
  if begin_substr != -1:
    end = begin_substr + len(slic)
    return "[{}:{}]".format(begin_substr if begin_substr else '', 
                           end if end != len(string) else '')
  
  # Reverse substring
  begin_substr = string[::-1].find(slic)
  if begin_substr != -1:
    offset_to_start = len(string) - begin_substr - 1
    start = offset_to_start if begin_substr else begin_substr
    end = offset_to_start - len(slic)
    return "[{}:{}:-1]".format(start if start else '', 
                              end if len(slic) != len(string) else '')
  
  # Sequence of characters
  found_char_pos = [i for i in range(len(string)) if string[i] in slic]
  start = found_char_pos[0]
  step = found_char_pos[1] - found_char_pos[0]
  end = found_char_pos[-1] + 1 if len(string) % step == 0 else 0
​
  # Check if reverse slice
  if ''.join(sorted(slic)) != slic:
    if found_char_pos[-1] != len(string) - 1:
      start = found_char_pos[-1] 
    step *= -1
​
  return "[{}:{}:{}]".format(start if start else '', end if end else '', step)

