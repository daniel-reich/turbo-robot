"""


Create a function that takes a dict with the size, the weight in kg, the age,
how much sport the person does and whether the person is male or female:

    dict = {
      "gender": "male",
      "height": 180,
      "weight": 80,
      "age": 20,
      "sport": 3
    }

Return the basal metabolic rate of the person rounded to one decimal place.
The formula is:

  * BMR for Men: 66.47 + (13.75 _weight) + (5.003_ height) − (6.755 * age)
  * BMR for Women: 655.1 + (9.563 _weight) + (1.85_ height) − (4.676 * age)

Once you’ve calculated your BMR, this is then put into the Harris Benedict
Formula , which calculates your total calorie intake required to maintain your
current weight. This is as follows:

  * Little/no exercise( **1** ): BMR * 1.2 = Total Calorie Need
  * Light exercise( **2** ): BMR * 1.375 = Total Calorie Need
  * Moderate exercise ( **3** ): BMR * 1.55 = Total Calorie Need
  * Very active ( **4** ): BMR * 1.725 = Total Calorie Need
  * Extra active ( **5** ): BMR * 1.9 = Total Calorie Need

### Examples

    BMR({
      "gender": "female",
      "height": 170,
      "weight": 65,
      "age": 25,
      "sport": 5
    }) ➞ 2801.2
    BMR({
      "gender": "male",
      "height": 180,
      "weight": 80,
      "age": 20,
      "sport": 3
    }) ➞ 2994.5
    BMR({
      "gender": "female",
      "height": 170,
      "weight": 70,
      "age": 40,
      "sport": 2
    }) ➞ 1996.5

### Notes

N/A

"""

def BMR(person):
    weight =person['weight']
    height =person['height']
    age = person['age']
    m= weight*13.75 + 66.47 + 5.003*height - age*6.755
    w = weight*9.563 + 655.1 + 1.85*height - age*4.676
    ans =m if person['gender']=='male' else w
    obj ={1:ans*1.2,2:ans*1.375,3:ans*1.55,4:ans*1.725,5:ans*1.9,}
    return round(obj[person['sport']], 1)

