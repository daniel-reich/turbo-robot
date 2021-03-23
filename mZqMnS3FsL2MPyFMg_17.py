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
  number = str(n)
  
  if n == 0:
    return "zero"
  
  single = {  "1": "one",
              "2": "two",
              "3": "three",
              "4": "four",
              "5": "five",
              "6": "six",
              "7": "seven",
              "8": "eight",
              "9": "nine",
              "0": ""       }
  double = {  "10": "ten",
              "11": "eleven",
              "12": "twelve",
              "13": "thirteeen",
              "14": "fourteen",
              "15": "fifteen",
              "16": "sixteen",
              "17": "seventeen",
              "18": "eighteen",
              "19": "nineteen" }
  prefix = {  "2": "twenty",
              "3": "thirty",
              "4": "forty",
              "5": "fifty",
              "6": "sixty",
              "7": "seventy",
              "8": "eighty",
              "9": "ninety",
              "0": ""         }
  toReturn = ""
  if len(number) == 3:
    toReturn += single[number[0]]
    toReturn += " hundred "
    number = number[1:]
  if len(number) == 2:
    if number in double:
      toReturn += double[number]
    else:
      if number[0] != "0":
        toReturn += prefix[number[0]]
        toReturn += " "
      toReturn += single[number[1]]
  else:
    return single[number]
  
  return toReturn

