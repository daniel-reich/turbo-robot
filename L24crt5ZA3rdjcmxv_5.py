"""
Each person in Italy has an unique identifying ID code issued by the national
tax office after the birth registration: the Fiscal Code ( _Codice Fiscale_ ).
Check the **Resources** tab for more info on this.

Given a dictionary containing the personal data of a person (name, surname,
gender and date of birth) return the 11 code characters as a string following
these steps:

  * Generate 3 capital letters from the **surname** , if it has:

    * At least 3 consonants then the first three consonants are used. ( _Newman - > NWM_).
    * Less than 3 consonants then vowels will replace missing characters in the same order they appear ( _Fox - > FXO | Hope -> HPO_).
    * Less than three letters then "X" will take the third slot after the consonant and the vowel ( _Yu - > YUX_).
  * Generate 3 capital letters from the **name** , if it has:

    * Exactly 3 consonants then consonants are used in the order they appear ( _Matt - > MTT_).
    * More than 3 consonants then first, third and fourth consonant are used ( _Samantha - > SNT | Thomas -> TMS_).
    * Less than 3 consonants then vowels will replace missing characters in the same order they appear ( _Bob - > BBO | Paula -> PLA_).
    * Less than three letters then "X" will take the the third slot after the consonant and the vowel ( _Al - > LAX_).
  * Generate 2 numbers, 1 letter and 2 numbers from **date of birth** and **gender** :

    * Take the last two digits of the year of birth ( _1985 - > 85_).
    * Generate a letter corresponding to the month of birth ( _January - > A | December -> T_) using the table for conversion included in the code.
    * For males take the day of birth adding one zero at the start if is less than 10 ( _any 9th day - > 09 | any 20th day -> 20_).
    * For females take the day of birth and sum 40 to it ( _any 9th day - > 49 | any 20th day -> 60_).

### Examples

    fiscal_code({
      "name": "Matt",
      "surname": "Edabit",
      "gender": "M",
      "dob": "1/1/1900"
    }) ➞ "DBTMTT00A01"
    
    fiscal_code({ 
      "name": "Helen",
      "surname": "Yu",
      "gender": "F",
      "dob": "1/12/1950"
    }) ➞ "YUXHLN50T41"
    
    fiscal_code({
      "name": "Mickey",
      "surname": "Mouse",
      "gender": "M",
      "dob": "16/1/1928"
    }) ➞ "MSOMKY28A16"

### Notes

  * Code letters must be uppercase.
  * Date of birth is given in D/M/YYYY format.
  * The conversion table for months is already in the starting code.
  * Y is not a vowel.

"""

months = { "1": "A", "2": "B", "3": "C", "4": "D", "5": "E", "6": "H",
"7": "L", "8": "M", "9": "P", "10": "R", "11": "S", "12": "T" }
​
def fiscal_code(person):
  def surname_coder(surname):
    vowels = 'A, E, I, O, U'.split(', ')
​
    cosonants_in_surname = []
​
    for l8r in surname:
      l8r = l8r.upper()
​
      if l8r not in vowels:
        cosonants_in_surname.append(l8r)
    
    l = len(cosonants_in_surname)
​
    coded = []
​
    if l >= 3:
      coded = cosonants_in_surname[:3]
    elif l < 3:
      for l8r in surname:
        l8r = l8r.upper()
​
        if l8r in vowels:
          cosonants_in_surname.append(l8r)
      
      ln = len(cosonants_in_surname)
​
      if ln >= 3:
        coded = cosonants_in_surname[:3]
      else:
​
        while ln < 3:
          cosonants_in_surname.append('X')
          ln = len(cosonants_in_surname)
        
        coded = cosonants_in_surname
    
    return coded
  def name_coder(name):
​
    vowels = 'a, e, i, o, u'.upper().split(', ')
​
    cosonants_in_name = []
​
    for l8r in name:
      l8r = l8r.upper()
​
      if l8r not in vowels:
        cosonants_in_name.append(l8r)
    
    l = len(cosonants_in_name)
    
    coded = []
    if l == 3:
      coded = cosonants_in_name
      print('coded')
​
    elif l > 3:
      coded = [cosonants_in_name[0], cosonants_in_name[2], cosonants_in_name[3]]
      print('moth')
​
    elif l < 3:
      nl = len(name)
      if nl >= 3:
        for l8r in name:
          l8r = l8r.upper()
​
          if l8r in vowels:
            cosonants_in_name.append(l8r)
        
        coded = cosonants_in_name
      elif nl < 3:
        print('hi')
        for l8r in name:
          l8r = l8r.upper()
​
          if l8r in vowels:
            cosonants_in_name.append(l8r)
          
        nl = len(cosonants_in_name)
​
        while nl < 3:
          cosonants_in_name.append('X')
          nl = len(cosonants_in_name)
        
        coded = cosonants_in_name
    
    
    return coded
  def dateofbirth_coder(dob, g):
    dob = dob.split('/')
​
    day = int(dob[0])
    month = dob[1]
    year = list(dob[2])
​
    months = { "1": "A", "2": "B", "3": "C", "4": "D", "5": "E", "6": "H", "7": "L", "8": "M", "9": "P", "10": "R", "11": "S", "12": "T" }
​
    ycode= '{y2}{y1}'.format(y2 = year[-2], y1 = year[-1])
    mcode = months[month]
​
    dcode = ''
    if g == 'M':
      if day < 10:
        dcode = '0' + str(day)
      else:
        dcode = str(day)
    elif g == 'F':
      dcode = str(day + 40)
​
    code = '{yc}{mc}{dc}'.format(yc = ycode, mc = mcode, dc = dcode)
​
    return code
  
  surname = person['surname']
  sc = surname_coder(surname)
  
  name = person['name']
  nc = name_coder(name)
  if len(nc) > 3:
    nc = nc[:3]
  gender = person['gender']
  dob = person['dob']
​
  dobcode = dateofbirth_coder(dob, gender)
​
  code = ''
​
  for item in sc:
    code += item
  for item in nc:
    code += item
  code += dobcode
​
  return code

