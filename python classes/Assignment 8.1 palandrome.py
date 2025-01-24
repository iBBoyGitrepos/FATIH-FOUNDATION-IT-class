def palandrome(str):
    palandrome = False
    for x in range(int(len(str)/2)):
        if str[x] == str[len(str)-x-1]:
            palandrome = True
        else:
            palandrome = False
            break
    if palandrome == True:
        print("string is palandrome")
    else:
        print("string is not palandrome")

palandrome("wqrw")