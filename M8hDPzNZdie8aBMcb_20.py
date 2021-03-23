"""


Implement a function count_substring that counts the number of substrings that
begin with character "A" and ends with character "X".

For example, given the input string `"CAXAAYXZA"`, there are four substrings
that begin with "A" and ends with "X", namely: "AX", "AXAAYX", "AAYX", and
"AYX".

### Examples

    count_substring("CAXAAYXZA") ➞  4
    
    count_substring("AAXOXXA") ➞ 6
    
    count_substring("AXAXAXAXAX") ➞ 15

### Notes

  * You should aim to avoid using nested loops to complete the task.
  * You can assume that the input string is composed of English upper case letters only.

"""

def count_substring(s):
    cnt = 0
    idxa = s.find('A')
    while idxa != -1:
        cnt+= s[idxa+1:].count('X')
        x = s[idxa+1:].find('A')
        if x == -1:
            break
        idxa += x + 1
    return cnt

