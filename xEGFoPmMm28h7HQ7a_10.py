"""


Given a string containing digits from `2-9` inclusive, return all possible
letter combinations that the number could represent. A mapping of digit to
letters (just like on the telephone buttons) is given below. Note that 1 does
not map to any letters.

![Alternative Text](https://edabit-challenges.s3.amazonaws.com/200px-
Telephone-keypad2.svg.png)

### Examples

    letter_combinations("23") ➞ ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    
    letter_combinations("532") ➞ ["jda", "jdb", "jdc", "jea", "jeb", "jec", "jfa", "jfb", "jfc", "kda", "kdb", "kdc", "kea", "keb", "kec", "kfa", "kfb", "kfc", "lda", "ldb", "ldc", "lea", "leb", "lec", "lfa", "lfb", "lfc"]

### Notes

N/A

"""

import itertools
import copy
​
​
def letter_combinations(digits):
    digits_map = dict(zip(['2', '3', '4', '5', '6', '7', '8', '9'], ['abc', 'def', 'ghi', 'jkl', 'mno', 'prs', 'tuv', 'wxyz']))
    results = []
​
    for digit in digits[1:]:
        if not results:
            results = list(digits_map[digits[0]])
        old_results = copy.copy(results)
        results = []
        for combination in itertools.product(old_results, digits_map[digit]):
            results.append((''.join(combination)))
    return results

