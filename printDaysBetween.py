from datetime import date, timedelta
sdate = date(2008, 8, 15)
edate = date(2008, 9, 15)

delta = edate - sdate

for i in range(delta.days + 1):
    day = sdate + timedelta(days=i)
    print(day)
