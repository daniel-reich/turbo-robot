"""


Given a list of words in the singular form, return a set of those words _in
the plural form_ **if they appear more than once in the list.**

###  Examples

    pluralize(["cow", "pig", "cow", "cow"]) ➞ { "cows", "pig" }
    
    pluralize(["table", "table", "table"]) ➞ { "tables" }
    
    pluralize(["chair", "pencil", "arm"]) ➞ { "chair", "pencil", "arm" }

### Notes

  * This is an **oversimplification** of the English language so no edge cases will appear.
  * Only focus on whether or not to add an **s** to the ends of words.
  * All tests will be valid.

"""

def pluralize(lst):
    last=[]
    lst1=set(lst)
    lst1=list(lst1)
    for i in lst1:
        if lst.count(i)==1:
            last.append(i)
        else:
            last.append(i+'s')
    return set(last)
