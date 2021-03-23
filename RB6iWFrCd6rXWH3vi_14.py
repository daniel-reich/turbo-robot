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
​
  digits = str(digits)
  container = []
  word = ""
​
  for i in range(0, len(digits)):
​
    if len(word) == 0:
​
      word = word + digits[i]
​
    else:
​
      x = int(digits[i])
      y = int(word[-1])
​
      if x % 2 == 0 and y % 2 != 0 or x % 2 != 0 and y % 2 == 0:
        word = word + digits[i]
      else:
        container.append(word)
        word = "" + digits[i]
​
    container.append(word)
​
  container_sort = container
  container_sort = sorted(container, key = len)
  x = len(container_sort[-1])
  container_sort = []
  for i in range(0, len(container)):
    if len(container[i]) == x:
      container_sort.append(container[i])
​
  return container_sort[0]

