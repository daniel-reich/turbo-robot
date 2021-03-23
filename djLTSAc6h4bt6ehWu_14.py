"""


Using Camel Case (or camelCase) is where the first word is in lower case, and
all words after it have their first letter capitalised. Note that there are no
spaces in between words!

Create a function that takes a string and returns it back in camelCase.

### Examples

    camelCasing("Hello World") ➞ "helloWorld"
    
    camelCasing("snake_case") ➞ "snakeCase"
    
    camelCasing("low high_HIGH") ➞ "lowHighHigh"

### Notes

  * You need to remove all spaces and underscores.
  * There will be no numbers in inputs.

"""

#First capitalize txt 
#Second replace first capitalize letter with lowwer one
#Third check if there is '_'  and remove it 
#Forth join the sentence together  
#~~~~~~~~~~~~~~~~~~~~~
def camelCasing(txt):
  txt=txt.title()
  txt=list(txt)
  txt.insert(0,txt[0].lower())
  txt.remove(txt[1])
  for i in txt:
    if i=='_':
      txt.remove('_')
  return(''.join(txt).replace(' ',''))

