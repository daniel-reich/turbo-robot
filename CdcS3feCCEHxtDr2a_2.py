"""


Create a function that returns `True` if an array of pairs are sufficient for
a clear ordering of all items.

To illustrate:

    clear_ordering([["D", "A"], ["C", "B"], ["A", "C"]]) ➞ True
    # Since unequivocally: "D" < "A" < "C" < "B"

On the other hand:

    clear_ordering([["D", "A"], ["B", "A"], ["C", "D"]]) ➞ False
    # Since we know that "C" < "D" < "A", and we know "B" < "A"
    # but we don't know anything about "B"s relationship with "C" or "D".

### Examples

    clear_ordering([["S", "T"], ["T", "U"], ["U", "V"]]) ➞ True
    
    clear_ordering([["T", "S"], ["T", "U"], ["U", "V"], ["V", "W"]]) ➞ False

### Notes

See Comments for a good visualization of the question.

"""

def clear_ordering(lst):
    firstDict = {}
    secondDict = {}
    for item in lst:
        if item[0] in firstDict:
            firstDict[item[0]] += 1
        else:
            firstDict[item[0]] = 1         
        if item[1] in secondDict:
            secondDict[item[1]] += 1
        else:
            secondDict[item[1]] = 1
    for item in firstDict:
        if firstDict[item] > 1:
            return False
    for item in secondDict:
        if secondDict[item] > 1:
            return False
    return True

