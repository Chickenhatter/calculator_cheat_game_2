player_one_map = [
['.','.','.','.','.','.'],
['.','.','.','.','.','.'],
['.','.','.','.','.','.'],
['.','.','.','.','.','.'],
['.','.','.','.','.','.'],
['.','.','.','.','.','.'],
]
display_control = "1"
player_two_map = player_one_map
if display_control == "1"
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
    print(player_one_map)
        
