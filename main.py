import filter, sys

def userInput():
    uInput = ""
    while True:
        uInput = str(input("Application name: "))
        if uInput == "":
            uInput = userInput()
        else:
            break
    return uInput

if __name__ == "__main__":
    uInput = userInput()
    response = filter.inputFromUser(uInput)
    if response[0] == "Too much":
        print("You have to be more specific, too much matches found.")
        print("Try again")
    elif response[0] == "Can handle":
        index = 0
        match_list = response[1]
        list_length = len(match_list)
        print("Total Match",list_length)
        if list_length == 1:
            filter.filterResponse(-1)
            sys.exit(-1)
        print("Matches found Select one of them.")
        while index < len(match_list):
            print(str(index + 1) + ": " + match_list[index])
            index += 1
        response = int(input(">> "))
        if response - 1 < list_length:
            try:
                filter.filterResponse(response - 1)
            except:
                print("Inappropriate selection.")
                print("Try again.")
                sys.exit(-1)
        else:
            print("Inappropriate selection.")
            print("Try again.")
            sys.exit(-1)

    elif response[0] == "Match Found":
        filter.filterResponse(-1)
        pass
    elif response[0] == "No match":
        print("Unable to find the application.")
        sys.exit(-1)
    else:
        print("Unexpected problem")
        sys.exit(-1)
