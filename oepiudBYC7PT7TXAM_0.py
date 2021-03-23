"""


Create a function that takes in a Roman numeral as a string and converts it to
an integer, returning the result. The function should work for all Roman
numerals representing positive integers less than 4000.

The following table shows how digits will be represented in Roman numeral
notation:

Place value| 1| 2| 3| 4| 5| 6| 7| 8| 9  
---|---|---|---|---|---|---|---|---|---  
Ones| I| II| III| IV| V| VI| VII| VIII| IX  
Tens| X| XX| XXX| XL| L| LX| LXX| LXXX| XC  
Hundreds| C| CC| CCC| CD| D| DC| DCC| DCCC| CM  
Thousands| M| MM| MMM| -| -| -| -| -| -  
  
### Examples

    parse_roman_numeral("VII") ➞ 7
    
    parse_roman_numeral("DCLXXIX") ➞ 679
    
    parse_roman_numeral("MMMCMV") ➞ 3905

### Notes

  * All letters will be in uppercase.
  * Assume all inputs will be well-formed Roman numerals.
  * While you could probably solve this by separately checking for each of these sequences inside the string, there is a smarter way. Think about the numerical value each individual letter has, and how the letter immmediately following it can affect that letter's numerical value.

"""

def parse_roman_numeral(num):
  value = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
  total = 0
  for i in range(len(num)):
    if i < len(num) - 1 and value[num[i]] < value[num[i+1]]:
      total -= value[num[i]]
    else:
      total += value[num[i]]
  return total

