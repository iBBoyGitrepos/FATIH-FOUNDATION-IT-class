def merge_sort(a):
    if int(len(a) > 1):
        x = int(len(a)/2)
        left = merge_sort(a[:x])
        right = merge_sort(a[x:])
        return merge(left, right)
    else:
        return a
    
def merge(left, right):
    new_arr = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            new_arr.append(left[0])
            left.pop(0)
        else:
            new_arr.append(right[0])
            right.pop(0)
        if len(left) == 0:
            for x in range(right):
                new_arr = merge_sort(x)
        else:
            for x in range(left):
                new_arr = merge_sort(x)
        return new_arr    
    else:
        return(a)

a = [2, 5, 3, 1]
print(merge_sort(a))
