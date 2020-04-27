list1 = [4, 5, 6]
list2 = [10, 20, 30]

for i in list1:
    for j in list2:
        if j == 20:
            continue
        print(i * j)
    print("Outside the nested loop")
