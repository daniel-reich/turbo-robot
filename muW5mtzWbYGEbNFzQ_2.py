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

def BMR(p):
  f1 = {"male": [66.47, 13.75, 5.003, 6.755], "female": [655.1, 9.563, 1.85, 4.676]}[p["gender"]]
  f2 = [1.2, 1.375, 1.55, 1.725, 1.9][p["sport"] - 1]
  return round((f1[0] + f1[1] * p["weight"] + f1[2] * p["size"] - f1[3] * p["age"]) * f2, 1)

