import datetime

# x = datetime.datetime(2018,5,15,  6,12,55,0, datetime.timezone.utcoffset())
# print(x.strftime("%d/%M/%Y-%z"))

# y = datetime.datetime.strptime("5/May/2020", "%d/%B/%Y")
# print(datetime.datetime.fromtimestamp(y.timestamp))

x = datetime.datetime.strptime("30/12/2020", "%d/%m/%Y")
print(x)
y = x.timestamp()
print(y)
z = datetime.datetime.fromtimestamp(y)
print(z)


