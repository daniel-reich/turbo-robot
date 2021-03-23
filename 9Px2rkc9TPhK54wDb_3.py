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

def share(x,y):
    if x>y:
        for i in range(2,y+1):
            if x%i==0 and y%i==0:
                return True
        return False
    else:
        for i in range(2,x+1):
            if x%i==0 and y%i==0:
                return True
        return False
        
    
print(share(4,3)) 
def ecg_seq_index(x):
    s=[1,2]
    data=3
    while True:
        
        if x in s:
            return s.index(x)
        elif share(s[-1],data):
            if data not in s:
                s.append(data)
                data=3
            else:
                data+=1
        else:
            data+=1

