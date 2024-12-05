table_of = int(input("Enter the number for print table: "))
table_range = int(input("Enter the number for table range: "))

for i in range(table_range):
    print(table_of, "x", i + 1, "=", table_of * (i + 1))
