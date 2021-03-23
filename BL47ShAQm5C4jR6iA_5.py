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
    if(len(dct) > 2):
      return list(sorted(dct.items(), key=lambda i: i[1])[-3])[0]
    return 0
​
​
print(third_most_expensive({"Jack": 3, "Alice": 4, "Bob": 2}))

