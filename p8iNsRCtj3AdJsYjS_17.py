"""
Given a column title as it appears in an Excel sheet return its corresponding
column number.

The number is computed in the following way:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...

### Examples

    title_to_number("A") ➞ 1
    
    title_to_number("R") ➞ 18
    
    title_to_number("AB") ➞ 28

### Notes

  * `1 <= len(s) <= 7`
  * `s` consists only of uppercase English letters.

"""

def title_to_number(column_title):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    column_number = 0
    for index, character in enumerate(column_title[::-1]):
        position = alphabet.find(character) + 1
        column_number += position * (26 ** index)
    return column_number

