"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime


user_date = input("Enter a month and a year in the format MM/YYYY: ")

if "/" in user_date: 
    month, year = user_date.split("/")
    if month.isnumeric() and year.isnumeric():
       print(calendar.HTMLCalendar().formatmonth(theyear=int(year), themonth=int(month), withyear=True))
    else:
        print("Please input a proper date using the format MM/YYYY")
elif user_date.isnumeric():
    if int(user_date) in range(1-12):
        month = user_date
        year = 2019
        print(calendar.HTMLCalendar().formatmonth(theyear=int(year), themonth=int(month), withyear=True))
    else:
        month= 9
        year = 2019
        print(calendar.HTMLCalendar().formatmonth(theyear=int(year), themonth=int(month), withyear=True))
elif user_date == "":
    month= 9
    year = 2019
    print(calendar.monthcalendar(int(year), int(month)))
else:
    print("Please input a proper date using the format MM/YYYY")
exit()

# It works! Here's a codepen of the html calendar looking all nice: https://codepen.io/meginks-the-styleful/pen/KKPywxg 

