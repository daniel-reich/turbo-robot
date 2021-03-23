"""


Create a function that takes a string as an argument. The function must return
a string containing 1s and 0s based on the string argument's words. If any
word in the argument is not equal to "zero" or "one" (case insensitive), you
should ignore it. The returned string's length should be a multiple of 8, if
the string is not a multiple of 8 you should remove the numbers in excess.

### Examples

    text_to_number_binary("zero one zero one zero one zero one") ➞ "01010101"
    
    text_to_number_binary("Zero one zero ONE zero one zero one") ➞ "01010101"
    
    text_to_number_binary("zero one zero one zero one zero one one two") ➞ "01010101"
    
    text_to_number_binary("zero one zero one zero one zero three") ➞ ""
    
    text_to_number_binary("one one") ➞ ""

### Notes

You must return the result as a string.

"""

def text_to_number_binary(txt):
  l=[]
  txt=txt.lower()
  t=txt.replace('zero','0').replace('one','1')
  r=t.split(' ')
  for i in r:
    if i=='0' or i=='1':
      l.append(i)
  s=''.join(l)    
  x=len(s)%8
  if x==0:
    return s
  return s[:-x]

