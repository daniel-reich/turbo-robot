"""


6174 is known as one of Kaprekar's constants, after the Indian mathematician
D. R. Kaprekar. Number 6174 is notable for the following rule:

  * Take any four-digit number, using at least two different digits (leading zeros are allowed).
  * Arrange the digits in descending and then in ascending order to get two four-digit numbers, adding leading zeros if necessary.
  * Subtract the smaller number from the bigger number.
  * Go back to step 2 and repeat.

The above process, known as Kaprekar's routine, will always reach its fixed
point, 6174, in at most 7 iterations. Once 6174 is reached, the process will
continue yielding 7641 – 1467 = 6174. For example, choose 3524:

    5432 – 2345 = 3087
    8730 – 0378 = 8352
    8532 – 2358 = 6174
    7641 – 1467 = 6174

Write a recursive function that will return the number of times it will take
to get from a number to 6174 (the above example would equal 3).

    (1)5432 – 2345 = 3087,
    (2)8730 – 0378 = 8352,
    (3)8532 – 2358 = 6174

495 would produce the following: 4950 to 9540 - 459, 9081 to 9810 - 189, 9621
to 9621 - 1269, 8352 to 8532 - 2358 answer: 4

For a 2 digit number, the following would be produced (stating with number 10
-> 100):

100 to 100 - 1, 990 to 990 - 99, 8910 to 9810 - 189, 9621 to 9621 - 1269, 8352
to 8532 - 2358 answer: 5

### Examples

    kaprekar(6621) ➞ 5
    
    kaprekar(6554) ➞ 4
    
    kaprekar(1234) ➞ 3

### Notes

If the subtracted number is less than 1000, add an extra zero to that number.
The number 1111 will equal 0000, so this number (1111) is invalid. If you're
still unclear, please check the comments section.

"""

def getNumbers_list(num): 
    #This function will return the descending order of the numbers in a sequence 
    numList = [] 
    for _n in str(num): 
        numList.append(int(_n)) 
    return numList 
def minus(firstNum,secondNum): 
    diff = [] 
    for i in range(len(firstNum)): 
        diff.append(firstNum[i] - secondNum[i])
    return diff 
​
def convertListToNum(minusNums): 
    num = "" 
    for _mNums in minusNums: 
        num += str(_mNums) 
    return int(num)
def addExtraZero(diff): 
    #This function will add an extra zero to the number 
    return int('0' + str(diff))
def kaprekar(num,counter=1 ): 
    if num == 6174: 
        return 0 
    if num < 1000: 
        num *= 10
    smallNumber = convertListToNum(sorted(getNumbers_list(num)))
    bigNumber = convertListToNum(sorted(getNumbers_list(num),reverse = True))
    diff =bigNumber - smallNumber 
    #if diff < 1000: 
        #diff = addExtraZero(diff)
    
    if diff == 6174: 
        print(counter)
        return counter
    
    else:
        counter += 1
        return kaprekar(diff,counter)

