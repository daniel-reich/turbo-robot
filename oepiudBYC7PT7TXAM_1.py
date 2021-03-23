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
  ans = 0
  while num:
    if num[0] == "M":
      ans+= 1000
      num = num[1:]
    elif num[:2] == "CM":
      ans+=900
      num = num[2:]
    elif num[0] == "D":
      ans+= 500
      num = num[1:]
    elif num[:2] == "CD":
      ans+=400
      num = num[2:]
    elif num[:1] == "C":
      ans+=100
      num = num[1:]
    elif num[:2] == "XC":
      ans+=90
      num = num[2:]
    elif num[:1] == "L":
      ans+=50
      num = num[1:]
    elif num[:2] == "XL":
      ans+=40
      num = num[2:]
    elif num[:1] == "X":
      ans+=10
      num = num[1:]
    elif num[:2] == "IX":
      ans+=9
      num = num[2:]
    elif num[:1] == "V":
      ans+=5
      num = num[1:]
    elif num[:2] == "IV":
      ans+=4
      num = num[2:]
    else:
      ans += len(num)
      num = ''
  return ans

