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
  if n == 0:
    return 'zero'
  ones = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
  tens = {2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}
  teens = {10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',
        18:'eighteen',19:'nineteen'}
  n_str = str(n)
  lst = []
  for i in range(len(n_str),0,-1):
    index = -1 * i
    num = int(n_str[index])
    if num==0:
      continue
    if index==-3:
      lst.append(ones[num]+' hundred')
    elif index==-2:
      if num == 1:
        num = int(n_str[index]+n_str[index+1])
        lst.append(teens[num])
        break
      else:
        lst.append(tens[num])
    else:
      lst.append(ones[num])
  ans = ' '.join(lst)
  return ans

