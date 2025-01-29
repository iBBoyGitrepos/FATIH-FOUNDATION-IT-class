import re

x = re.findall("^[1-2]?[0-9]/[1-9]{2}/[0-9]$", input("enter date: "))

if x:
    print("valid date")
    print(x)
else:
    print("invalid date")
    print(x)
    