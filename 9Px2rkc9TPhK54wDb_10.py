"""


In the ECG Sequence (that always starts with the numbers 1 and 2), every
number that succeeds is the smallest not already present in the sequence and
that shares a factor (excluding 1) with its preceding number. Every number in
the ECG Sequence (besides 1 and 2) has a different index from its natural
index in a normal numeric sequence. See the example below to establish the ECG
Sequence Index of number 3.

    # Find the smallest number that is not in sequence...
    # This number shares a factor with the preceding?
    
    SEQUENCE = [1, 2]
    
    3 = no factors shared with 2
    4 = shares factor 2 with number 2
    
    SEQUENCE = [1, 2, 4]
    
    3 = no factors shared with 4
    5 = no factors shared with 4
    6 = shares factor 2 with number 4
    
    SEQUENCE = [1, 2, 4, 6]
    
    3 = shares factor 3 with number 6
    
    SEQUENCE = [1, 2, 4, 6, 3]
    
    Number 3 is at index 4 in the ECG Sequence.

Given an integer `n` implement a function that returns its ECG Sequence Index.

### Examples

    ecg_seq_index(3) ➞ 4
    
    ecg_seq_index(5) ➞ 9
    
    ecg_seq_index(7) ➞ 13

### Notes

  * ECG is the acronym for the electrocardiogram: if you try to graphically represent the trend of the sequence, a similar scheme appears.
  * Curiosity: every odd prime `p` in the sequence is preceded by `2p` and followed by `3p`.

"""

s=[1,2]
​
def ecg_seq_index(n):
  global s
  while not n in s:
    fx=set(factor(s[-1]));x=1;mem=s[-1];mcof=n**2
    while mem==s[-1]:
      mem2=set(i for i in fx if not x*i in s)
      mcof=min([x*i for i in mem2]+[mcof]);fx-=mem2
      if not fx or min(fx)*x>mcof:s+=[mcof]
      x+=1
  return s.index(n)
  
def factor(num):
  res=[];i=2
  while num!=1:
    while not num%i:
      res+=[i]
      num//=i
    i+=1
  return res

