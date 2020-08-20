import registry as reg
import applicationhandle as app
directory = names = []
matchNames = matchDir = []
uInput = ""

def inputFromUser(userInput):
    global uInput, names, directory
    uInput = userInput
    r_names, r_directory = reg.giveAllData()
    names = r_names
    directory = r_directory
    return filterInput()

def filterInput():
    index = 0
    matchIndex = []
    global uInput, names, directory, matchNames, matchDir
    print("User:",uInput)
    if len(names) != 0 and len(directory) != 0 and uInput != "":
        print(len(names))
        for name in names:
            if name.lower().find(uInput.lower()) > -1:
                print("Match:",name)
                matchIndex.append(index)
            index += 1
        if len(matchIndex) > 10:
            print("Too much.")
            return ("Too much")
        elif len(matchIndex) < 10 and len(matchIndex) > 0:
            temp_match = []
            for index in matchIndex:
                temp_match.append(names[index])
                # matchNames.append(names[index]) when using this   names as well as directory is added in same "matchNames" list so i used temporary list
                matchDir.append(directory[index])
            print("Can handle.")
            matchNames = temp_match
            return ("Can handle", matchNames)
        elif len(matchIndex) == 1:
            print("Match Found.")
            return ("Match Found")
        else:
            print("No match.")
            return ("No match")
    else:
        return ("ERROR")

def filterResponse(response):
    if response > -1:
        # Now Select the application from directory and open it.
        print("Selected app: {} | Directory: {}".format(matchNames[response],matchDir[response]))
        app.openApplication(matchNames[response], matchDir[response])
    else:
        print("Selected app:",matchNames[response])
        app.openApplication(matchNames[0], matchDir[0])
    


