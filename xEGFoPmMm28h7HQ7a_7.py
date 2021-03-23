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
    
    letters = [[], [], ["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"],["j", "k", "l"],\
           ["m", "n", "o"], ["p", "q", "r", "s"], ["t", "u", "v"], ["w", "x", "y", "z"]]
​
    digits_list = [int(x) for x in str(digits)]    
    
    if len(digits_list) == 2:
        list1 = letters[digits_list[0]]
        list2 = letters[digits_list[1]]
        return ["{}{}".format(i,j) for i in list1 for j in list2]
    elif len(digits_list) == 3:
        list1 = letters[digits_list[0]]
        list2 = letters[digits_list[1]]
        list3 = letters[digits_list[2]]
        return ["{}{}{}".format(i,j,k) for i in list1 for j in list2 for k in list3]
    else:
        list1 = letters[digits_list[0]]
        list2 = letters[digits_list[1]]
        list3 = letters[digits_list[2]]
        list4 = letters[digits_list[3]]
        return ["{}{}{}{}".format(i,j,k,l) for i in list1 for j in list2 for k in list3 for l in list4]

