"""
Create a function that takes a string containing money in dollars and pounds
sterling (seperated by comma) and returns the sum of _dollar bills only_ , as
an integer.

For the input string:

  * Each amount is prefixed by the currency symbol: **$** for dollars and **£** for pounds.
  * Thousands are represented by the suffix **k**.

i.e. $4k = $4,000 and £40k = £40,000

### Examples

    add_bill("d20,p40,p60,d50") ➞ 20 + 50 = 70
    
    add_bill("p30,d20,p60,d150,p360") ➞ 20  + 150 = 170
    
    add_bill("p30,d2k,p60,d200,p360") ➞ 2 * 1000 + 200 = 2200

### Notes

There is at least one dollar bill in string.

"""

def add_bill(money):
  # Input is a string and we need list of all the entries split by comma
  money = money.split(",")
  # Output sum of dollars in money, initialize with zero
  dollar_total = 0
  # Given
  dollar_string = "d"
  thousand_string = "k"
  
  #Setup variables
  convert = 0
  
  # Loop through every entry
  for entry in money:
    # If entry stars with dollar string use it
    if(entry[0] == dollar_string):
      # Check if entry has thousand string in it
      if(thousand_string in entry[1:]):
        # Convert rest of entry except last character to string
        convert = int(entry[1:-1])
        # Multiply by 1000 and Add conversion to dollar_total
        dollar_total += convert * 1000
      else:
        # Convert rest of entry to string into a number 
        convert = int(entry[1:])
        # Add conversion to total
        dollar_total += convert
  
  # Return the output, in our case dollar_total
  return dollar_total

