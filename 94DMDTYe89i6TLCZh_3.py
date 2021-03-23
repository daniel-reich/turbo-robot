"""


Create a function that takes a number that represents a person's programming
language score, and returns an alphabetised list of programming languages they
are proficient in. Arbitrarily assigned points for each language are listed
below:

Language| Points  
---|---  
C#| 1  
C++| 2  
Java| 4  
JavaScript| 8  
PHP| 16  
Python| 32  
Ruby| 64  
Swift| 128  
  
### Examples

    get_languages(25) ➞ ["C#", "JavaScript", "PHP"]
    
    get_languages(100) ➞ ["Java", "Python", "Ruby"]
    
    get_languages(53) ➞ ["C#", "Java", "PHP", "Python"]

### Notes

Easier using bitwise operations.

"""

def get_languages(num):
  languages = ["C#", "C++", "Java", "JavaScript", "PHP", "Python", "Ruby", "Swift"]
  proficient = []
  for language in languages[::-1]:
    if 2 ** languages.index(language) <= num:
      proficient.append(language)
      num -= 2 ** languages.index(language)
    if num < 0:
      proficient.pop()
      break
  return sorted(proficient)

