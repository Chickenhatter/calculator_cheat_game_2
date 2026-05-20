word = input("5 letter word: ").lower()
loop = 0
try:
    word[5] = word
    loop = 5
except:
    try:
        word[4] = word[4]
    except:
        loop = 5

