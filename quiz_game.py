print('Welcome to my computer quiz?')

playing = input('Do you want to play my quiz? (y/n) ')

if playing != 'y':
    quit()

print('Ok, lets play the quiz!')

max_points = 2
counter = 0
answer = input('What is the shortname for the skier Marco Odermatt? ')
if answer.lower() == 'odi':
    counter = counter+1
    print('Correct, you have {} point(s)'.format(counter))
    
else:
    print('Wrong!')


answer = input('What is the firstname of the best NFL player?  ')
if answer.lower() == 'tom':
    counter = counter+1
    print('Correct, you have {} point(s)'.format(counter))
    
else:
    print('Wrong!')


if counter == 2:
    print('End of the quiz! You answer all questions corret and get {} points out of {}. '.format(counter, max_points ))
else:
    print('End of the quiz! You get {} point(s) out of {}. '.format(counter, max_points ))
