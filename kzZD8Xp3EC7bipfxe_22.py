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

worded_math=lambda e:('Zero','One','Two')[eval(''.join([{'one':'1','two':'2','zero':'0','plus':'+','minus':'-'}[x]for x in e.lower().split()]))]

