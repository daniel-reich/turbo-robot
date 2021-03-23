"""


Maya numeral system was **vigesimal** ( _base 20_ ) and **positional** :
units, tens, hundreds (and so on) were read as descendant progressive powers
of 20, instead of 10 like we do with our decimal system. Some examples:

    - 39 => (1 x 20¹) + (19 x 20º)
    - 815 => (2 x 20²) + (0 x 20¹) + (15 x 20º)
    - 16125 => (2 x 20³) + (0 x 20²) + (6 x 20¹) + (5 x 20º)

Every digit (as to say the number to be multiplied for the power of 20) was
symbolized with a combination of pebbles (dots), woodsticks (lines) and shells
(used for the number 0) following a _base5_ system. See the table below:

![Mayan Numbers](https://edabit-challenges.s3.amazonaws.com/maya_numbers.jpg)

You must implement a function that, given a non-negative integer, returns a
list of strings, with each string representing the symbolized single digit.

Symbols to use are " **@** " for shells, " **-** " for lines and " **o** " for
dots. Dots have to be placed **before** the lines.

### Examples

    # Be careful, spaces between symbols are placed only for better readability!
    # Don't use spaces in returned strings.
    
    maya_number(39) ➞ ["o", "o o o o - - -"]
    
    maya_number(815) ➞ ["o o", "@", "- - -"]
    
    maya_number(16125) ➞ ["o o", "@", "o -", "-"]

### Notes

  * Check the **Resources** tab for more info on Maya numerals (and Maya arithmetic).
  * All given integers are valid, no exceptions to handle.

"""

def twenty_power(n):
    i = 0
    result = []
    while i >= 0:
        if n / (20 ** i) >= 20:
            i += 1
        else:
            result= [(i, n // (20 ** i))]
            break
    if n == n // (20 ** i) * (20 ** i):
        return result
    else:
        return result + twenty_power(n - (n // (20 ** i)) * (20 ** i))
​
​
def maya_number(n):
    dict_maya = {0: "@", 1:"o", 2: "oo", 3: "ooo", 4: "oooo", 5: '-', 6: "o-", 7: "oo-",
                 8: "ooo-", 9: "oooo-", 10: "--", 11: "o--", 12: "oo--", 13: 'ooo--',
                 14: "oooo--", 15: "---", 16: 'o---', 17: "oo---", 18: "ooo---", 19: "oooo---"}
    final_result = []
    result = [twenty_power(n)[0]]
    for i in range(1, len(twenty_power(n))):
        if twenty_power(n)[i-1][0] - twenty_power(n)[i][0] == 1:
            result.append(twenty_power(n)[i])
        elif twenty_power(n)[i-1][0] - twenty_power(n)[i][0] > 1:
            for j in range(twenty_power(n)[i-1][0]-1, twenty_power(n)[i][0], -1):
                result.append((j, 0))
            result.append(twenty_power(n)[i])
    if twenty_power(n)[-1][0] == 1:
        result.append((0, 0))
    for j in range(len(result)):
            final_result.append(dict_maya[result[j][1]])
    return final_result

