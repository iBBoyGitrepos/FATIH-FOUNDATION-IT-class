def fabulacciserice(range):
    serice = [1, 1]

    while not serice[len(serice)-1] >= range:
        # if serice[len(serice)-1] >= range
            sum_num = serice[len(serice)-1] + serice[len(serice)-2]
            serice.append(sum_num)
    print(serice)

user_input = int(input("Enter the max range: "))
fabulacciserice(user_input)