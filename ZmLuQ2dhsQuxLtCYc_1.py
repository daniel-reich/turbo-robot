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

def is_leap_year(y):
    return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)
​
def days_in_month(m, y):
    if m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    if m == 2:
        return 29 if is_leap_year(y) else 28
    return 30
​
def energy_bill(start_date, end_date, start_read, end_read, tariff, stand):
    if end_read < start_read:
        return "Invalid meter readings"
    y1, m1, d1 = [int(_) for _ in start_date.split(',')]
    y2, m2, d2 = [int(_) for _ in end_date.split(',')]
    if [y1, m1, d1] > [y2, m2, d2]:
        return "Invalid date"
    days = 0
    while [y1, m1, d1] != [y2, m2, d2]:
        days += 1
        d1 += 1
        if d1 > days_in_month(m1, y1):
            m1 += 1
            d1 = 1
            if m1 > 12:
                y1 += 1
                m1 = 1
    price = (days * stand + (end_read - start_read) * tariff) * 1.05
    return "$" + str(round(price, 2))

