player_one_map = [
['.','.','.','.','.','.'],
['.','.','.','.','.','.'],
['.','.','.','.','.','.'],
['.','.','.','.','.','.'],
['.','.','.','.','.','.'],
['.','.','.','.','.','.'],
]
display_control = "1"
player_two_map = [
['.','.','.','.','.','.'],
['.','.','.','.','.','.'],
['.','.','.','.','.','.'],
['.','.','.','.','.','.'],
['.','.','.','.','.','.'],
['.','.','.','.','.','.'],
]
player_two_map_shot = [
['.','.','.','.','.','.'],
['.','.','.','.','.','.'],
['.','.','.','.','.','.'],
['.','.','.','.','.','.'],
['.','.','.','.','.','.'],
['.','.','.','.','.','.'],
]
player_one_map_shot = [
['.','.','.','.','.','.'],
['.','.','.','.','.','.'],
['.','.','.','.','.','.'],
['.','.','.','.','.','.'],
['.','.','.','.','.','.'],
['.','.','.','.','.','.'],
]
player_two_map_hit = [
['.','.','.','.','.','.'],
['.','.','.','.','.','.'],
['.','.','.','.','.','.'],
['.','.','.','.','.','.'],
['.','.','.','.','.','.'],
['.','.','.','.','.','.'],
]
player_one_map_hit = [
['.','.','.','.','.','.'],
['.','.','.','.','.','.'],
['.','.','.','.','.','.'],
['.','.','.','.','.','.'],
['.','.','.','.','.','.'],
['.','.','.','.','.','.'],
]

if display_control == "1":
    if display_control == "1":#4
        fin = input("(row,column)(1-6)(4)Enter the first cordinate of the first ship:")
        direct = input("Use number for direction")
        player_one_map[(int(fin[0])-1)][(int(fin[1])-1)] = "X"
        if direct == "2":
            player_one_map[(int(fin[0]))][(int(fin[1])-1)] = "X"
            player_one_map[(int(fin[0])+1)][(int(fin[1])-1)] = "X"
            player_one_map[(int(fin[0])+2)][(int(fin[1])-1)] = "X"
        if direct == "4":
            player_one_map[(int(fin[0])-1)][(int(fin[1])-2)] = "X"
            player_one_map[(int(fin[0])-1)][(int(fin[1])-3)] = "X"
            player_one_map[(int(fin[0])-1)][(int(fin[1])-4)] = "X"
        if direct == "8":
            player_one_map[(int(fin[0]))-2][(int(fin[1])-1)] = "X"
            player_one_map[(int(fin[0])-3)][(int(fin[1])-1)] = "X"
            player_one_map[(int(fin[0])-4)][(int(fin[1])-1)] = "X"
        if direct == "6":
            player_one_map[(int(fin[0])-1)][(int(fin[1]))] = "X"
            player_one_map[(int(fin[0])-1)][(int(fin[1])+1)] = "X"
            player_one_map[(int(fin[0])-1)][(int(fin[1])+2)] = "X"
    if display_control == "1":#3
        fin = input("(row,column)(1-6)(3)Enter the first cordinate of the first ship:")
        direct = input("Use number for direction")
        player_one_map[(int(fin[0])-1)][(int(fin[1])-1)] = "X"
        if direct == "2":
            player_one_map[(int(fin[0]))][(int(fin[1])-1)] = "X"
            player_one_map[(int(fin[0])+1)][(int(fin[1])-1)] = "X"
        if direct == "4":
            player_one_map[(int(fin[0])-1)][(int(fin[1])-2)] = "X"
            player_one_map[(int(fin[0])-1)][(int(fin[1])-3)] = "X"
        if direct == "8":
            player_one_map[(int(fin[0]))-2][(int(fin[1])-1)] = "X"
            player_one_map[(int(fin[0])-3)][(int(fin[1])-1)] = "X"
        if direct == "6":
            player_one_map[(int(fin[0])-1)][(int(fin[1]))] = "X"
            player_one_map[(int(fin[0])-1)][(int(fin[1])+1)] = "X"
    if display_control == "1":#2
        fin = input("(row,column)(1-6)(2)Enter the first cordinate of the first ship:")
        direct = input("Use number for direction")
        player_one_map[(int(fin[0])-1)][(int(fin[1])-1)] = "X"
        if direct == "2":
            player_one_map[(int(fin[0]))][(int(fin[1])-1)] = "X"
        if direct == "4":
            player_one_map[(int(fin[0])-1)][(int(fin[1])-2)] = "X"
        if direct == "8":
            player_one_map[(int(fin[0]))-2][(int(fin[1])-1)] = "X"
        if direct == "6":
            player_one_map[(int(fin[0])-1)][(int(fin[1]))] = "X"
    if display_control == "1":#2
        fin = input("(row,column)(1-6)(2)Enter the first cordinate of the first ship:")
        direct = input("Use number for direction")
        player_one_map[(int(fin[0])-1)][(int(fin[1])-1)] = "X"
        if direct == "2":
            player_one_map[(int(fin[0]))][(int(fin[1])-1)] = "X"
        if direct == "4":
            player_one_map[(int(fin[0])-1)][(int(fin[1])-2)] = "X"
        if direct == "8":
            player_one_map[(int(fin[0]))-2][(int(fin[1])-1)] = "X"
        if direct == "6":
            player_one_map[(int(fin[0])-1)][(int(fin[1]))] = "X"
    v = 20
    while v != 0:
        print(' ')
        v -= 1


if display_control == "1":
    if display_control == "1":#4
        fin = input("(row,column)(1-6)(4)Enter the first cordinate of the first ship:")
        direct = input("Use number for direction")
        player_two_map[(int(fin[0])-1)][(int(fin[1])-1)] = "X"
        if direct == "2":
            player_two_map[(int(fin[0]))][(int(fin[1])-1)] = "X"
            player_two_map[(int(fin[0])+1)][(int(fin[1])-1)] = "X"
            player_two_map[(int(fin[0])+2)][(int(fin[1])-1)] = "X"
        if direct == "4":
            player_two_map[(int(fin[0])-1)][(int(fin[1])-2)] = "X"
            player_two_map[(int(fin[0])-1)][(int(fin[1])-3)] = "X"
            player_two_map[(int(fin[0])-1)][(int(fin[1])-4)] = "X"
        if direct == "8":
            player_two_map[(int(fin[0]))-2][(int(fin[1])-1)] = "X"
            player_two_map[(int(fin[0])-3)][(int(fin[1])-1)] = "X"
            player_two_map[(int(fin[0])-4)][(int(fin[1])-1)] = "X"
        if direct == "6":
            player_two_map[(int(fin[0])-1)][(int(fin[1]))] = "X"
            player_two_map[(int(fin[0])-1)][(int(fin[1])+1)] = "X"
            player_two_map[(int(fin[0])-1)][(int(fin[1])+2)] = "X"
    if display_control == "1":#3
        fin = input("(row,column)(1-6)(3)Enter the first cordinate of the first ship:")
        direct = input("Use number for direction")
        player_two_map[(int(fin[0])-1)][(int(fin[1])-1)] = "X"
        if direct == "2":
            player_two_map[(int(fin[0]))][(int(fin[1])-1)] = "X"
            player_two_map[(int(fin[0])+1)][(int(fin[1])-1)] = "X"
        if direct == "4":
            player_two_map[(int(fin[0])-1)][(int(fin[1])-2)] = "X"
            player_two_map[(int(fin[0])-1)][(int(fin[1])-3)] = "X"
        if direct == "8":
            player_two_map[(int(fin[0]))-2][(int(fin[1])-1)] = "X"
            player_two_map[(int(fin[0])-3)][(int(fin[1])-1)] = "X"
        if direct == "6":
            player_two_map[(int(fin[0])-1)][(int(fin[1]))] = "X"
            player_two_map[(int(fin[0])-1)][(int(fin[1])+1)] = "X"
    if display_control == "1":#2
        fin = input("(row,column)(1-6)(2)Enter the first cordinate of the first ship:")
        direct = input("Use number for direction")
        player_two_map[(int(fin[0])-1)][(int(fin[1])-1)] = "X"
        if direct == "2":
            player_two_map[(int(fin[0]))][(int(fin[1])-1)] = "X"
        if direct == "4":
            player_two_map[(int(fin[0])-1)][(int(fin[1])-2)] = "X"
        if direct == "8":
            player_two_map[(int(fin[0]))-2][(int(fin[1])-1)] = "X"
        if direct == "6":
            player_two_map[(int(fin[0])-1)][(int(fin[1]))] = "X"
    if display_control == "1":#2
        fin = input("(row,column)(1-6)(2)Enter the first cordinate of the first ship:")
        direct = input("Use number for direction")
        player_two_map[(int(fin[0])-1)][(int(fin[1])-1)] = "X"
        if direct == "2":
            player_two_map[(int(fin[0]))][(int(fin[1])-1)] = "X"
        if direct == "4":
            player_two_map[(int(fin[0])-1)][(int(fin[1])-2)] = "X"
        if direct == "8":
            player_two_map[(int(fin[0]))-2][(int(fin[1])-1)] = "X"
        if direct == "6":
            player_two_map[(int(fin[0])-1)][(int(fin[1]))] = "X"
    v = 20
    while v != 0:
        print(' ')
        v -= 1


while True:
    if display_control == "1":#Player one turn
        if display_control == "1":#print 1
            print(player_one_map_shot[0][0],player_one_map_shot[0][1],player_one_map_shot[0][2],player_one_map_shot[0][3],player_one_map_shot[0][4],player_one_map_shot[0][5])
            print(player_one_map_shot[1][0],player_one_map_shot[1][1],player_one_map_shot[1][2],player_one_map_shot[1][3],player_one_map_shot[1][4],player_one_map_shot[1][5])
            print(player_one_map_shot[2][0],player_one_map_shot[2][1],player_one_map_shot[2][2],player_one_map_shot[2][3],player_one_map_shot[2][4],player_one_map_shot[2][5])
            print(player_one_map_shot[3][0],player_one_map_shot[3][1],player_one_map_shot[3][2],player_one_map_shot[3][3],player_one_map_shot[3][4],player_one_map_shot[3][5])
            print(player_one_map_shot[4][0],player_one_map_shot[4][1],player_one_map_shot[4][2],player_one_map_shot[4][3],player_one_map_shot[4][4],player_one_map_shot[4][5])
            print(player_one_map_shot[5][0],player_one_map_shot[5][1],player_one_map_shot[5][2],player_one_map_shot[5][3],player_one_map_shot[5][4],player_one_map_shot[5][5])
        if display_control == "1":#shooting 1
            choice = input("(one)Enter coordinate of shot: ")
            if player_two_map[(int(choice[0])-1)][(int(choice[1])-1)] == "X":
                player_one_map_shot[(int(choice[0])-1)][(int(choice[1])-1)] = "X"
                player_one_map_hit[(int(choice[0])-1)][(int(choice[1])-1)] = "X"
            else:
                player_one_map_shot[(int(choice[0])-1)][(int(choice[1])-1)] = "0"
    v = 20
    while v != 0:
        print(' ')
        v -= 1
    if display_control == "1":#Player two turn
        if display_control == "1":#print 2
            print(player_two_map_shot[0][0],player_two_map_shot[0][1],player_two_map_shot[0][2],player_two_map_shot[0][3],player_two_map_shot[0][4],player_two_map_shot[0][5])
            print(player_two_map_shot[1][0],player_two_map_shot[1][1],player_two_map_shot[1][2],player_two_map_shot[1][3],player_two_map_shot[1][4],player_two_map_shot[1][5])
            print(player_two_map_shot[2][0],player_two_map_shot[2][1],player_two_map_shot[2][2],player_two_map_shot[2][3],player_two_map_shot[2][4],player_two_map_shot[2][5])
            print(player_two_map_shot[3][0],player_two_map_shot[3][1],player_two_map_shot[3][2],player_two_map_shot[3][3],player_two_map_shot[3][4],player_two_map_shot[3][5])
            print(player_two_map_shot[4][0],player_two_map_shot[4][1],player_two_map_shot[4][2],player_two_map_shot[4][3],player_two_map_shot[4][4],player_two_map_shot[4][5])
            print(player_two_map_shot[5][0],player_two_map_shot[5][1],player_two_map_shot[5][2],player_two_map_shot[5][3],player_two_map_shot[5][4],player_two_map_shot[5][5])
        if display_control == "1":#shooting 2
            choice = input("(two)Enter coordinate of shot: ")
            if player_one_map[(int(choice[0])-1)][(int(choice[1])-1)] == "X":
                player_two_map_shot[(int(choice[0])-1)][(int(choice[1])-1)] = "X"
                player_two_map_hit[(int(choice[0])-1)][(int(choice[1])-1)] = "X"
            else:
                player_two_map_shot[(int(choice[0])-1)][(int(choice[1])-1)] = "0"
    v = 20
    while v != 0:
        print(' ')
        v -= 1
    if display_control == "1":#Win
        if player_two_map_hit == player_two_map:
            print("Good Job Player Two")
            break
        if player_one_map_hit == player_one_map:
            print("Good Job Player One")
            break