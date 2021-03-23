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

numbers = {
0: "zero",
1: "one",
2: "two",
3: "three",
4: "four",
5: "five",
6: "six",
7: "seven",
8: "eigth",
9: "nine",
10: "ten",
11: "eleven",
12: "twelve",
13: "thirteen",
14: "fourteen",
15: "fifeteen",
16: "sixteen",
17: "seventeen",
18: "eighteen",
19: "nineteen",
20: "twenty",
30: "thirty",
50: "fifty"
}
def num_to_eng(n):
  res = ""
  if n in numbers.keys():
    return numbers[n]
  if n >= 100:
    res = numbers[n//100] + " hundred" + " "
    n = n % 100
  if n in numbers.keys():
    return res + numbers[n]
  p = (n // 10)*10 
  if p in numbers.keys():
    res += numbers[p]
  else:
    res += numbers[n // 10] + "ty"
  return res + " " + numbers[n-p]   
    
  
  return res

