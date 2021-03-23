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

from datetime import datetime
​
def energy_bill(time1, time2, read1, read2, tariff, stand):
    days = (
        datetime(*map(int, time2.split(","))) -
        datetime(*map(int, time1.split(",")))
    ).days * stand
    if days < 0:
        return "Invalid date"
    meter = (read2 - read1) * tariff
    if meter < 0:
        return "Invalid meter readings"
    return "${}".format(round(1.05 * (days + meter), 2))

