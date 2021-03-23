"""


Create a function that outputs the result of a math expression in words.

### Examples

    worded_math("One plus one") ➞ "Two"
    
    worded_math("zero Plus one") ➞ "One"
    
    worded_math("one minus one") ➞ "Zero"

### Notes

  * Expect only the operations `plus` and `minus`.
  * Expect to only get numbers and answers from `0` to `2`.
  * The first letter of the answer must be capitalised.

"""

def worded_math(equ):
    nums = ['zero', 'one', 'two']
    lst = equ.split()
    if lst[1].lower() == 'plus':
        return nums[nums.index(lst[0].lower())
                    + nums.index(lst[2].lower())].capitalize()
    elif lst[1].lower() == 'minus':
        return nums[nums.index(lst[0].lower())
                    - nums.index(lst[2].lower())].capitalize()

