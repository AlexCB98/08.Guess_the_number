import random

print('Welcome to the Number Guessing Game! ')

n_to_guess = random.randint(0,100)

def easy():
    lives = 10
    return lives

def hard():
    lives = 5
    return lives

def guess_the_number():

    difficulty = input('Choose a difficulty: Type easy/hard: ')

    if difficulty == 'easy':
        lives = easy()
    else:
        lives = hard()

    print(f'You have {lives} attempts remaining to guess the number.')

    while True:

        guess = int(input('Make a guess: '))

        print(f'You have {lives} attempts remaining to guess the number.')

        if guess == n_to_guess:
            print(f'You got it. The answer was {n_to_guess}.')
        elif guess > n_to_guess:
            print('Too high.')
        else:
            print('Too low.')

        if guess != n_to_guess:
            lives -= 1

        if lives == 0:
            print('You do not have any more guesses.')
            break
    return  'Game over.'


print(guess_the_number())