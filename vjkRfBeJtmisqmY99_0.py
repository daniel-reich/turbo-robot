"""


You are given a list of 9 7-letter words. You are also given the middle letter
of one of the 6 of them which fit together in a sort of star pattern as
follows:

Word 1 fits diagonally downwards from left to right. Its 1st letter is the
last letter of word 5; 3rd letter the 5th of word 3;last letter the last
letter of word 4.

Word 2 fits diagonally downwards from left to right. Its 1st letter is the 1st
letter of word 3; 5th letter the 3rd of word 4; last letter the 1st of word 6.

Word 3 fits horizontally from left to right. Its 1st letter is the 1st of word
2; 3rd the 5th of word 5; 5th the 3rd of word 1; last the last of word 6.

Word 4 fits horizontally from left to right. Its 1st letter is the 1st of word
5; 3rd the 5th of word 2; 5th the 3rd of word 6; last the last of word 1.

Word 5 fits diagonally upwards from left to right. Its 1st letter is the 1st
letter of word 4; 5th the 3rd letter of word 3; last the 1st of word 1.

Word 6 fits diagonally upwards from left to right. Its 1st letter is the last
of word 2; 3rd the 5th of word 4; last the last of word 3.

Write a function which takes in a list of 9 7-letter words and number of one
of the words and its middle letter and outputs a list of the 6 words which fit
together as above, ordered as words 1 to 6 as described. For some tests there
may be more than 1 correct answer - any will be accepted.

 **Examples**

fit_words(["crudity", 'reactor', 'grammar', 'bromide', 'aridity', 'airport',
'trilogy', 'rhizome', 'barrier' ](),(3,'d')) --> ['rhizome', 'airport',
'aridity', 'bromide', 'barrier', 'trilogy']()

fit_words(['station', 'freezer', 'sulfate', 'portion', 'trilogy', 'typhoon',
'solvent', 'episode', 'steeple' ](),(3,'e')) --> ['typhoon', 'sulfate',
'steeple', 'station', 'solvent', 'episode']()

 **Notes**

Words are numbered from 1 (so the clue word in each of the examples is the 3rd
word)

Case may be ignored - all test words are lower case.

"""

chain=[[[0,4,-1],[2,2,4],[-1,3,-1]],[[0,2,0],[4,3,2],[-1,5,0]],
        [[0,1,0],[2,4,4],[4,0,2],[-1,5,-1]],[[0,4,0],[2,1,4],[4,5,2],[-1,0,-1]],
  [[0,3,0],[4,2,2],[-1,0,0]],[[0,1,-1],[2,3,4],[-1,2,-1]]]
ansx=[]
​
def fit_words(words, clue):
  global chain,ansx
  for i in [w for w in words if w[len(w)//2]==clue[1]]:
    check(i,words,[[clue[0]-1,i]],clue[0]-1)
  mem,ansx=ansx,[]
  return mem[0] if len(mem)==1 else mem
​
def check(word,pool,res,con):
  global chain,ansx
  pool.remove(word);
  dic={i:w for i,w in res};n=-2
  while all([i[1] in dic and dic[i[1]][i[2]]==word[i[0]] for i in chain[con]]):
    try:con,word=res[n];n-=1
    except:
      mem = [w for i,w in sorted(res,key = lambda x:x[0])]
      if mem not in ansx:ansx+=[mem]
      break
  for i in chain[con]:
    if i[1] in dic and dic[i[1]][i[2]]!=word[i[0]]:break
    elif i[1] in dic:pass
    else:
      memw = [w for w in pool if w[i[2]]==word[i[0]]]
      if not memw:break
      for j in memw:check(j,pool[:],res[:]+[[i[1],j]],i[1])

