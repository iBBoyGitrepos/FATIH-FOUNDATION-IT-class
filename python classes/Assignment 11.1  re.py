import re

x = re.findall("^[a-z0-9]+@[a-z]+\\.[a-z]+$", input("enter your email: "))

if x:
    print(x)
else:
    print("invalid email...!")