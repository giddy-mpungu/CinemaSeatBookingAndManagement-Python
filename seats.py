from prettytable import PrettyTable
seatsDict ={} #prices
catDict = {} #category
chartDict = {} #indicators */#
    
#read txt file to get the price and category lists
def getPriceCat():
    pricesList = []
    pricesListCategory = []
    f = open('prices.txt', 'r')
    alist = f.readlines()
    f.close()
    for item in alist:
        pricesList.append(int(item.strip().split(",")[1]))
        pricesListCategory.append(item.strip().split(",")[0])

    return pricesList,pricesListCategory

#returning the prices and category lists
PricesList=getPriceCat()[0]
PricesListCategories=getPriceCat()[1]

#returns the list of rows and current status values
def getRows(seatsArray,rowsList):
    rowArray = []
    for item in seatsArray:
        if rowArray == []:
            rowArray.append(item[0])
            rowArray.append(seatsArray[item])
        else:
            if item[0] in rowArray:
                rowArray.append(seatsArray[item])
            else:
                rowsList.append(rowArray)
                rowArray = []
                rowArray.append(item[0])
                rowArray.append(seatsArray[item])
                
    rowsList.append(rowArray)
    return rowsList

# saving the seat chart for a given movie name
def saveChart(listOfrows,movieName):
    f = open(movieName+'.txt', 'w+')
    for row in listOfrows:
        f.write(','.join(row)+"\n")
    f.close()

#that deos not save, such that we update the catdict regulary
def updateRequiredDictsOnProgramReload(movieName):
    rows = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P"] 
    rowsList =[]
    for item in rows:
        for i in range(1,21):
            seat = item + str(i)
            if (item == "A" or item == "B") and (5<=i<=15):
                seatsDict[seat] = PricesList[0]
                chartDict[seat] = "*"
                catDict[seat] = PricesListCategories[0]
            elif (item == "A" or item == "B") and (i <=5 or i >=15):
                seatsDict[seat] = PricesList[1]
                chartDict[seat] = "*"
                catDict[seat] = PricesListCategories[1]
            elif (item == "C" or item == "D" or item == "E" or item == "F") and (i >=1 or i <=20):
                seatsDict[seat] = PricesList[1]
                chartDict[seat] = "*"
                catDict[seat] = PricesListCategories[1]
            elif (item == "G" or item == "H" or item == "I" or item == "J" or item == "K" or item == "L") and (i >=1 or i <=20):
                seatsDict[seat] = PricesList[2]
                chartDict[seat] = "*"
                catDict[seat] = PricesListCategories[2]
            elif (item == "M" or item == "N" or item == "O" or item == "P" ) and (i >=1 or i <=20):
                seatsDict[seat] = PricesList[3]
                chartDict[seat] = "*"
                catDict[seat] = PricesListCategories[3]

#creates and saves defaut available seats chart
def createsDefaultMovieSeatChart(movieName):
    rows = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P"] 
    rowsList =[]
    for item in rows:
        for i in range(1,21):
            seat = item + str(i)
            if (item == "A" or item == "B") and (5<=i<=15):
                seatsDict[seat] = PricesList[0]
                chartDict[seat] = "*"
                catDict[seat] = PricesListCategories[0]
            elif (item == "A" or item == "B") and (i <=5 or i >=15):
                seatsDict[seat] = PricesList[1]
                chartDict[seat] = "*"
                catDict[seat] = PricesListCategories[1]
            elif (item == "C" or item == "D" or item == "E" or item == "F") and (i >=1 or i <=20):
                seatsDict[seat] = PricesList[1]
                chartDict[seat] = "*"
                catDict[seat] = PricesListCategories[1]
            elif (item == "G" or item == "H" or item == "I" or item == "J" or item == "K" or item == "L") and (i >=1 or i <=20):
                seatsDict[seat] = PricesList[2]
                chartDict[seat] = "*"
                catDict[seat] = PricesListCategories[2]
            elif (item == "M" or item == "N" or item == "O" or item == "P" ) and (i >=1 or i <=20):
                seatsDict[seat] = PricesList[3]
                chartDict[seat] = "*"
                catDict[seat] = PricesListCategories[3]
                
        ListOfRows = getRows(chartDict,rowsList)
        saveChart(ListOfRows,movieName)
     

#opens saved seat chart file for a given movie
def openMovieSeatChartFile(movieName):
    f = open(movieName+'.txt', 'r')
    alist = f.readlines()
    f.close()
    rowsInFile = []
    for item in alist:
        rowsInFile.append(item.strip().split(','))

    return rowsInFile

#prnts the chart depending on the movie name and saved chart details            
def printChart(movieName):
    listOfrows = openMovieSeatChartFile(movieName)
    chart = PrettyTable()
    #print(listOfrows)
    chart.field_names = [" ",1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    for row in listOfrows:
        chart.add_row(row)
    print(chart)

#reading values from file into a dict A1:*
def getDictValuesFromFile(movieName):
    dictValues = {}
    rowsFromFile = openMovieSeatChartFile(movieName)
    rows = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P"]
    for j in range(len(rows)):
        for i in range(1,21):
            item = rows[j]
            seat = item + str(i)
            dictValues[seat] = rowsFromFile[j][i]
    return dictValues

#returns the available seats for a given category
def seatsAvailablePerCat(category,movieName):
    dictValues = {}
    dictValues = getDictValuesFromFile(movieName)
    keys = list(dictValues.keys())
    for key in keys:
        if catDict[key] == category and dictValues[key] == "*":
            seatAvail = key+ ", "+ str(seatsDict[key])
            print(seatAvail)
    
#update Seats available per category
def updateSeatsAvailablePercat(optionList,movieName):
    dictValues = {}
    optionList = optionList.split(",")
    rowsList = []
    dictValues = getDictValuesFromFile(movieName)
    #updating
    for item in optionList:
        dictValues[item.upper()] = "#"
    #saving to the file again
    listOfrows = getRows(dictValues,rowsList)
    saveChart(listOfrows,movieName)

#updating tickets sold and revenue values using movie name and booked tickets
def updateTicketAndRevenue(optionList,category,movieName,numberOfSeats,TicketsDict,RevenueDict):
    optionList = optionList.split(",")

    if category == "TWIN":
        if numberOfSeats%2 == 0:
            numberOfSeats = numberOfSeats
        else:
            numberOfSeats = numberOfSeats + 1
        
    #updating revenue
    PrevRevValue =  RevenueDict[movieName]
    newRevenue = PrevRevValue + (numberOfSeats*seatsDict[optionList[0].upper()])
    RevenueDict[movieName] = newRevenue
    #updating tckets
    PrevTicketValue =  TicketsDict[movieName]
    newTicketValue = PrevTicketValue + numberOfSeats
    TicketsDict[movieName] = newTicketValue

    #saving in a file
    listofRevenue = []
    listofTickets = []
    list_key = list(RevenueDict.keys())
    for key in list_key:
        listofRevenue.append(key+":"+str(RevenueDict[key]))
        listofTickets.append(key+":"+str(TicketsDict[key]))
        
    listOfrows = []
    listOfrows.append(listofRevenue)
    listOfrows.append(listofTickets)
    f = open('tickets_revenue.txt', 'w+')
    for row in listOfrows:
        f.write(','.join(row)+"\n")
    f.close()

    
    
#to return number of movies booked (seats/ticed count >0)
def moviesBooked(moviesList):
    RevenueDictPerMovie1 = {}
    TicketSoldDictPermovie1 = {}
    #reading fomtickets_revenue file to updates dicts
    f = open('tickets_revenue.txt', 'r')
    alist = f.readlines()
    f.close()
    rowsInFile = []
    for item in alist:
        rowsInFile.append(item.strip().split(','))

    #initializing revenue and tickets from file
    revenueList = rowsInFile[0]
    ticketsList = rowsInFile[1]
    for item in revenueList:
        itemList = item.split(":")
        RevenueDictPerMovie1[itemList[0]] = int(itemList[1])
    for item in ticketsList:
        itemList = item.split(":")
        TicketSoldDictPermovie1[itemList[0]] = int(itemList[1])

    moviesBookedList = []
    moviesBookedTicketsList = []
    moviesBookedRevenueList = []
    totalRevenue = 0
    totalTickets = 0
    for movie in moviesList:
        if TicketSoldDictPermovie1[movie] > 0:
            moviesBookedList.append(movie)
            totalRevenue = totalRevenue + RevenueDictPerMovie1[movie]
            totalTickets = totalTickets + TicketSoldDictPermovie1[movie]
            moviesBookedTicketsList.append(TicketSoldDictPermovie1[movie])
            moviesBookedRevenueList.append(RevenueDictPerMovie1[movie])
            
    return ','.join(moviesBookedList),totalRevenue,totalTickets,moviesBookedTicketsList,moviesBookedRevenueList

    
            
    
    
