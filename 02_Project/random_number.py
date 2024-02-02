import random

number = random.randrange(0,100)
# print(number)


counter = 0
while counter < 10:
    counter = counter + 1
    print('That is your {} try.'.format(counter))
    guess_number = input('Type a number: ')

    if guess_number.isdigit():
        guess_number = int(guess_number)
        if guess_number < 0:
            print('Please write a number thats bigger then 0.')
            continue
        elif guess_number > 99:
            print('Please write a number thats smaller then 100.')
            continue
        elif guess_number > number:
            print('The number must be smaller.')
            continue
        elif guess_number < number:
            print('The number must be bigger.')
            continue
        elif guess_number == number:
            print('You got it!/n The number is {}. You needed {} guesses.'.format(number, counter))
            break

