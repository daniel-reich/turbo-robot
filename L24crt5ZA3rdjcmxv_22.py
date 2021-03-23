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
vowels="aeiou"
def get_vowels(x):
    return [n for n in x if n in vowels]
def get_consonants(x):
    return [n for n in x if n not in vowels]
def fiscal_code(person):
    code=""
    name=person["surname"].lower()
    v=get_vowels(name)
    c=get_consonants(name)
    if len(c)>=3:
        code+="".join(c[:3])
    elif len(name)>2:
        code+="".join(c)+"".join(v[:3-len(c)])
    else:
        code+="".join(c)+"".join(v)+"X"
    name=person["name"].lower()
    v=get_vowels(name)
    c=get_consonants(name)    
    if len(c)==3:
        code+="".join(c)
    elif len(c)>3:
        code+=c[0]+c[2]+c[3]
    elif len(name)>2:
        code+="".join(c)+"".join(v[:3-len(c)])
    else:
        code+="".join(c)+"".join(v)+"X"
    
    dob=person["dob"]
    code+=dob[-2:]
    dobs=dob.split("/")
    code+=months[dobs[1]]
    if person["gender"]=="M":
        if len(dobs[0])==1:
            code+="0"+dobs[0] 
        else: code+=dobs[0]
    else: 
        code+=str(int(dobs[0])+40)
    
    
    return code.upper()

