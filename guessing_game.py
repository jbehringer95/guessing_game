import random

highscore = 0
attempts = 0
def start_game():
    print('Welcome to the number guessing game.')
    random_number =  random.randint(1, 10)
    guess = ()
    global attempts
    global highscore
    attempts = 0
    attempts += 1
    while guess != random_number:
        try:
            guess = int(input('Please guess a number from 1-10  '))
        
        except:
            print('This is not a valid number')
        
        else:
            
            if guess <= 10:
            
                if guess < random_number:
                    attempts += 1
                    print('The number is higher than {}'.format(guess))
                
                elif guess > random_number:
                    attempts += 1
                    print('The number is lower than {}'.format(guess))
                    
                elif guess == random_number:
                    print('Wow, you guessed the number right in {} attempts'.format(attempts))
                    
                    if highscore == 0:
                        print('Awesome job, you have made a new highscore of {}'.format(attempts))
                        highscore = attempts
                    
                    elif highscore < attempts:
                        print('Sorry you did not make a new highscore.')
            
                    elif highscore > attempts:
                        print('Awesome job, you have made a new highscore of {}'.format(attempts))
                        highscore = attempts
            
            else:
                print('Sorry the number is not between 1-10')

start_game()
                
new_game = input('Would you like to play another game. (y/n)  ')

while new_game == 'y':
    print('The highscore is {}'.format(highscore))
    start_game()
    new_game = input('Would you like to play another game. (y/n)  ')
    



print('Have a lovely day and please return if you wanna play again')
