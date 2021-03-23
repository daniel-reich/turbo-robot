"""


Create a function that takes a string (without spaces) and a word list,
cleaves the string into words based on the list, and returns the correctly
spaced version of the string (a sentence). If a section of the string is
encountered that can't be found on the word list, return `"Cleaving stalled:
Word not found"`.

### Examples

    word_list = ["about", "be", "hell", "if", "is", "it", "me", "other", "outer", "people", "the", "to", "up", "where"]
    cleave("ifitistobeitisuptome", word_list) ➞ "if it is to be it is up to me"
    
    cleave("hellisotherpeople", word_list) ➞ "hell is other people"
    
    cleave("hellisotterpeople", word_list) ➞ "Cleaving stalled: Word not found"

### Notes

Words on the `word_list` can appear more than once in the string. The
`word_list` is a reference guide, kind of like a dictionary that lists which
words are allowed.

"""

def cleave(string, lst):
       #Make list of possible words (pw) from lst in string
       pw=[]
       for x in lst:
              if x in string:
                     pw.append(x)
       #Count how many times each word appear in string
       count=[]
       for x in pw:
              a=string.count(x)
              count.append(a)
       #Make list of pw*count
       nl=''
       for x in range(0,len(pw)):
              nl+=(pw[x]+' ')*count[x]
       nl=nl.split()
       #Make list of start index of nl
       s=[]
       for x in pw:
              temp=string
              while x in temp:
                     s.append(temp.index(x))
                     temp=temp.replace(x,(' '*len(x)),1)
       #Make list of end index of nl
       e=[]
       for x in range(0,len(nl)):
              e.append(s[x]+len(nl[x]))
       #make final list (fl) with index (flI)
       fl=[]
       flI=[]
       for x in range(0,len(nl)):
              if (s[x]==0 or s[x] in e) and (e[x]==len(string) or e[x] in s):
                     fl.append(nl[x])
                     flI.append(s[x])
       #Zip lists
       L=list(zip(fl,flI))
       
       #Sort list
       from operator import itemgetter
       L
       x=sorted(L, key=itemgetter(1))
​
       #Get output
       o=''
       test=''
       for y in range(0,len(x)):
              o+=str(x[y][0])+' '
              test+=str(x[y][0])
       #if not in list
       if test == string:
              return o.strip()
       else:
              return "Cleaving stalled: Word not found"

