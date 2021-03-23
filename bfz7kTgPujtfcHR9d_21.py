"""


Create a function which replaces all the x's in the string in the following
ways:

Replace all x's with "cks" **UNLESS** :

  * The word begins with "x", therefore replace it with "z".
  * The word is just the letter "x", therefore replace it with "ecks".

### Examples

    x_pronounce("Inside the box was a xylophone") ➞ "Inside the bocks was a zylophone"
    
    x_pronounce("The x ray is excellent") ➞ "The ecks ray is eckscellent"
    
    x_pronounce("OMG x box unboxing video x D") ➞ "OMG ecks bocks unbocksing video ecks D"

### Notes

  * All x's are lowercase.
  * I know that not all words with x's follow this rule, but there are too many edge cases to count!

"""

def x_pronounce(sentence):
  b=sentence.split(" ")
  a=len(b)
  newStr=""
  f=""
  for i in range(0,a):
    c=b[i]
    d=len(c)
    if(c=="x" and d==1):
      f="ecks"
    elif(c[0]=="x"):
      e="z"
      f=e+c[1:]
    elif(c.count("x")>0):
      for j in range(0,d):
        if(c[j]=="x"):
          f=c[0:j]+"cks"+c[j+1:]
    else:
      f=c
    if(i==0):
      newStr=newStr+f
    else:
      newStr=newStr+" "+f
  return newStr

