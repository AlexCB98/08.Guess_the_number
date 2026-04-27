import random

print('Welcome to the Number Guessing Game! ')

n_to_guess = random.randint(0,100)

def easy():
    lives = 10
    return lives

def hard():
    lives = 5
    return lives

def guess():

    lives = 0

    difficulty = input('Choose a difficulty: Type easy/hard: ')
    guess = int(input('Make a guess: '))

    if difficulty == 'easy':
        easy()
    else:
        hard()

    print(f'You have {lives} attempts remaining to guess the number.')

    if guess == n_to_guess:
        print(f'You got it. The answer was {n_to_guess}.')
    elif guess > n_to_guess:
        lives -= 1
        print('Too high.')
    else:
        lives -= 1
        print('Too low.')

print(guess())