"""


Create a function that takes a list and string. The function should remove the
letters in the string from the list, and return the list.

### Examples

    remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string") ➞ ["w"]
    
    remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon") ➞ ["b", "g", "w"]
    
    remove_letters(["d", "b", "t", "e", "a", "i"], "edabit") ➞ []

### Notes

  * If number of times a letter appears in the list is greater than the number of times the letter appears in the string, the extra letters should be left behind (see example #2).
  * If all the letters in the list are used in the string, the function should return an empty list (see example #3).

"""

from collections import Counter
def remove_letters(lst1, str1):
    removelst = []
    string1 = Counter(str1)
    list1 = Counter(lst1)
    for k, v in list1.items():
        if k not in string1:
            removelst.append(k)
        for k1, v1 in string1.items():
            if k == k1:
                if v1 < v:
                    removelst.append(k)
    return removelst

