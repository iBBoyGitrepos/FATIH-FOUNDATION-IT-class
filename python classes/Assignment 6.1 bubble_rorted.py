def bubble_sorted(lst):
    for n in range(len(lst) - 1):  
        for x in range(len(lst) - 1 - n):  
            if lst[x] > lst[x + 1]:  
                lst[x], lst[x + 1] = lst[x + 1], lst[x]
    
    print(lst)

lst = [2, 3, 4, 1, 8, 9, 5, 10, 6, 7]
bubble_sorted(lst)
