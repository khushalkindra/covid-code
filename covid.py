spaces = int(input())                             # total number of spaces
positions_list = list(map(int, input().split()))  # positions of employees where 0 represent empty spaces
l1 = []
count = 0
if len(positions_list) == spaces:
    for i in range(0, len(positions_list)):
        if positions_list[i] == 1:
            l1.append(i)
    for g in range(0, len(l1) - 1):
        b = l1[g + 1] - l1[g]
        if b >= 6:                                # if space b/w employees less than 6 feet
            count += 1
        else:
            count += 0
    if count != len(l1)-1:
        print('NO')                               # covid guidelines not followed
    else:
        print('YES')                              # covid guidelines followed
