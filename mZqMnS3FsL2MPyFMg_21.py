"""


Write a function that accepts a positive integer between `0` and `999`
inclusive and returns a string representation of that integer written in
English.

### Examples

    num_to_eng(0) ➞ "zero"
    
    num_to_eng(18) ➞ "eighteen"
    
    num_to_eng(126) ➞ "one hundred twenty six"
    
    num_to_eng(909) ➞ "nine hundred nine"

### Notes

  * There are no hyphens used (e.g. "thirty five" not "thirty-five").
  * The word "and" is not used (e.g. "one hundred one" not "one hundred and one").

"""

def num_to_eng(n):
  z={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',
12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'fourty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',100:'hundred'}
  if(n in z.keys()):
    return z[n]
  else:
    x=1
    ans=''
    nn=n
    while(n>0):
      if(x==1):
        if(n%10!=0):
          ans+=z[n%10]+' '
        x+=1
      elif(x==2):
        x+=1
        if((n%10)!=0 and (n%10)!=1):
          ans=z[(n%10)*10]+' '+ans+' '
        elif((n%10)==1):
          ans=z[(nn%10)+10]+' '
      else: 
        ans=z[n%10]+' '+z[100]+' '+ans+' '
        x+=1
      n=n//10 
    return ans.rstrip()

