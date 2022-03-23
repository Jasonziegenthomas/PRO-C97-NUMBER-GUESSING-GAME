import random

print('number gussing game')
number = number.randit(1,9)
chances=0
while chance < 5:
    guess = int(input('Enter your guess : '))
    if guess == number :
    print('congratulation you won')
    break
    elif guess < number :
    print("Your guess is too low , guess a number higher than ", guess)
    else :
    print('your guess is  too low ,please guess a number higher than',guess)
    chances +=1

if not chances < 5:
    print('you lose')



