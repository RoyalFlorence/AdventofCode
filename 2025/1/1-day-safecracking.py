# step 1, iterate through list, make two seperate lists of letters and numbers
# step 2, for each element, make movement
# step 3, check if the dial ends up on zero and count that. 

import csv
import time

position = 50
zero_counter = 0
dial_max = 100
waitTime = 0.0

with open('~/AdventofCode/2025/1/safe-dial-list-1.csv') as file:
    reader = csv.reader(file)
    for ii in reader:
        text = ii[0]
        direction = text[0]
        distance = int(text[1:])
        print('direction is: ', direction)
        print('distance is: ', distance)

        if(direction=='R'):
            position = (position+distance)%dial_max
            print('Dialing to the right...')
            print('New position is: ', position)
            if(position==0):
                print('Position ended on a zero! ')
                zero_counter+=1
                print('+1 for the zero counter, zero counter now on: ', zero_counter)
                time.sleep(waitTime)

        if(direction=='L'):
            position = (position-distance)%dial_max
            print('Dialing to the left...')
            print('New position is: ', position)
            if(position==0):
                print('Position ended on a zero! ')
                zero_counter+=1
                print('+1 for the zero counter, zero counter now on: ', zero_counter)
                time.sleep(waitTime)

print('\nFinal zero counter is: ', zero_counter)