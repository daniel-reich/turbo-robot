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
  d = ['C#',
  'C++',
  'Java',
  'JavaScript',
  'PHP',
  'Python',
  'Ruby',
  'Swift']
  s = list(bin(num)[2:])
  s.reverse()
  langs = []
  for i in range(len(s)):
    if s[i] == '1':
      langs.append(d[i])
  return langs

