"""


Write a function that returns the **longest non-repeating substring** for a
string input.

### Examples

    longest_nonrepeating_substring("abcabcbb") ➞ "abc"
    
    longest_nonrepeating_substring("aaaaaa") ➞ "a"
    
    longest_nonrepeating_substring("abcde") ➞ "abcde"
    
    longest_nonrepeating_substring("abcda") ➞ "abcd"

### Notes

  * If multiple substrings tie in length, return the one which occurs **first**.
  *  **Bonus** : Can you solve this problem in **linear time**?

"""

def longest_nonrepeating_substring(txt):
​
  Counter = 0
  Length = len(txt)
​
  Current = 0
    
  Word = ""
  Target = txt[0]
  
  while (Current < Length):
        
    if (Word == ""):    
      Word = Word + txt[Current]
      Current += 1
        
    elif (txt[Current] in Word):
        
      if (len(Word) > len(Target)):
        Target = Word
        Counter += 1
        Current = Counter
        Word = ""
      else:
        Counter += 1
        Current = Counter
        Word = ""
    
    else:
      Word = Word + txt[Current]
      Current += 1
​
  if (len(Word) > len(Target)):
    Target = Word
​
  return Target

