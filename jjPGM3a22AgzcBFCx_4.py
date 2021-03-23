"""


Our fleet managed to get one of the enemy's top-secret codes from the remains
of its fallen ship. The codes were immediately sent over to our code-breaking
base over at **Bleckley Park** ;) for analysis. The team found that each code
contains 25 numbers with one missing. The missing number corresponds to a
letter in the English alphabet. Your job is to find a more efficient Method of
decrypting the messages by `digitizing` the process.

Write a function that takes a list, detects the missing number (in the list),
and returns its **corresponding letter**.

### Examples

    decrypt(24, 12, 2, ..., 25) ➞ "N"
    # The missing number is 14.
    
    decrypt(24, 12, 2, ..., 25) ➞ "O"
    # The missing number is 15.
    
    decrypt(24, 12, 2, ..., 25) ➞ "P"
    # The missing number is 16.

### Notes

  * The list will only contain positive integers from 1 to 26 with one missing.
  * There will be no duplicate numbers.
  * Return the **capital** letter.

"""

def decrypt(lst):
  numToLetter = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",10:"J",11:"K",12:"L",13:"M",14:"N",15:"O",16:"P",17:"Q",18:"R",19:"S",20:"T",21:"U",22:"V",23:"W",24:"X",25:"Y",26:"Z"}
  for i in range(1,27):
    if not i in lst:
      return numToLetter[i]

