"""
Given a column title as it appears in an Excel sheet return its corresponding
column number.

The number is computed in the following way:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...

### Examples

    title_to_number("A") ➞ 1
    
    title_to_number("R") ➞ 18
    
    title_to_number("AB") ➞ 28

### Notes

  * `1 <= len(s) <= 7`
  * `s` consists only of uppercase English letters.

"""

VALUES = {chr(65+i): i+1 for i in range(26)}
for i in range(10):
    VALUES[str(i)] = i
INV_VALUES = {value: key for key, value in VALUES.items()}
​
POWERS = {(base, power): base**power for base in range(1, 37) for power in range(200)}
​
​
def from_base(k, base_k):
    # convert integer k in base base_k to decimal (base 10)
    L = len(k)
    res = 0
    for i in range(L - 1, -1, -1):
        res += VALUES[k[i]] * POWERS[(base_k, L - 1 - i)]
    return res
​
def title_to_number(s):
  return from_base(s, 26)

