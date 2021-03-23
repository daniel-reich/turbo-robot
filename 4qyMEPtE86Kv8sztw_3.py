"""


Adding fractional binary numbers is similar to adding decimals. The places to
the right of the decimal point (or binary point) are halves, quarters, eighths
instead of tenths, hundredths, thousandths, etc.

Improvise a function that takes two fractional binary numbers and produces
their base-10 sum. The sum can be a whole number, a fraction, or a mixed
number. The answer should be returned as a string with fractions reduced to
lowest terms.

### Examples

    binary_sum(["1.1", "1.1"]) ➞ "3"
    # 1.5 + 1.5
    
    binary_sum(["11.1", "0.001"]) ➞ "3 5/8"
    # 3.5 + 0.125
    
    binary_sum(["1101.0", "0.0100"]) ➞ "13 1/4"
    # 13 + 1/4
    
    binary_sum(["0.11", "0.00001"]) ➞ "25/32"
    # 3/4 + 1/32
    
    binary_sum(["0.0", "101.00"]) ➞ "5"

### Notes

N/A

"""

def fractionizer (fraction):
  result,temp,denominators,i= 0,fraction,[],1
  while not round(result,len(str(fraction))-2) == fraction:
    if result+1/(2**i)<= fraction:
      denominators.append(2**i)
      result+=1/(2**i)
      temp-=result
    i+=1
  return denominators
​
def binary_sum(lst):
  first,second=[0,0],[0,0]
  first[0],first[1]=lst[0].split('.')[0],lst[0].split('.')[1]
  second[0],second[1]=lst[1].split('.')[0],lst[1].split('.')[1]
  whole =sum([2**(len(first[0])-1-i) for i in range (len(first[0])) if first[0][i]=='1'])+\
  sum([2**(len(second[0])-1-i) for i in range (len(second[0])) if second[0][i]=='1'])
  fraction= sum([2**(-i-1) for i in range (len(first[1])) if first[1][i]=='1'])+\
  sum([2**(-i-1)  for i in range (len(second[1])) if second[1][i]=='1'])
  if fraction>=1:
    whole,fraction=whole+1,fraction-1
  if fraction == 0:
    return str(whole)
  denominators=fractionizer (fraction)
  lcd=max(denominators)
  numerator=0
  for i in range(len(denominators)):
    numerator+=lcd//denominators[i]
  return str(whole) + ' ' + str(numerator) + '/' + str(lcd) if whole >0 else str(numerator) + '/' + str(lcd)

