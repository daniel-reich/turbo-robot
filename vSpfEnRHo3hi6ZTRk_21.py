"""


What's the probability of someone making a certain amount of free throws in a
row given their free throw success percentage? If Sally makes 50% of her free
shot throws. Then Sally's probability of making 5 in a row would be 3%.

### Examples

    free_throws("75%", 5) ➞ "24%"
    
    free_throws("25%", 3) ➞ "2%"
    
    free_throws("90%", 30) ➞ "4%"

### Notes

  * The success rate is a string.
  * The function should return a string with the percent sign.
  * Round your answer to the nearest whole number.

"""

def free_throws(success, rows):
  
  PreStep_S1 = str(success)
  PreStep_S2 = PreStep_S1.replace("%","")
  PreStep_S3 = int(PreStep_S2)
  PreStep_S4 = float(PreStep_S3 * 0.01)
  PreStep_S5 = round(PreStep_S4, 2)
  Occurrence = PreStep_S5
  
  Decimal = Occurrence ** rows
  Number = Decimal * 100
  Percentage = int(round(Number,0))
  
  Answer = str(Percentage) + "%"
  
  return Answer

