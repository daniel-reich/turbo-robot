"""


Write a function that transforms a list of characters into a list of
dictionaries, where:

  1. The keys are the characters themselves.
  2. The values are the ASCII codes of those characters.

### Examples

    to_dict(["a", "b", "c"]) ➞ [{"a": 97}, {"b": 98}, {"c": 99}]
    
    to_dict(["^"]) ➞ [{"^": 94}]
    
    to_dict([]) ➞ []

### Notes

N/A

"""

def to_dict(lst):
    lst_2=[]
    if not lst:
        return []
    else:
        for i in lst:
            dict={}
            dict[i]=ord(i)
            lst_2.append(dict)
    return lst_2

