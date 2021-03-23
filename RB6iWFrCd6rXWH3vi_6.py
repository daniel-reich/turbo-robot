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
  n_digits = ''.join([str(int(x)%2) for x in digits])
  index_len = {}
  for i in range(len(n_digits)-1):
    l = 0
    for ii in range(len(n_digits[i:])-1):
      if n_digits[i+ii] != n_digits[i+ii+1]:
        l += 1
      else:
        break
    index_len[i] = l
  w_d = max(index_len, key=index_len.get)
  return digits[w_d:1 + w_d + index_len[w_d]]

