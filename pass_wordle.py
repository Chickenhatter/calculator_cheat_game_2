word = input("5 letter word: ").lower()
control = ['.','.','.','.','.']
tremba = control
filler = control
loop = 0
try:
    word[5] = word
    loop = 5
except:
    try:
        print(word[4])
    except:
        loop = 5
if loop == 0:
    while loop != 15:
        loop += 1
        print('.')
    loop = 0
    while loop != 5:
        guess = input("Word guess: ")
        woop = 0
        try:
            checker = guess[5]
        except:
            try:
                checker = guess[4]
                checker = 'va'
            except:
                checker = 's'
        if checker == 'va':
            print(guess)
            for i in guess:
                if word[woop] == guess[woop]:
                    filler[woop] = word[woop]
                elif i in word:
                    filler[woop] = '?'
                else:
                    filler[woop] = 'X'
                woop += 1
            print(f'{filler[0]}{filler[1]}{filler[2]}{filler[3]}{filler[4]}')
            if ((filler[0])+(filler[1])+(filler[2])+(filler[3])+(filler[4])) == word:
                break
            loop += 1
if loop == 5:
    print('You lost, the word was ', {word})
else:
    print(f'You win, the word was {word}')