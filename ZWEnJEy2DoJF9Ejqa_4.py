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
  edabit = list("edabit")
  holder = []
  counter = 0
  for char in range(len(txt)):
    if txt[char] == edabit[counter]:
        holder.append(txt[char])
        counter +=1
    if counter == len(edabit):
        break
  return "YES" if holder == edabit else "NO"

