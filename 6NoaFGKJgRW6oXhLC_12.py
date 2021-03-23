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

def sum_of_vowels(sentence):
  total = 0
  point = {'a' : 4, 'e' : 3, 'i' : 1, 'o' : 0, 'u' : 0}
  vowels = ['a', 'e', 'i', 'o', 'u']
  sentence = sentence.lower()
  for x in sentence:
    if x in vowels:
      total += point[x]
  return total
