"""


Create a function that takes a string and returns `True` or `False` depending
on whether or not the given formula is correct.

### Examples

    formula("6 * 4 = 24") ➞ True
    
    formula("18 / 17 = 2") ➞ False
    
    formula("") ➞ None

### Notes

  * You have to figure out what `a` is.
  * Ignore the spaces.
  * If the input is an empty string `""`, return `None`.
  * You do not need to dynamically find the value of `a` (it's a constant and the same accross all tests).

"""

def formula(txt):
  if txt =='':
    return None
  else:
    if not 'a' in txt:
      txt = txt.split('=')
      #print(txt)
      res = eval(txt[0])
      bool = True
      for i in range(1,len(txt)):
        if res == eval(txt[i]):
          continue
        else:
          bool = False
          break
      return bool
    else:
      opr = ['*','+','-','/']
      if not any(elem in txt  for elem in opr):
        return True
      else:
        txt = txt.split('=')
        #print(txt)
        n = len(txt)
        res = 0
        i = 0
        bool = True
        while True:
          if not 'a' in txt[i]:
            res = eval(txt[i])
            break
          elif i + 1==n:
            break
          i+=1
        print(res)
        for i in range(n):
          if res == 0:
            break
          if 'a' in txt[i]:
            a = list(txt[i])
            if "*" in a:
              if res%int(a[-2])==0:
                bool = True
              else:
                bool = False
          elif res == eval(txt[i]):
            continue
          else:
            bool = False
            break
        return bool

