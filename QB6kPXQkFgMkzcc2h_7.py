"""


Create a function that will remove the letters "a", "b" and "c" from the given
string and return the modified version. If the given string does not contain
"a", "b", or "c", return `None`.

### Examples

    remove_abc("This might be a bit hard") ➞ "This might e  it hrd"
    
    remove_abc("hello world!") ➞ None
    
    remove_abc("") ➞ None

### Notes

If the given string does not contain "a", "b", or "c", return `None`.

"""

def remove_abc(txt):
  txt1=''
  for i in txt:
    if i.lower()=='a' or i.lower()=='b' or i.lower()=='c':
      continue
    else:
      txt1=txt1+i
  return None if txt1==''or txt1==txt else txt1

