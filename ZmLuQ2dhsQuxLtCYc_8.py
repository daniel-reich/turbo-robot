"""


Create a function that calculates an energy bill.

Given a billing start date and end date, start and end meter reading, a unit
price in pence, and a standing charge (a daily rental fee for your meter) as
arguments, calculate your bill.

An energy bill is calculated by multiplying the difference between meter
readings with the unit price and adding the number of days multiplied by the
standing charge. You then have to add 5% tax.

(days between dates x standing charge) + (diference bewteen meter readings x
unit price) + 5% tax

### Examples

    energy_bill("2020,01,01", "2020,04,01", 1000, 2000, 0.188, 0.243),  = "$220.62"
    "2020,04,01" (end date) - "2020,01,01" ( start date ),  = 91 days
      2000 ( end meter read )- 1000 ( start meter read ) = 1000 units used
      1000 (units) * 0.188p (each unit cost) = $188
      91 (days) * 0.243p (standing charge) == $22.113
      22.113 (Total standing charge cost) + $188 (total unit cost) = $210.113
      210.113 (cost) * 0.05 (uk tax on energy) = 10.50565
      210.113 (cost) + 10.50565 (tax) = 220.61865
      answer = "$220.62"

### Notes

  * If the end date is an earlier date from the start date return `"Invalid date"`.
  * If the end meter reading is less then the start meter reading return `"Invalid meter readings"`.
  * Please bring to my attention any clarity issues.

"""

import datetime
def energy_bill(start_date, end_date, start_read, end_read, tariff, stand):
​
  start_year = int(start_date.split(',')[0])
  start_month = int(start_date.split(',')[1])
  start_day = int(start_date.split(',')[2])
  
  end_year = int(end_date.split(',')[0])
  end_month = int(end_date.split(',')[1])
  end_day = int(end_date.split(',')[2])
  
  date1 = datetime.date(start_year,start_month,start_day)
  date2 = datetime.date(end_year,end_month,end_day)
  
  amount_of_days_between_two = (date2 - date1).days
  if amount_of_days_between_two < 0:
    return 'Invalid date'
  
  total_misc = (amount_of_days_between_two * stand) + ((end_read - start_read)*tariff)
  the_total_cost = total_misc + (total_misc * 0.05)
  
  return '${}'.format(round(the_total_cost,2)) if the_total_cost > 0 else 'Invalid meter readings'

