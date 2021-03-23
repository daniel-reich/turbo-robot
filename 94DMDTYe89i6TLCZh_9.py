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
  lg = {
    1  :    'C#',
    2  :    'C++',
    4  :    'Java',
    8  :    'JavaScript',
    16 :    'PHP',
    32 :    'Python',
    64 :    'Ruby',
    128:    'Swift'
  }
  s = bin(num)[2:][::-1]
  l_out = []
  for i in range(len(s)):
    if s[i] == '1':
      l_out.append(lg[2**i])
  return l_out

