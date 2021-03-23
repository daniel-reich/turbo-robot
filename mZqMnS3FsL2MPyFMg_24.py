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
    begin = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    twenties = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    hundreds = ["", "one hundred", "two hundred", "three hundred", "four hundred", "five hundred", "six hundred", "seven hundred", "eight hundred", "nine hundred"]
    result = ""
    sn = str(n)
    if len(sn) == 3:
        result += hundreds[int(sn[0])] + " "
        if sn[1] == "1":
            result += teens[int(sn[2])]
        else:
            result += twenties[int(sn[1])]
            if sn[1] != "0":
                result += " "
            result += begin[int(sn[2])]
    elif len(sn) == 2:
        if sn[0] == "1":
            result += teens[int(sn[1])]
        else:
            result += twenties[int(sn[0])]
            if sn[1] != "0":
                result += " "
            result += begin[int(sn[1])]
    else:
        result += begin[int(sn[0])]
    
    return result

