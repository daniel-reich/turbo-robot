"""


Given a string containing digits from `2-9` inclusive, return all possible
letter combinations that the number could represent. A mapping of digit to
letters (just like on the telephone buttons) is given below. Note that 1 does
not map to any letters.

![Alternative Text](https://edabit-challenges.s3.amazonaws.com/200px-
Telephone-keypad2.svg.png)

### Examples

    letter_combinations("23") ➞ ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    
    letter_combinations("532") ➞ ["jda", "jdb", "jdc", "jea", "jeb", "jec", "jfa", "jfb", "jfc", "kda", "kdb", "kdc", "kea", "keb", "kec", "kfa", "kfb", "kfc", "lda", "ldb", "ldc", "lea", "leb", "lec", "lfa", "lfb", "lfc"]

### Notes

N/A

"""

def letter_combinations(digits):
  def plc(dgts):
    dic = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
    
​
    d = str(dgts)
​
    if len(d) == 3:
      poss = []
​
      firstlen = len(dic[d[0]])
      seconlen = len(dic[d[1]])
      thirdlen = len(dic[d[2]])
​
      
      possible_backs = []
      for n in range(3):
        for num in range(3):
          possible_backs.append(''.join([dic[d[1]][n], dic[d[2]][num]]))
     
      possible_backs = list(set(possible_backs))
      if firstlen == 4:
        for n in range(4):
          for back in possible_backs:
            poss.append(dic[d[0]][n] + back)
      else:
        
        for n in range(3):
          for back in possible_backs:
            poss.append(dic[d[0]][n] + back)
    
    elif len(d) == 2:
      poss = []
​
      for n in range(3):
        for num in range(3):
          poss.append(dic[d[0]][num] + dic[d[1]][n])
​
    return poss
  combs = plc(digits)
​
  return sorted(combs)

