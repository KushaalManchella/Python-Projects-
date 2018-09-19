#! /usr/bin/env python3/4

def find(pattern):
    count = 0
    indices = []
    answers = []
    for i in pattern:
        if i != 'X':
            indices.append(count)
        count = count+1

#    return
#    print(indices)
#    print(len(pattern))

    with open("sequence.txt","r") as seq:
        text = seq.read()
        #text = "1547896154321687984"
        for i in range(len(text)):
            check1 = 1
            if text[i] == pattern[indices[0]]:
                check = 0
                for x in range(len(indices)):
                    if i + indices[x] - indices[0] < len(text):
                        temp = indices[x] - indices[0]
                    else:
                        check1 = 0
                    if text[i+temp] == pattern[indices[x]]:
                        check += 1
                #                    #    print(check)
                #                print(text[i:len(pattern)])
                    if check == len(indices) and check1 != 0:
                        y = i - indices[0]
                        answers.append(text[y:y+(len(pattern))])
    #                    print(text[i:(len(pattern)+1)])
                #    print("got here")
    #print(answers)
    return(answers)

#find("1XX7")

def getStreakProduct(sequence, maxSize, product):
    text = "54789654321687984"
    ans = []

    for i in range(len(sequence)):
        if i+1 < len(sequence):
            k = i+1
        size = 1
        mult = int(sequence[i])
#        print(mult)
        while size < maxSize and mult < product:
            mult = mult * int(sequence[k])
            if k+1 < len(sequence):
                k = k+1
#            print(mult)
            size = size+1
#            print(size)
            if mult == product:
                ans.append(int(sequence[i:i+size]))
                break

#            print(size)


    #print(ans)
    return(ans)



#getStreakProduct("43200", 3, 24)


def writePyramids(filePath, baseSize, count, char):
    with open(filePath, 'w') as file:
        row_count = (baseSize+1)/2
        col_count = count
        char_count = 1
        space_count = baseSize-1
        diff = 1
        diff_temp = 1
        char_temp = 1
        space_temp = baseSize-1


        while row_count > 0:
            while col_count > 0:
                while space_count > (space_temp/2):
                    file.write(" ")
                    space_count = space_count-1
                    #print("space_count: ",format(space_count))
                while char_count > 0:
                    file.write(char)
                    char_count = char_count-1
                    #print("char_count: ",format(char_count))
                while space_count > 0:
                    file.write(" ")
                    space_count = space_count-1
                    #print("space_count: ",format(space_count))
                if(col_count != 1):
                    file.write(" ")
                col_count = col_count-1

                #print("col_count: ",format(col_count))
                diff = diff_temp
                space_count = space_temp
                char_count = char_temp


            file.write("\n")
            row_count = row_count-1
            col_count = count
            #print(space_count)
            # print(char_count)
            diff = diff+2
            diff_temp = diff
            space_count = baseSize-diff
            space_temp = space_count
            char_count = diff
            char_temp = char_count
            #print(char_temp)
            #print("row_count: ",format(row_count))

    return filePath

writePyramids('my_pyramid13.txt', 13, 6, 'X')
writePyramids('my_pyramid15.txt', 15, 5, '*')



def getStreaks(sequence, letters):
    temp_string = ""
    ans = []
    i = 0
    while i < len(sequence):
        temp = i
        if sequence[i] in letters:

            temp_string = temp_string+sequence[i]
            #print(temp_string)
            while (temp+1) != len(sequence):

                if sequence[temp+1] == temp_string[0]:
                    temp_string = temp_string+sequence[temp+1]
                    temp = temp+1
                else:
                    ans.append(temp_string)
                    temp_string = ""
                    diff = temp-i
                    i = i+diff
                    break
                if temp+1 == len(sequence):
                    ans.append(temp_string)
                    temp_string = ""
                    diff = temp-i
                    i = i+diff
                    break

        i = i+1
    #print(ans)
    return(ans)


#getStreaks("AAASSSSSSAPPPSSPPBBCCCSSS","PAZ")


def findNames(nameList, part, name):
    ans = []

    if part == "L":
        for entry in nameList:
            index = 0
            while entry[index] != " ":
                index += 1
            index += 1
            #while index < len(entry):
            if entry[index:len(entry)].lower() == name.lower():
                ans.append(entry)
                #index += 1

    elif part == "F":
        for entry in nameList:
            index = 0
            stop = 0
            while entry[index] != " ":
                index += 1
            stop = index
            #print(stop)
            index = 0
            if entry[index:stop].lower() == name.lower():
                ans.append(entry)

    elif part == "FL":
        for entry in nameList:
            index = 0
            stop = 0
            while entry[index] != " ":
                index += 1
            stop = index
            #print(stop)
            index = 0
            if entry[index:stop].lower() == name.lower() or entry[(stop+1):len(entry)].lower() == name.lower():
                ans.append(entry)

    #print(ans)
    return(ans)

#findNames(["George Smith", "Mark Johnson", "Cordell Theodore", "Maria Satterfield", "Johnson Cadence"], "FL", "Johnson")

def convertToBoolean(num, size):

    bin_num = bin(num)
    #print(num)
    #print(len(bin_num[2:]))
    #print(bin_num[2:])
    bool_val = 0
    list_num = 0
    ans = []
    size_copy = size

    index = 2
    if(size > len(bin_num[2:])):
        diff = size - len(bin_num[2:])
        bool_val = False
        while diff != 0:
            ans. append(bool_val)
            diff -= 1


    while index < len(bin_num):
        if(bin_num[index] == '1'):
            bool_val = True
        else:
            bool_val = False
        ans.append(bool_val)
        index += 1
        list_num += 1


    #print(ans)
    return(ans)

#convertToBoolean(9,3)


def convertToInteger(boolList):

    index = 0
    binary_list = []
    while index < len(boolList):
        if boolList[index] == True:
            binary_list.append('1')
        else:
            binary_list.append('0')
        index += 1

    #print(binary_list)
    integer = 0
    index -= 1
    digit = 0
    #print(index)


    while index >= 0:
        if binary_list[index] == '1':
            integer = (2**(digit)) + integer
        #print(integer)
        index -= 1
        digit += 1

    #print(integer)




    return(integer)

#convertToInteger([False, False, True, False, False, True])
