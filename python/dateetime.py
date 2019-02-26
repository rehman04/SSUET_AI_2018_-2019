import datetime
t=datetime.time(12,20,25)
print(t)

today=datetime.date.today()
print(today)

print(today.timetuple())

d1=datetime.date(2018,9,11)
print(d1)

d2=d1.replace(year=1995,month=2,day=4)
print(d2)

print(d1)

print(d1-d2)

print(datetime.timedelta(8620))