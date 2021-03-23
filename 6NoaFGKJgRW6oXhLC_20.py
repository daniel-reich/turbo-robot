"""


Create a function that takes a string and returns the **sum of vowels** ,
where some vowels are considered numbers.

Vowel| Number  
---|---  
A| 4  
E| 3  
I| 1  
O| 0  
U| 0  
  
### Examples

    sum_of_vowels("Let\'s test this function.") ➞ 8
    
    sum_of_vowels("Do I get the correct output?") ➞ 10
    
    sum_of_vowels("I love edabit!") ➞ 12

### Notes

Vowels are case-insensitive ( _e.g. A = 4 and a = 4_ ).

"""

def sum_of_vowels(txt):
    count = 0
    txt = txt.upper()
    for x in txt:
        if x == "A":
            count += 4
        elif x == "E":
            count += 3
        elif x == "I":
            count += 1
        else:
            count += 0
    return count

