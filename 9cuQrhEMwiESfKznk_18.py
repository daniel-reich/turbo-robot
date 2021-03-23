"""


This is a companion to my [previous
challenge](https://edabit.com/challenge/mZqMnS3FsL2MPyFMg).

Given an English description of an integer in the range **0 to 999** , devise
a function that returns the integer in numeric form.

### Examples

    eng2nums("four") ➞  4
    
    eng2nums("forty") ➞ 40
    
    eng2nums("six hundred") ➞ 600
    
    eng2nums("one hundred fifteen") ➞ 115
    
    eng2nums("seven hundred sixty seven") ➞ 767

### Notes

  * No hyphens are used in test cases ("twenty three" not "twenty-three").
  * The word "and" is not used: "one hundred three" not "one hundred and three".

"""

def eng2nums(s):
  s = str(s)
  numbers = {'0': 'zero','1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
  exceptions = {'10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen', '15': 'fifteen', '16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineteen'}
  tens = {'2': 'twenty', '3': 'thirty', '4': 'fourty', '5': 'fifty', '6': 'sixty', '7': 'seventy', '8': 'eighty', '9': 'ninety'}
  
  bases = {'one hundred': 100, 'two hundred': 200, 'three hundred': 300, 'four hundred': 400, 'five hundred': 500, 'six hundred': 600, 'seven hundred': 700, 'eight hundred': 800, 'nine hundred': 900}
  
  if s in bases:
    return bases[s]
  
  list_of_exceptions = [exceptions[x] for x in exceptions.keys()]
  corresponding_exceptions = [x for x in exceptions]
  
  list_of_tens = [tens[x] for x in tens.keys()]
  corresponding_tens = [x for x in tens]
  
  list_of_numbers = [numbers[x] for x in numbers.keys()]
  corresponding_numbers = [x for x in numbers]
  
  if s in list_of_exceptions:
    return int(corresponding_exceptions[list_of_exceptions.index(s)])
  
  x = s.split(' ')
  emptystring = ''
  if x[0] in list_of_exceptions:
    return int(corresponding_exceptions[list_of_exceptions.index(x)])
  elif len(x) > 1:
    for eachpart in x:
      if eachpart in list_of_tens:
        if eachpart == x[-1]:
          emptystring += corresponding_tens[list_of_tens.index(eachpart)] + '0'
        else:
          emptystring += corresponding_tens[list_of_tens.index(eachpart)]
      elif eachpart in list_of_numbers:
        if eachpart == x[-1] and len(x) == 3 and 'hundred' in s:
          emptystring += '0' + corresponding_numbers[list_of_numbers.index(eachpart)]
        else:
          emptystring += corresponding_numbers[list_of_numbers.index(eachpart)]
      elif eachpart in list_of_exceptions:
        emptystring += corresponding_exceptions[list_of_exceptions.index(eachpart)]
    print(emptystring)
    return int(emptystring)
  elif len(x) == 1:
    if x[0] in list_of_numbers:
      return int(corresponding_numbers[list_of_numbers.index(x[0])])
    else:
      return int(corresponding_tens[list_of_tens.index(x[0])] + '0')
  if len(s) == 3:
    first_digit = s[0]
    second_digit = s[1]
    last_digit = s[2]
    exception = s[1:3]
    if int(exception) >= 10 and int(exception) < 20:
      return numbers[first_digit] + ' hundred ' + exceptions[exception]
    else:
      return numbers[first_digit] + ' hundred ' + tens[second_digit] + ' ' + numbers[last_digit]
  elif len(s) == 2:
    if int(s) >= 10 and int(s) < 20:
      return exceptions[s]
    else:
      first_digit = s[0]
      last_digit = s[1]
      return tens[first_digit] + ' ' + numbers[last_digit]
  else:
    return numbers[s]

