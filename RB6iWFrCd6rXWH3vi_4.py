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

def longest_substring(d):
  parity = ['x']+['o' if int(i)%2 else 'e' for i in d]+['x']
  repeats = [parity[i-1:i+2].count(parity[i]) for i in range(1,len(parity)-1)]
  indices = [i for i in range(len(repeats)) if (i in [0,len(repeats)-1] and repeats[i]==1) or (repeats[i]==2 and i in range(1, len(repeats)-1) and (repeats[i-1]==1 or repeats[i+1]==1))]
  subs = [d[indices[i]:indices[i+1]+1] for i in range(0,len(indices),2)]
  return max(subs,key=len)

