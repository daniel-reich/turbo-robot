"""


Write a **recursive** function that takes a string input and returns the
string in a _reversed_ **case** and **order**.

### Examples

    invert("dLROW YM sI HsEt") ➞ "TeSh iS my worlD"
    
    invert("ytInIUgAsnOc") ➞ "CoNSaGuiNiTY"
    
    invert("step on NO PETS") ➞ "step on NO PETS"
    
    invert("XeLPMoC YTiReTXeD") ➞ "dExtErIty cOmplEx"

### Notes

  * No empty strings and will neither contain special characters nor punctuation.
  * You are expected to solve this challenge using a **recursive** approach.
  * You can check on the **Resources** tab for more details about _recursion_.
  * An iterative version of this challenge can be found via this [link](https://edabit.com/challenge/jyqcRv6giw8an8KB2).

"""

def invert(s, i=0):
  if i == len(s) - 1:
    l8r = s[i]
    if l8r.islower() == True:
      return l8r.upper()
    else:
      return l8r.lower()
  else:
    l8r = s[i]
    if l8r.islower() == True:
      cl8r = l8r.upper()
    else:
      cl8r = l8r.lower()
    
    i += 1
    return invert(s,i) + cl8r

