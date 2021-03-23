"""


Given a string of digits, return the longest substring with _alternating_
odd/even or even/odd digits. If two or more substrings have the same length,
return the substring that occurs first.

### Examples

    longest_substring("225424272163254474441338664823") ➞ "272163254"
    # substrings = 254, 272163254, 474, 41, 38, 23
    
    longest_substring("594127169973391692147228678476") ➞ "16921472"
    # substrings = 94127, 169, 16921472, 678, 476
    
    longest_substring("721449827599186159274227324466") ➞ "7214"
    # substrings = 7214, 498, 27, 18, 61, 9274, 27, 32
    # 7214 and 9274 have same length, but 7214 occurs first.

### Notes

The minimum alternating substring size is 2.

"""

def longest_substring(digits):
  biggest_sub, current_sub = "", "" 
  for i in range(len(digits)-1):
    if (int(digits[i])%2 == 0 and int(digits[i+1])%2 == 1) or (int(digits[i])%2 == 1 and int(digits[i+1])%2 == 0):
      current_sub += digits[i]
    else:
      if len(current_sub) == 0:
        continue
      if (int(current_sub[len(current_sub)-1])%2 == 0 and int(digits[i])%2 == 1) or (int(current_sub[len(current_sub)-1])%2 == 1 and int(digits[i])%2 == 0):
        current_sub += digits[i]
        if len(current_sub) > len(biggest_sub):
          biggest_sub = current_sub
          current_sub = ""
        else:
          current_sub = ""
      elif len(current_sub) > len(biggest_sub):
        biggest_sub = current_sub
        current_sub = ""
  if len(current_sub) != 0 and ((int(current_sub[len(current_sub)-1])%2 == 0 and int(digits[len(digits)-1])%2 == 1) or (int(current_sub[len(current_sub)-1])%2 == 1 and int(digits[len(digits)-1])%2 == 0)):
    current_sub += digits[len(digits)-1]
  if len(current_sub) > len(biggest_sub):
    return current_sub
  return biggest_sub

