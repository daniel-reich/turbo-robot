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

def invert(s):
  if len(s)==1:
    return s.upper() if s.islower() else s.lower()
  if s[-1].islower():
    return s[-1].upper()+invert(s[:-1])
  return s[-1].lower()+invert(s[:-1])

