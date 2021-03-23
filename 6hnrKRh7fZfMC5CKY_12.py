"""


Given an integer, return a new **integer** according to the rules below:

  * Split the number into groups of two digit numbers. If the number has an _odd_ number of digits, return `"invalid"`.
  * For each group of two digit numbers, concatenate the _last digit_ to a new string the same number of times as the value of the _first digit_.
  * Return the result as an _integer_.

    look_and_say(3132) ➞ 111222
    
    # By reading the number digit by digit, you get three "1" and three "2".
    # Therefore, you put three ones and three two's together.
    # Remember to return an integer.

### Examples

    look_and_say(95) ➞ 555555555
    
    look_and_say(1213141516171819) ➞ 23456789
    
    look_and_say(120520) ➞ 200
    
    look_and_say(231) ➞ "invalid"

### Notes

  * Note that the number **0** can be included (see example #3).
  * Check the **Resources** tab for a TED-Ed video for extra clarity.

"""

def look_and_say(n):
  n_s = str(n)
  if len(n_s) % 2 != 0:
    return "invalid"
  else:
    var = ""
    i = 0
    while i < len(n_s):
      j = 0
      while j < int(n_s[i]):
        var = var + n_s[i+1]
        j = j + 1
      i = i + 2
  return int(var)

