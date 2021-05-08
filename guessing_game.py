import random

# Empty list to keep track of highscores and attempts in the game.
highscore = 0
attempts = 0


def start_game():
    print('Welcome to the number guessing game.')
    # Gets a random number to use in the guessing game
    random_number = random.randint(1, 10)
    guess = ()
    global attempts
    global highscore
    attempts = 0
    attempts += 1
    while guess != random_number:
        # Makes sure the user does puts in an input that is an integer
        try:
            guess = int(input('Please guess a number from 1-10  '))

        except Exception:
            print('This is not a valid number')

        else:

            # Makes sure the guess is between 1-10
            if (guess <= 10) and (guess >= 1):

                # Checks the number to see if it is correct
                # If the number is not correct then it
                # tells you if it is lower or higher
                if guess < random_number:
                    attempts += 1
                    print('The number is higher than {}'.format(guess))

                elif guess > random_number:
                    attempts += 1
                    print('The number is lower than {}'.format(guess))

                elif guess == random_number:
                    print('Wow, you guessed the number'
                          'right in {} attempts'.format(attempts))

                    # Checks to see if you got a highscore
                    if highscore == 0:
                        print('Awesome job, you have made'
                              'a new highscore of {}'.format(attempts))
                        highscore = attempts

                    elif highscore < attempts:
                        print('Sorry you did not make a new highscore.')

                    elif highscore > attempts:
                        print('Awesome job, you have made'
                              'a new highscore of {}'.format(attempts))
                        highscore = attempts

            else:
                print('Sorry the number is not between 1-10')


start_game()

new_game = input('Would you like to play another game. (y/n)  ')

# While loop to let you keep playing the game to get a new highscore
while new_game == 'y':
    print('The highscore is {}'.format(highscore))
    start_game()
    new_game = input('Would you like to play another game. (y/n)  ')

print('Have a lovely day and please return if you wanna play again!')
