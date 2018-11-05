"""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import datetime

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    current_month = datetime.date(year,month,1)
    if month == 12:
        month = 1
        year = year+1
    else:
        month = month +1
    next_month =  datetime.date(year,month,1)
    
    difference = next_month - current_month
    
    return difference.days

def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    if year>= datetime.MINYEAR and year<= datetime.MAXYEAR:
        if month>=1 and month<=12:
            if days_in_month(year,month)>=day and day>0:
                return True
            
    return False

    


def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    if is_valid_date(year1,month1,day1) and is_valid_date(year2,month2,day2):
        first_date = datetime.date(year1,month1,day1)
        second_date = datetime.date(year2,month2,day2)

        if second_date > first_date:
            difference = second_date - first_date
            return difference.days

    return 0

def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    
    if is_valid_date(year,month,day):

        todays_date = datetime.date.today()
        birth_date = datetime.date(year,month,day)
        if todays_date > birth_date:
            return days_between(year,month,day,todays_date.year,todays_date.month,todays_date.day)
    
    return 0
