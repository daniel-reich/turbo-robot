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

import string
​
months = { "1": "A", "2": "B", "3": "C", "4": "D", "5": "E", "6": "H",
"7": "L", "8": "M", "9": "P", "10": "R", "11": "S", "12": "T" }
​
vowels = set('AEIOU')
consonants = set(string.ascii_uppercase) - vowels
​
​
def get_consonants_vowels(word):
    return ''.join(filter(lambda x: x in consonants, word.upper())), ''.join(filter(lambda x: x in vowels, word.upper()))
​
​
def handle_surname(surname):
    surname_c, surname_v = get_consonants_vowels(surname)
    
    code = surname_c[:3]
    
    if len(code) < 3:
        code += surname_v[:3 - len(code)]
    
    while len(code) < 3:
        code += 'X'
    
    return code
​
​
def handle_name(name):
    name_c, name_v = get_consonants_vowels(name)
    
    if len(name_c) > 3:
        return name_c[0] + name_c[2:4]
    elif len(name_c) == 3:
        return name_c
    elif len(name_c) < 3:
        code = name_c + name_v[:3 - len(name_c)]
        
        while len(code) < 3:
            code += 'X'
        
        return code
​
​
def handle_dob_gender(dob, gender):
    dob_lst = dob.split('/')
    code = dob_lst[2][-2:]
    code += months[dob_lst[1]]
    day = int(dob_lst[0]) if gender == 'M' else int(dob_lst[0]) + 40
    day = str(day) if day >= 10 else '0' + str(day)
    return code + day
    
​
def fiscal_code(person):
    code = handle_surname(person['surname'])
    code += handle_name(person['name'])
    code += handle_dob_gender(person['dob'], person['gender'])
    
    return code

