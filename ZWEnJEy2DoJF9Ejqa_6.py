"""


A string contains the word "edabit" if a _subsequence_ of its characters spell
"edabit".

Write a function that accepts a string and returns “YES” if the string
contains a subsequence of the word edabit or "NO" if it does not.

### Examples

    edabit_in_string(“eddaaabt”) ➞ “NO”
    
    edabit_in_string(“edwardisabletodoit”) ➞ “YES”
    
    edabit_in_string(“abecdfghijklmnopqrstuvwxyz”) ➞ “NO”

### Notes

Check the **Resources** tab for more details on subsequence.

"""

def edabit_in_string(txt):
  word="edabit"
  new=""
  c=0
  for i in range(len(word)):
    while True:
      if c>=len(txt):
        return "NO"
      if word[i]==txt[c]:
        new+=txt[c]
        c+=1
        break
      c+=1
  if word==new:
    return "YES"
  else:
    return "NO"

