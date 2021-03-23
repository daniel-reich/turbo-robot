"""


Time to call your lover to inform him/her what he/she lost in the burglary.

Given a dictionary of the stolen objects, return the 3rd most expensive item
on the list. If that is not possible, because there are not enough items,
return `False`.

### Examples

    third_most_expensive({}) ➞ False
    
    third_most_expensive({"piano": 100}) ➞ False
    
    third_most_expensive({"piano": 100, "stereo": 200 }) ➞ False

### Notes

All prices will be of different monetary values.

"""

def third_most_expensive(dct):
    if len(dct)<3:return False
    return sorted(list(dct.items()),key = lambda x:x[1],reverse=True)[2][0]

