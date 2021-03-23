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

import re
def fiscal_code(person):
    months = { "1": "A", "2": "B", "3": "C", "4": "D", "5": "E", "6": "H",
            "7": "L", "8": "M", "9": "P", "10": "R", "11": "S", "12": "T" }
​
    def Code(name,type="surname"):
        
        c_in_names= re.sub('[aeiou]', '', name.lower())
        w_in_names= re.sub('[bcdfghjklmnpqrstvwxyz]', '', name.lower())
        
        if len(name)>2:
            if len(c_in_names) > 3 and type=="name":
                #output=c_in_names[0]+c_in_names[4:6]
                output=c_in_names[0]+c_in_names[2:4]
                
​
            if len(c_in_names) > 3 and type=="surname":
                output=c_in_names[0:3]
            
            if len(c_in_names) == 3:
                output=c_in_names        
            
            if len(c_in_names) == 2:
                output =c_in_names+w_in_names[0:1]
​
            if len(c_in_names) == 1:
                output =c_in_names+w_in_names[0:2]
            
            if len(c_in_names) == 0:
                output =w_in_names[0:3]
        
        if len(name)==2:
            if len(c_in_names[0:2]) == 2:
                output=c_in_names[0:2]+"X"
        
            if len(c_in_names[0:2]) == 1:
                output =c_in_names[0:1]+w_in_names[0:1]+"X"
​
            if len(c_in_names[0:3]) == 0:
                output =w_in_names[0:2]+"X"
​
        if len(name)==1:
            if len(c_in_names[0:1]) == 1:
                output=c_in_names[0:2]+"XX"
        
            if len(c_in_names[0:3]) == 0:
                output =w_in_names[0:1]+"XX"
            
        return output
​
    c_code=Code(person["name"],type="name").upper()
    s_code=Code(person["surname"]).upper()
​
    y=person["dob"].split("/")[2][2:4]
    m=months[person["dob"].split("/")[1]]
​
    if person["gender"] == "M":
        if int(person["dob"].split("/")[0]) < 10:
            d="0"+ person["dob"].split("/")[0] 
        else:
            d=person["dob"].split("/")[0] 
    else:
        d=int(person["dob"].split("/")[0])+40
​
​
    return s_code+c_code+str(y)+str(m)+str(d)

