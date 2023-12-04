fname = input("Input file name: ")
combinedNumbers = ""
numberCatchList = []
finalList = []
numberCatchListLength = 0

try:
    fname = open(fname,"r")
except FileNotFoundError:
    print("File cannot be opened check the spelling of the file or if the file exists")
    quit()
    
for line in fname:
    #reset numberCatchList
    numberCatchList = []
    #For character in string if a number add to list
    for character in line:
        if character.isnumeric():
            numberCatchList.append(character)

    numberCatchListLength = len(numberCatchList) -1

    #If the length of numberCatchList is greater than 2 remove center section else if length is 1 duplicate number
    if len(numberCatchList) > 2:
        del(numberCatchList[1:numberCatchListLength])
    elif len(numberCatchList) == 1:
        numberCatchList.append(numberCatchList[0])

    #Combine the two pulled numbers and add them to a list as an integer
    combinedNumbers = numberCatchList[0] + numberCatchList[1]
    print(combinedNumbers)

    finalList.append(int(combinedNumbers))

#Calculate the sum of the list
print(sum(finalList))

#close the file        
fname.close()