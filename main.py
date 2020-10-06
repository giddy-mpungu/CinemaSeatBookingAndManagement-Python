from seats import*
# from admin import movies_list, time_list

print("\n\nWelcome! To Cinema Booking System\n")
restart = "Y"

TicketSoldDictPermovie = {}
RevenueDictPerMovie = {}

# movies = movies_list
# times = time_list

movies = ["Zootopia","The Maze Runner","Black Panther","Little"]
times = [": 1:00pm",": 3:00pm",": 5:00pm",": 7:00pm"]

#checking for created or not
#reading created_or_not file 
f = open('created_or_not.txt', 'r')
alist = f.readlines()
f.close()
rowsInFile = []
for item in alist:
    rowsInFile.append(item.strip())
if rowsInFile[0] == "FALSE":
    #creating the movies chart files
    for movieName in movies:
        createsDefaultMovieSeatChart(movieName)

    #creating default dictionary for ticket sold and revenue per movie
    for movie in movies:
        TicketSoldDictPermovie[movie] = 0
        RevenueDictPerMovie[movie] = 0
    f = open('created_or_not.txt', 'w+')
    alist = f.write("TRUE")
    f.close()
    
    #saving in a file
    listofRevenue = []
    listofTickets = []
    list_key = list(RevenueDictPerMovie.keys())
    for key in list_key:
        listofRevenue.append(key+":"+str(RevenueDictPerMovie[key]))
        listofTickets.append(key+":"+str(TicketSoldDictPermovie[key]))
        
    listOfrows = []
    listOfrows.append(listofRevenue)
    listOfrows.append(listofTickets)
    f = open('tickets_revenue.txt', 'w+')
    for row in listOfrows:
        f.write(','.join(row)+"\n")
    f.close()

    
else:
    for movieName in movies:
        updateRequiredDictsOnProgramReload(movieName)
        
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
        RevenueDictPerMovie[itemList[0]] = int(itemList[1])
    for item in ticketsList:
        itemList = item.split(":")
        TicketSoldDictPermovie[itemList[0]] = int(itemList[1])

while True:
    def menu():
        print("\nChoose your preference...\n")
        print("1. Movie Schedule.")
        print("2. Seat Assignment.")
        print("3. Payments (for reserved seat).")
        print("4. Reset Seating Plan.")
        print("5. Exit.")
        option = int(input("\n--> "))
        return option

            #*******FOR THE MOVIE SCHEDULE OPTION******
    option = menu()
    if option == 1:
        print("\nChoose your prefered movie...\n")
        # movie schedule.readlines()
        for i in range(len(movies)):
            print(str(i+1)+". "+ movies[i]+ times[i])
        opt = int(input("\n--> "))

        movieNameSelected = movies[opt-1]
        print("\nWanna watch "+movieNameSelected+"..!\n")
        print("1. Buy a ticket")
        opt = int(input("\n--> "))
        
        if opt == 1:
            num_of_seats = int(input("Enter number of seats required: "))
            seat_cat = str(input("Desired seat category(TWIN, VIP, VVIP, ECONOMY): "))
            #print(avaiable seats)
            print("Select seat from these below")
            seatsAvailablePerCat(seat_cat.upper(),movieNameSelected)
            #update file for the movie using movie name
            print(" ")
            optionList = str(input("Choose seat: "))
            updateSeatsAvailablePercat(optionList,movieNameSelected)
            #update ticket sold and cost value
            updateTicketAndRevenue(optionList,seat_cat.upper(),movieNameSelected,num_of_seats,TicketSoldDictPermovie,
                                   RevenueDictPerMovie)
            
            #Back to main menu
            menu()

    if option == 2:
        print("\nMovie seat charts and general report...\n")
        print("1. General Report.")
        print("2. Movies seat Charts.")
        print("3. back.")

        opt = int(input("\n--> "))
        
        bookedMoviesList = []
        ticketsList = []
        revenueList = []
        
        info= moviesBooked(movies)
        bookedMoviesList = info[0].split(",")
        ticketsList = info[3]
        revenueList = info[4]
        if opt == 1:
            print("\n**********GENERAL REPORT*********\n")
            #movies booked ; all movies
            print(" Movies Booked: ",info[0])
            #tikets Solved generally
            print(" Number of Tickets Sold: ",info[2])
            #revenue expected
            print(" Expected Revenue : shs ",info[1])
            
            #Back to main menu
            menu()
            
        if opt == 2:
            print("\n**********SEATS CHART*********\n")
            #movies chats with stats
            for i in range(len(bookedMoviesList)):
                movie = bookedMoviesList[i]
                print("MOVIE: ", movie)
                printChart(movie)
                print("Available Seats: ", 320-ticketsList[i])
                print("Expected Revenue: ", revenueList[i], "\n")
            
            #Back to main menu
            menu()

        if opt == 3:
            #Back to main menu
            menu()
            
    #option 3

    if option == 4:
        print("\nReset sitting plan...\n")
        print("1. RESET all seats")

        opt = int(input("\n--> "))

        if opt == 1:
            print("\n**********RESETING*********\n")
            #resetting
            f = open('created_or_not.txt', 'w+')
            alist = f.write("FALSE")
            f.close()
            print("...........Done resetting, run app again.......\n")
            exit()
            
            menu()

    if option == 5:
        print("\nExiting..................\n")
        exit()


   
