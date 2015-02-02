def guess_square():
    x = 23
    epsilon = 0.01
    step = 0.1
    guess = 0.0

    while abs(guess**2-x) >= epsilon:
        if guess <= x:
            guess += step
        else:
            break
    if abs(guess**2 - x) >= epsilon:
        print 'failed'
    else:
        print 'succeeded: ' + str(guess)

def secret_number():
    guess_value = 50
    maxi = 99
    mini = 0
    guess = 'l'
    print('Please think of a number between 0 and 100!')

    while guess != 'c':
        print("Is your secret number ", guess_value, "?", "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
        guess_value = eval(input(' '))

        if guess == 'l':
           mini = guess_value
           guess_value = (maxi -  guess_value)/2 + guess_value

        elif guess == 'h':
            maxi = guess_value
            guess_value = (guess_value - mini)/2 + guess_value

        else:
            print('select a valid option')

    print('Game over. Your secret number was: ', guess_value)
