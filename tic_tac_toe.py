tic_map = [['.','.','.'],['.','.','.'],['.','.','.']]
game_fish = False
while True:
    if game_fish == False:
        if game_fish == False:
            print(tic_map[0][0],tic_map[0][1],tic_map[0][2])
            print(tic_map[1][0],tic_map[1][1],tic_map[1][2])
            print(tic_map[2][0],tic_map[2][1],tic_map[2][2])
        choice = input("row/colomn/x")
        if tic_map[int(choice[0])-1][int(choice[1])-1] == '.':
            tic_map[int(choice[0])-1][int(choice[1])-1] = "X"
        if game_fish == False:#trickeck
            if game_fish == False: #0,0
                if (tic_map[0][0] == tic_map[0][1] == tic_map[0][2] != '.'):
                    print(tic_map[0][0])
                    break
                if (tic_map[0][0] == tic_map[1][1] == tic_map[2][2] != '.'):
                    print(tic_map[0][0])
                    break
                if (tic_map[0][0] == tic_map[1][0] == tic_map[2][0] != '.'):
                    print(tic_map[0][0])
                    break
            if game_fish == False: #2,2
                if (tic_map[0][2] == tic_map[1][2] == tic_map[2][2] != '.'):
                    print(tic_map[0][2])
                    break
                if (tic_map[2][0] == tic_map[2][1] == tic_map[2][2] != '.'):
                    print(tic_map[2][0])
                    break
            if game_fish == False: #1,1
                if (tic_map[0][1] == tic_map[1][1] == tic_map[2][1] != '.'):
                    print(tic_map[0][1])
                    break
                if (tic_map[1][0] == tic_map[1][1] == tic_map[1][2] != '.'):
                    print(tic_map[1][0])
                    break
                if (tic_map[2][0] == tic_map[1][1] == tic_map[0][2] != '.'):
                    print(tic_map[2][0])
                    break
    if game_fish == False:
        if game_fish == False:
            print(tic_map[0][0],tic_map[0][1],tic_map[0][2])
            print(tic_map[1][0],tic_map[1][1],tic_map[1][2])
            print(tic_map[2][0],tic_map[2][1],tic_map[2][2])
        choice = input("row/colomn/o")
        if tic_map[int(choice[0])-1][int(choice[1])-1] == '.':
            tic_map[int(choice[0])-1][int(choice[1])-1] = "O"
        if game_fish == False:#trickeck
            if game_fish == False: #0,0
                if (tic_map[0][0] == tic_map[0][1] == tic_map[0][2] != '.'):
                    print(tic_map[0][0])
                    break
                if (tic_map[0][0] == tic_map[1][1] == tic_map[2][2] != '.'):
                    print(tic_map[0][0])
                    break
                if (tic_map[0][0] == tic_map[1][0] == tic_map[2][0] != '.'):
                    print(tic_map[0][0])
                    break
            if game_fish == False: #2,2
                if (tic_map[0][2] == tic_map[1][2] == tic_map[2][2] != '.'):
                    print(tic_map[0][2])
                    break
                if (tic_map[2][0] == tic_map[2][1] == tic_map[2][2] != '.'):
                    print(tic_map[2][0])
                    break
            if game_fish == False: #1,1
                if (tic_map[0][1] == tic_map[1][1] == tic_map[2][1] != '.'):
                    print(tic_map[0][1])
                    break
                if (tic_map[1][0] == tic_map[1][1] == tic_map[1][2] != '.'):
                    print(tic_map[1][0])
                    break
                if (tic_map[2][0] == tic_map[1][1] == tic_map[0][2] != '.'):
                    print(tic_map[2][0])
                    break
    