"""


Create a function that, given a string `txt`, finds a letter that has a single
occurrence. Return the letter in uppercase. If the input is empty, return an
empty string `""`.

### Examples

    single_occurrence("EFFEAABbc") ➞ "C"
    
    single_occurrence("AAAAVNNNNSS") ➞ "V"
    
    single_occurrence("S") ➞ "S"

### Notes

The function will not be case sensitive.

"""

from collections import OrderedDict  
def single_occurrence(txt):
    if (txt == ""):
        return ("")
    #splits string into list of char
    def split(word): 
        return [char for char in word]  
    #counts occurrences of char in list
    def group_list(lst):   
        res =  [(el, lst.count(el)) for el in lst] 
        return list(OrderedDict(res).items())
    #string to uppercase
    txt = txt.upper()
    char_list = split(txt)
    occur = group_list(char_list)
    #finds single occurrence
    for i in occur:
        if i[1] == 1:
            return (i[0])

