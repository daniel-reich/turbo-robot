"""


The function is given a string containing digits from `2` to `9`. Return a set
of all possible letter combinations that could represent the digit-string.

### Digits to Letters Mapping

    d = { "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz" }

### Examples

    letters_combinations("23") ➞ { "ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf" }
    
    letters_combinations("") ➞ set()
    
    letters_combinations("2") ➞ { "a", "b", "c" }

### Notes

N/A

"""

def combo_list_of_string(lst_of_strs):
    if len(lst_of_strs) == 0:
        return ['']
    result = []
    for i in range(0, len(lst_of_strs)):
        for j in range(len(lst_of_strs[i])):
            to_add_letter = lst_of_strs[i][j]
            remain_lst_of_strs = lst_of_strs[i + 1:]
            for string in combo_list_of_string(remain_lst_of_strs):
                if len(string) == len(lst_of_strs) - 1:
                    result.append(to_add_letter + string)
    return result
​
​
​
def letters_combinations(digits):
    dict_phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    if len(digits) == 0:
        return set()
    lst_of_strs = []
    for i in range(len(digits)):
        lst_of_strs.append(list(dict_phone[digits[i]]))
    return set(combo_list_of_string(lst_of_strs))

