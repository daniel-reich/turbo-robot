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
    aplh_index = [[],[],["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"], ["m", "n", "o"], ["p", "q", "r", "s"],["t", "u", "v"], ["w", "x", "y", "z"]]
    length = 1
    for i in digits:
        length *= len(aplh_index[int(i)])
    results = []
    count = 0
    for i in range(len(digits)):
        result = ["" for i in range(length)]
        for char in aplh_index[int(digits[i])]:
            forward = (length // len(aplh_index[int(digits[i])])) * (aplh_index[int(digits[i])].index(char) + 1)
            while count != length:
                result[count] += char
                count += 1
                if count == forward:
                    break
        if len(result[-1]) != "":
            count = 0
            results.append(result)
            length = length // len(aplh_index[int(digits[i])])
    
    result = results[0]
    results.pop(0)
    for i in range(len(results)):
        needmore = len(result) // len(results[i])
        results[i] = results[i] * needmore
​
    for o in results:
        for i in range(len(result)):
            result[i] += o[i]
​
    return result

