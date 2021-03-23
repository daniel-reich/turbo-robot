"""


Write a function that returns `True` if a string consists of **ascending or
ascending AND consecutive** numbers.

### Examples

    ascending("232425") ➞ True
    # Consecutive numbers 23, 24, 25
    
    ascending("2324256") ➞ False
    # No matter how this string is divided, the numbers are not consecutive.
    
    ascending("444445") ➞ True
    # Consecutive numbers 444 and 445.

### Notes

A **number** can consist of any number of digits, so long as the numbers are
adjacent to each other, and the string has at least two of them.

"""

def ascending(txt):
  factors = lambda x: [f for f in range(1,x) if not x%f]
  for i in factors(len(txt)):
    nums = [int(txt[s:s+i]) for s in range(0,len(txt),i)]
    print(sum(range(1,len(nums))))
    if sum(range(1,len(nums)))==(sum(nums) - (nums[0]*len(nums))):
      return True
    print(nums)
  return False

