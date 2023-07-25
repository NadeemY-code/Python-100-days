#guess game
secret_number = 9
Guess_count = 0
while Guess_count < 3:
    Guess_the_number = int(input('guess\n'))
    Guess_count +=1
    if Guess_the_number == secret_number :
        print('you won ')
        break
else:
        print("Better luck next time" )
