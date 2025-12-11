import csv
csv_file = '3-jolt-list.csv'
output_txt_file = '3-output.txt'

def maxValueFirstPosition(inputVector):
    if(len(inputVector)==0):
        print('inputVector is apparently empty? ', inputVector, '\n')
        return 0,0
    if(len(inputVector)!=0):
        maxValue = max(inputVector)
        #first position of the highest value
        firstPosition = inputVector.index(maxValue)
        return maxValue, firstPosition



with open(output_txt_file, 'w') as output:
    with open(csv_file) as file:
        reader = csv.reader(file)
        foundJoltValueVector = []
        for row in reader:
            joltStrVector=[]
            joltIntVector=[]
            output.write(str(row)+'\n')
            for ii in range(len(str(row[0]))):
                string_row = str(row[0])
                int_row = int(row[0])
                joltStrVector.append(string_row[ii])
                joltIntVector.append(int(string_row[ii]))

            maxValue, firstPosition = maxValueFirstPosition(joltStrVector)
            if(maxValue==0 and firstPosition==0):
                print(row[0])
            # now to split the vector and do the same, but only if the firstPosition of the MaxValue is not the last number
            if(firstPosition!=len(joltIntVector)):
                #make a sub vector starting from the first position of the highest number(excl.)
                subjoltIntVector = []
                for ii in range(firstPosition+1, len(joltIntVector)):
                    subjoltIntVector.append(joltIntVector[ii])
                submaxValue, subfirstPosition = maxValueFirstPosition(subjoltIntVector)
                

            if(firstPosition==len(joltIntVector)):
                print('max value is last digit of row\n')
                subjoltIntVector = []
                for ii in range(0, len(joltIntVector)-1):
                    subjoltIntVector.append(joltIntVector[ii])
                submaxValue, subfirstPosition = maxValueFirstPosition(subjoltIntVector)

            foundJoltValue = int(str(maxValue)+str(submaxValue))
            output.write('found max jolt value of this list is '+str(foundJoltValue)+'\n')
            print('Found max jolt value is ', foundJoltValue)
            foundJoltValueVector.append(foundJoltValue)
        output.write('\n\nList of all found jolt values is \n' + str(foundJoltValueVector))
        output.write('\n\nSum all found jolt outputs is : ' + str(sum(foundJoltValueVector)))

    output.close()