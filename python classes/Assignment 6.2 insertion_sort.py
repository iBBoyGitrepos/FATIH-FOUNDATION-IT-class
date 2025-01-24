a = [1, 3, 5, 6, 2, 5, 9, 7, 11]

for i in range(1, len(a)):
    for j in range(i):
        if a[i] < a[j]:
            a.insert(j, a[i])
            a.pop(i+1)
            break
print(a)