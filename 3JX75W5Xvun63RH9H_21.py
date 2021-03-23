"""


Given a number `n`, return a sentence which describes the number in the
following ways.

  * Always start the string with **"The most"**.
  * If `n` is evenly divisible by 1, add **"brilliant"** to the sentence.
  * If `n` is evenly divisble by 2, add **"exciting"** to the sentence.
  * ... 3, add **"fantastic"** to the sentence.
  * ... 4, add **"virtuous"** to the sentence.
  * ... 5, add **"heart-warming"** ...
  * ... 6, add **"tear-jerking"** ...
  * ... 7, add **"beautiful"** ...
  * ... 8, add **"exhilarating"** ...
  * ... 9, add **"emotional"** ...
  * If `n` is evenly divisible by 10, add **inspiring** to the sentence.
  * Always end the string with **"number is"** `n`!

### Examples

    describe_num(13) ➞ "The most brilliant number is 13!"
    # 13 is evenly divisble by 1 only
    
    describe_num(4) ➞ "The most brilliant exciting virtuous number is 4!"
    # 4 is evenly divisible by 1, 2 and 4
    
    describe_num(21) ➞ "The most brilliant fantastic beautiful number is 21!"
    # 21 is evenly divisible by 1, 3 and 7
    
    describe_num(60) ➞ "The most brilliant exciting fantastic virtuous heart-warming tear-jerking inspiring number is 60!"
    # 60 is evenly divisible by 1, 2, 3, 4, 5, 6 and 10

### Notes

  * Add words to the sentence in the order going down the list.
  *  **BONUS:** Try to find the lowest number which uses all possible words in the sentence!

"""

def describe_num(n):
  l = ""
  
  if n%1==0:
    l+="brilliant"
    l+=" "
  if n%2==0:
    l+="exciting"
    l+=" "
  if n%3==0:
    l+="fantastic"
    l+=" "
  if n%4==0:
    l+="virtuous"
    l+=" "
  if n%5==0:
    l+="heart-warming"
    l+=" "
  if n%6==0:
    l+="tear-jerking"
    l+=" "
  if n%7==0:
    l+="beautiful"
    l+=" "
  if n%8==0:
    l+="exhilarating"
    l+=" "
  if n%9==0:
    l+="emotional"
    l+=" "
  if n%10==0:
    l+="inspiring"
    l+=" "
  txt="number is {}"
  x = txt.format(n)
  return "The most"+" "+''.join(l)+x+"!"

