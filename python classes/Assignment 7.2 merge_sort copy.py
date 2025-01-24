def merge_sort(a):
    if int(len(a) > 1):
        half = int(len(a)/2)
        left = merge_sort(a[:half])
        right = merge_sort(a[half:])
        new_arr = []
        
        if len(left) == 0 or len(right) == 0:
            sorted_l = merge_sort(left)
            sorted_r = merge_sort(right)
            
        while len(left) == 0 or len(right) == 0:
            if left[0] < right[0]:
                new_arr.insert(left[0])
                left.pop(0)
            else:
                new_arr.append(right[0])
                right.pop(0)
            # if len(left) == 0:
            #     for x in right:
            #         x = merge_sort(new_arr)
            # else:
            #     for x in range(left):
            #         x = merge_sort(new_arr)
        return new_arr    
    else:
        return(a)

a = [2, 5, 3, 1]
print(merge_sort(a))
