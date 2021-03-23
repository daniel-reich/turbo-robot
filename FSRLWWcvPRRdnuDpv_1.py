"""


Jake is a very habitual person. He eats breakfast at 7:00 a.m. each morning,
lunch at 12:00 p.m. and dinner at 7:00 p.m. in the evening.

Create a function that takes in the current time as a string and determines
the duration of time before Jake's next meal. Represent this as a list with
the first and second elements representing hours and minutes, respectively.

### Examples

    time_to_eat("2:00 p.m.") ➞ [5, 0]
    // 5 hours until the next meal, dinner
    
    time_to_eat("5:50 a.m.") ➞ [1, 10]
    // 1 hour and 10 minutes until the next meal, breakfast

### Notes

N/A

"""

def time_to_eat(current_time):
  #Converted hours to minutes to make comparison easier
  breakfast = 420;
  lunch = 720;
  dinner = 1140;
  full_day = 1440;
  
  #Determines if it's morning or night
  morning = True;
  if (current_time.find('p.m') != -1):
    morning = False;
    
  #Splits the time from the A.M/P.M Callout 
  num_time = current_time.split(' ');
  
  #Splits hours and minutes
  hours_minutes = num_time[0].split(':',1);
    
  #Converts hours to minutes and adds 12 hours if afternoon
  
  if (morning == False):
    hours = (int(hours_minutes[0]) + 12) * 60;
  elif (morning == True and int(hours_minutes[0]) == 12):
    hours = 0;  
  else:
    hours = int(hours_minutes[0]) * 60;
​
  #Totals up minutes and hours 
  
  minutes_total = int(hours_minutes[1]) + hours;
  print(minutes_total);
  if (minutes_total < breakfast):
    diff_minutes = breakfast - minutes_total;
  elif (minutes_total > breakfast and minutes_total < lunch):
    diff_minutes = lunch - minutes_total;
  elif (minutes_total > lunch and minutes_total < dinner):
    diff_minutes = dinner - minutes_total;
  else:
    diff_minutes = full_day - minutes_total + breakfast;
    
  #conversion back to list
  
  diff_hours = int(diff_minutes / 60);
  diff_minutes_remain = abs((diff_hours * 60) - diff_minutes);
  
  answer = [diff_hours,diff_minutes_remain]
  
  return answer

