first_number = int(input("Enter the first number: "))
operator = input("Enter the operator of them (+, -, *, /): ")
while not(operator == '+' or operator == '-' or operator == '*' or operator == '/'):
    operator = input("invalid operator, Pleace correct the operator (+, -, *, /): ")
last_number = int(input("Enter the last number: "))

if (operator == '+'):
    print(str(first_number), " + ", str(last_number), " = ", str(first_number + last_number))
elif (operator == '-'):
    print(str(first_number), " - ", str(last_number), " = ", str(first_number + last_number))
elif (operator == '*'):
    print(str(first_number), " * ", str(last_number), " = ", str(first_number * last_number))
elif (operator == '/'):
    if (last_number != 0):
        print(str(first_number), " / ", str(last_number), " = ", str(first_number / last_number))
    else:
        print("error: infinity") 

