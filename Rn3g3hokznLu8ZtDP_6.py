"""


Write a function which increments a string to create a new string.

  *  **If the string ends with a number** , the number should be incremented by `1`.
  *  **If the string doesn't end with a number** , `1` should be **added** to the new string.
  *  **If the number has leading zeros** , the amount of digits **should be considered**.

### Examples

    increment_string("foo") ➞ "foo1"
    
    increment_string("foobar0009") ➞ "foobar0010"
    
    increment_string("foo099") ➞ "foo100"

### Notes

N/A

"""

import re
​
def increment_string(word):
  ending_digits_patten  = re.compile(r"\d+");
  if(not word[-1].isdigit()):
    return word+"1";
  return re.sub(ending_digits_patten ,lambda m : increment(m.group()), word);
​
def increment(num_string):
  zeroes_idx  = num_string.rfind("0");
  zeroes , number  = num_string[:zeroes_idx+1] , num_string[zeroes_idx+1:];
  result  = zeroes + str(int(number) +1);
  return result[len(result)- len(num_string):]

