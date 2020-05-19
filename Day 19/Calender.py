import datetime
import calendar
def find(date):
  born=datetime.datetime.strptime(date,'%m %d %Y').weekday()
  return calendar.day_name[born]
date=input()
x=find(date)
print(x.upper())