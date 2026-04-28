import random

print('Welcome to the Number Guessing Game! ')

def easy():
    lives = 10
    return lives

def hard():
    lives = 5
    return lives

def guess_the_number():

    n_to_guess = random.randint(0, 100)

    print('Easy - 10 lives / Hard - 5 lives.')
    difficulty = input('Choose a difficulty. Type easy/hard: ')

    if difficulty == 'easy':
        lives = easy()
    elif difficulty == 'hard':
        lives = hard()
    else:
        print('Invalid difficulty.')
        return

    while True:

        print(f'You have {lives} attempts remaining to guess the number.')

        guess = int(input('Make a guess: '))

        if guess == n_to_guess:
            print(f'You got it. The answer was {n_to_guess}.')
            return 'You win! '
        elif guess > n_to_guess:
            print('Too high.')
        else:
            print('Too low.')

        if guess != n_to_guess:
            lives -= 1

        if lives == 0:
            print('You do not have any more guesses.')
            return  f'Game over! The number was {n_to_guess}. '

do_you = input('Do you want to play ? Type y/n: ')

if do_you != 'y':
    print('Thanks for playing this Guess The Number. ^^')
else:
    guess_the_number()


