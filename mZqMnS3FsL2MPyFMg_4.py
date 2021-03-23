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
  word = ""
  one = {
  0 : "zero",
  1 : "one", 
  2 : "two", 
  3 : "three",
  4 : "four", 
  5 : "five",
  6 : "six",
  7 : "seven", 
  8 : "eight",
  9 : "nine",
  10 : "ten",
  11 : "eleven",
  12 : "twelve", 
  13 : "thirteen",
  14 : "fourteen",
  15 : "fifteen",
  16 : "sixteen", 
  17 : "seventeen",
  18 : "eighteen", 
  19 : "nineteen"
  }
​
  two = {
  20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty", 70: "seventy", 80:"eighty", 90:"ninety"
  }
​
  if n >= 100: 
    word += one[n // 100] + " hundred "
    n -= n // 100 * 100
  if n >= 20:
    word += two[n - n % 10]
    n %= 10
    word += " "
  if n <= 19:
    word += one[n]
  
  return word

