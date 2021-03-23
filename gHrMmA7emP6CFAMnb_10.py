"""


In this challenge, you have to establish if a number is apocalyptic. A
positive integer `n` greater than 0 is apocalyptic when **2 elevated to`n`**
contains one or more occurrences of **666** into it.

Given an integer n, implement a function that returns:

  * `"Safe"` if `n` is not apocalyptic.
  * `"Single"` if into `2^n` there's a single occurence of 666.
  * `"Double"` if into `2^n` there are two occurences of 666.
  * `"Triple"` if into `2^n` there are three occurences of 666.

### Examples

    is_apocalyptic(66) ➞ "Safe"
    # 2^66 = 73786976294838206464
    
    is_apocalyptic(157) ➞ "Single"
    # 2^157 =
    # 182687704|666|362864775460604089535377456991567872
    
    is_apocalyptic(220) ➞ "Double"
    # 2^220 =
    # 168499|666|66969149871|666|8844293872691710232152640 ...
    
    is_apocalyptic(931) ➞ "Triple"
    # 2^931 =
    # 181520618710|666|8777829|666|135436890332191479738353753001777065257954029122510259245050254290156440857653562895251700406555730694879815558725330603736697259064676478076718090|666| ...

### Notes

  * Any given `n` will be a positive integer in the range of 1 to 1000.
  * Occurrences have to be unique, you can't use digits that have already been matched again (see example #3, there are five adjacent 6, but only a possible match).

"""

def is_apocalyptic(number):
  
  rawnum = str(2**number)
  print(rawnum)
  n = (rawnum.count("666"))
  print(n)
  d = {0:"Safe", 1:"Single", 2:"Double", 3:"Triple"}
  return(d[n])
