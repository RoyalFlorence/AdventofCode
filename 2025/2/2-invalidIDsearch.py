# step plan

# step 1
# make function that has ID integer input
# check if the amount of characters is even
# if yes, then split up in two parts and check if both parts are the same
# if yes, then store

# step 2
# make for-loop that ranges from first ID to second ID(incl.)
# use function for each iteration

import csv
import math

# csv_filename = 'test-idRanges.csv'
csv_filename = 'idRanges.csv'
# step 1, function that check invalid ID
# part 2
# function invalidID2 that takes as input a to-be-checked ID and the biggest number of the data set
# for range 1 to biggestNr/2(rounded down), check if the amount of characters of the number is divisible by that number
# if it is divisble, then divide the ID into character brackets of that size and check if the brackets are all equal.

def invalidID(input_id):

    string_input_id = str(input_id)
    print('string_input_id is: ', string_input_id)
    print('length of string_input_id is: ', len(string_input_id))
    if(len(string_input_id)%2==1):
        print('input ID has uneven characters, therefore no repeating digits are possible.')
        return input_id, 0
    if(len(string_input_id)%2==0):
        part_1 = string_input_id[0:len(string_input_id)//2]
        part_2 = string_input_id[len(string_input_id)//2:]
        # print('first half of ID is ', part_1)
        # print('second half of ID is ', part_2)
        input_id_1 = int(part_1)
        input_id_2 = int(part_2)
        if(input_id_1==input_id_2):
            print('repeating digits found for ', string_input_id, '\n namely ', part_1, ' and ', part_2, ' are the same repeating digits.')
        
            return input_id, 1
        else:
            return input_id, 0
def findBiggestNr(input_csv):

    with open(input_csv) as file:
        reader = csv.reader(file)
        biggestNr = 0
        for row in reader:
            if(int(row[1])>biggestNr):
                biggestNr=int(row[1])
    return biggestNr
def invalidID2(input_id, biggestNr):

    #for-loop from 1 to biggestNr/2(rounded down) to divide into character brackets
    # ii is bracket length
    for ii in range(1, math.floor(len(str(biggestNr))/2)+1):
        #declare empty vector to append character brackets to
        bracketVector = []
        #check if input is divisble by iterator, if so, divide input into character brackets
        if(len(str(input_id))%ii==0):
            for jj in range(0, len(str(input_id)), ii):
                bracketVector.append(str(input_id)[jj:jj+ii])
            if(len(bracketVector)==1):
                print('This bracket vector only has one element, very stinkie!')
                continue
            else:
                print('This bracket vector is not stinkie')
                print(bracketVector)
            # print('bracketVector with bracket length ', ii,  ' is :')
            # print(bracketVector)

            # bracketVector is the ID split up into equally sized parts
            # now check if each element in the bracketVector is the same
            # 
            if(len(set(bracketVector))==1 and len(bracketVector)>1):
                print('\nRepeating digits found in ID ', input_id, ' :')
                print(bracketVector, '\n\n')
                return input_id, 1
            else:
                continue
            
        else:
            continue
    return input_id, 0
    



list_invalidID = []
with open('2-output.txt', 'w') as output:

    # biggest number in the csv file is:
    biggestNr = findBiggestNr(csv_filename)
    output.write('list of found invalid IDs is: \n')
    with open(csv_filename) as file:
        reader = csv.reader(file)
        print('reader is ', reader)



        for row in reader:
            first_ID = int(row[0])
            print('first ID is ', first_ID)
            last_ID = int(row[1])
            print('last ID is ', last_ID)
            for ii in range(first_ID, last_ID+1):
                # print('seeing if number ', ii, ' has repeating numbers...')
                output_invalidID = invalidID2(ii, biggestNr)
                value_invalidID = output_invalidID[0]
                bool_invalidID = output_invalidID[1]
                if(bool_invalidID==1):
                    list_invalidID.append(value_invalidID)
                    output.write(str(value_invalidID)+'\n')
    output.write('sum of each found invalid ID is: '+ str(sum(list_invalidID)))
    output.close()

# testNr = 123123123123123123
# print(invalidID2(testNr, len(str(testNr))))
# print(findBiggestNr(csv_filename))

