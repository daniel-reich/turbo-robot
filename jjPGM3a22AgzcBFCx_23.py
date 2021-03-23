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
  normal = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
  alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
  number = list(set(normal) - set(lst))
  return alphabet[number[0] - 1]

