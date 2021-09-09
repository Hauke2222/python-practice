my_list = [1, 3, 6, 7, 9, 12, 32]

divisible_by_3 = filter(lambda x: x % 3 == 0, my_list)

print(list(divisible_by_3))