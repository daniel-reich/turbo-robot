"""


Write a function that takes a string input and returns the string in a
_reversed_ **case** and **order**.

### Examples

    invert("dLROW YM sI HsEt") ➞ "TeSh iS my worlD"
    
    invert("ytInIUgAsnOc") ➞ "CoNSaGuiNiTY"
    
    invert("step on NO PETS") ➞ "step on NO PETS"
    
    invert("XeLPMoC YTiReTXeD") ➞ "dExtErIty cOmplEx"

### Notes

  * No empty strings and will neither contain special characters nor punctuation.
  * A recursive version of this challenge can be found via this [link](https://edabit.com/challenge/hmt2HMc4XNYrwPkDh).

"""

invert=lambda s:''.join(i.upper() if i.islower() else i.lower() for i in s[::-1])

