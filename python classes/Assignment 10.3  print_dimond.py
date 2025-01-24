def print_dimond(max_range):
    for i in range(1, max_range +1):
        print(f"{' ' * (max_range - i)}{'* ' * i}")
        
    for i in range(1, max_range):
        print(f"{' ' * i}{'* ' * (max_range-i)}")
         
print_dimond(7)

# Assignment  print_dimond.py