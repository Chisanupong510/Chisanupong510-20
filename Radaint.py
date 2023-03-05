import random
target = random.randint(0,100)
count = 0
while True:
    n=int(input('enter the number between 0-100: '))
    count +=1
    if(n>100):
        print('Sorry, your guess is of of renge')
    elif n < target:
        print('Sorry, your guess is too low')
    elif n > target:
        print('Sorry your guess is too high')
    else :
        print('Congratulation,your guess is correct. Total number of guesses is %d' % count)
