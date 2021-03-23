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

invert=f=lambda s:f(s[1:])+s[0].swapcase()if s else''

