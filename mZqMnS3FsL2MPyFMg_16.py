"""


Write a function that accepts a positive integer between `0` and `999`
inclusive and returns a string representation of that integer written in
English.

### Examples

    num_to_eng(0) ➞ "zero"
    
    num_to_eng(18) ➞ "eighteen"
    
    num_to_eng(126) ➞ "one hundred twenty six"
    
    num_to_eng(909) ➞ "nine hundred nine"

### Notes

  * There are no hyphens used (e.g. "thirty five" not "thirty-five").
  * The word "and" is not used (e.g. "one hundred one" not "one hundred and one").

"""

nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
def num_to_eng(n):
  if n > 100:
    return nums[n//100] + " hundred " + num_to_eng(n%100)
  if n < 20:
    return nums[n]
  if n % 10 == 0:
    return tens[n//10-2]
  return tens[n//10-2] + " " + nums[n%10]

