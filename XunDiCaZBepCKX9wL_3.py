"""


This string, `"sadbpstcrdvaefikkgoenqrt"` has a five letter word embedded
within it.

Here's a clue on how to find it:

  1. The `string` can be broken up from left to right into a series of overlapping letter triplets.
  2. The letter values for each triplet are summed with a=1, b=2, ..., z=26.
  3. The values of the triplets that contain the letters of the secret word as the middle member form an increasing arithmetic series.

Given the `string` and `length` of the secret word, improvise a function that
finds the secret word.

### Examples

    secret_word("sadbpstcrdvaefikkgoenqrt", 5) ➞ "brake"
    # sa(dbp)st(crd)(vae)f(ikk)g(oen)qrt
    # The values of the triplets in parentheses are 22, 25, 28, 31, 34.
    # An arithmetic series with difference of 3.
    
    secret_word("aheiayd", 3) ➞ "hey"
    # (a[he)i](ayd)
    # The triplets with the secret letters can overlap.
    # ahe=14, hei=22, ayd=30; a series with a difference of 8.

### Notes

N/A

"""

def secret_word(s,length):
    d=[]
    for i in range(len(s)-2):
        d.append(sum(ord(s[i+k])-96 for k in range(3)))
    for i in range(len(d)):
        for x in range(1,76):
            count=1
            ans=[i+1] 
            for y in range(i+1,len(d)):    
                if d[i]+count*x==d[y]:
                    count+=1
                    ans.append(y+1)
                    if count==length:
                        return ''.join([s[i] for i in ans])

