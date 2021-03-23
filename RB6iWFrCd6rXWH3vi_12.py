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
  ix = 0
  while True:
    if (int(digits[ix]) + int(digits[ix + 1])) % 2 == 1:
      ix += 1
    else:
      break
  last_s = 0
  last_e = ix
  max_s = 0
  max_e = last_e
  ix += 1
  while True:
    if ix == len(digits) - 2:
      if (int(digits[ix]) + int(digits[ix + 1])) % 2 == 0:
        last_s = last_e + 1
        last_e = ix
        if last_e - last_s > max_e - max_s:
          max_e = last_e
          max_s = last_s
      else:
        last_s = last_e + 1
        last_e = ix + 1
        if last_e - last_s > max_e - max_s:
          max_e = last_e
          max_s = last_s
      break
    else:
      if (int(digits[ix]) + int(digits[ix + 1])) % 2 == 0:
        last_s = last_e + 1
        last_e = ix
        if last_e - last_s > max_e - max_s:
          max_e = last_e
          max_s = last_s
      ix += 1
  return digits[max_s:max_e + 1]

