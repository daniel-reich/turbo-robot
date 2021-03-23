"""


You will be given a string consisting of a list of integers and their
relationships to their neighboring integers. For instance:

    "-15<-10<=0=0<5"

Test to see that all the relationships between the integers in the string are
true. If they are, return `True`. If they are not, return `False`.

### Examples

    validate_relationships("5>-1<0=0<-5>5=5") ➞ False
    # This is False because 0 is not less than -5.
    
    validate_relationships("-15<-10<=0=0<5") ➞ True
    
    validate_relationships("0=807<1000<=1000>9990<-3605<=20") ➞ False
    # This is False because 0 is not equal to 807.

### Notes

  * This is a modifcation of Helen Yu's "Correct Signs" challenge.
  * As the examples above show, there could be negative numbers in the string.
  * The numbers will only be separated by: `=, <, >, >=, <=`
  * Tests will not contain any spaces.

"""

def validate_relationships(txt):
  str1=""
  st2=""
  ls=[]
  k=[]
  res1=[]
  res2=[]
  flag=True
  for i in txt:
    if i in ['0','1','2','3','4','5','6','7','8','9','-']:
      k.append(st2)
      st2=""
      str1+=i
    else:
      st2+=i
      ls.append(str1)
      str1=""
  ls.append(str1)
  for i in ls:
    if not i=='':
      res1.append(int(i))
  for i in k:
    if not i=='':
      res2.append(i)
  for i in res2:
    if i=='=':
      if res1[0]!=res1[1]:
        flag=False
        break
      else:
        res1=res1[1:]
    elif i=='<=':
      if res1[0]>res1[1]:
        flag=False
        break
      else:
        res1=res1[1:]
    elif i=='>=':
      if res1[0]<res1[1]:
        flag=False
        break
      else:
        res1=res1[1:]
    elif i=='<':
      if res1[0]>=res1[1]:
        flag=False
        break
      else:
        res1=res1[1:]
    elif i=='>':
      if res1[0]<=res1[1]:
        flag=False
        break
      else:
        res1=res1[1:]
  return flag

