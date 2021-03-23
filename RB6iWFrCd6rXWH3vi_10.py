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
  digits = digits
  longestSubstring = digits[0]
  substringArray = []
  parityBit = True if int(digits[0]) % 2 == 0 else False
  
  for x in digits[1:]:      
    if int(x) % 2 == 0 and not parityBit:
      parityBit = True
      longestSubstring += x
    elif (int(x) % 2) == 1 and parityBit:
      parityBit = False
      longestSubstring += x
    else:
      substringArray.insert(len(substringArray), longestSubstring)
      longestSubstring = x
      parityBit = True if int(x) % 2 == 0 else False
  
  if longestSubstring:
    substringArray.insert(len(substringArray), longestSubstring)
    
  return (max(substringArray, key=len))

