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

def letter_combinations(digits):
    keys = {'1': '', '2': 'abc', '3': 'def', '4':'ghi', '5': 'jkl', '6': 'mno', '7': 'prs', '8': 'tuv',
            '9': 'wxyz'}
    def permute(length):
        if length == len(digits):
            return list(keys[digits[len(digits)-1]])
        else:
            return [x + y for x in list(keys[digits[length - 1]]) for y in permute(length + 1)]
    return permute(1)

