"""


Given a string containing **unique** letters, return a sorted string with the
letters that **don't appear in the string**.

### Examples

    get_missing_letters("abcdefgpqrstuvwxyz") ➞ "hijklmno"
    
    get_missing_letters("zyxwvutsrq") ➞ "abcdefghijklmnop"
    
    get_missing_letters("abc") ➞ "defghijklmnopqrstuvwxyz"
    
    get_missing_letters("abcdefghijklmnopqrstuvwxyz") ➞ ""

### Notes

  * The combination of both strings should be **26 elements** long, including all the letters in the alphabet.
  * Letters will all be in lowercase.

"""

def get_missing_letters(s):
​
  Sample = str(s)
  Sample = Sample.lower()
  Sample = list(Sample)
  Sample = sorted(Sample)
  
  Code = "abcdefghijklmnopqrstuvwxyz" 
  Complete = list(Code)
  Complete = sorted(Complete)
  
  Wanted = []
  
  CC = 0
  CL = len(Code)
    
  SC = 0
  SL = len(Sample)
  
  while (CC < CL) and (SC < SL):    
    Code_Item = str(Code[CC])
    Sample_Item = str(Sample[SC])
    
    if (Sample_Item != Code_Item):
      Wanted.append(Code_Item)
      CC += 1
    else:
      CC += 1
      SC += 1
    
  while (CC < CL):
    Code_Item = str(Code[CC])
    Wanted.append(Code_Item)
    CC += 1
    
  Missing = ""
  
  Counter = 0
  Length = len(Wanted)
  
  while (Counter < Length):
    Item = str(Wanted[Counter])
    Missing = Missing + Item
    Counter += 1
  
  return Missing

