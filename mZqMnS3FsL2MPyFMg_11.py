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

def num_to_eng(n):
  single = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
  teen = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
  tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "hundred"]
  if n < 10:
    return single[n]
  if n < 20:
    return teen[n-10]
  if n < 100:
    if n %10 == 0:
      return tens[n//10 - 2]
    return tens[n//10 -2] + " " + single[n%10]
  if n % 100 == 0:
    return single[n//100] + " " + "hundred"
  return single[n//100] + " " + "hundred " + num_to_eng(n%100)

