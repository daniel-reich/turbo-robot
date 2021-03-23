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

from datetime import date
def energy_bill(start_date, end_date, start_read, end_read, tariff, stand):
    if end_read < start_read: return "Invalid meter readings"
    
    # Days 
    un_sort_days = start_date.replace(","," ") + " " + end_date.replace(","," ")
    sorted_days = un_sort_days.split(" ")
    sorted_days = list(map(int,sorted_days))
    
    days = (date(sorted_days[3], sorted_days[4], sorted_days[5]) - 
            date(sorted_days[0], sorted_days[1], sorted_days[2]))
    
    if str(days.days).startswith("-"): return "Invalid date"
    day_standing = days.days * stand
    
    # Units
    meter_read = (end_read - start_read) * tariff
    
    unit_cost = day_standing + meter_read
    unit_cost_tax = unit_cost * 0.05
    return "$" + str(round(unit_cost_tax + unit_cost,2))

