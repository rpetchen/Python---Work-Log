import datetime
import re


def searchByDate(logList):

    foundLogList = []
    searchActive = True
    while searchActive:
        dateInput = input("""Enter the date\nPlease use MM/DD/YYYY: """)

        try:
            convertedInput = datetime.datetime.strptime(
                dateInput, '%m/%d/%Y').date()

            for log in logList:
                if log.getTaskDate() == convertedInput:
                    foundLogList.append(log)
        except ValueError as e:
            print("Error: {} doesn't seem to be a valid date\n".format(dateInput))

        if foundLogList:
            searchActive = False
            displayResults(foundLogList)

        elif not foundLogList:
            searchActive = False
            inp = input("No results. Press enter to return to search menu")


def searchByRegex(logList):

    foundLogList = []
    searchActive = True

    while searchActive:

        regexInput = input("""Enter regex patter: """)

        for log in logList:

            titleSearch = re.search(regexInput, log.getTaskTitle())

            noteSearch = re.search(regexInput, log.getTaskNotes())

            if titleSearch or noteSearch:
                foundLogList.append(log)

        if foundLogList:
            searchActive = False
            displayResults(foundLogList)

        elif not foundLogList:
            searchActive = False
            inp = input("No results. Press enter to return to search menu")

def searchByString(logList):

    foundLogList = []
    searchActive = True

    while searchActive:

        stringInput = input("""Enter search term: """)

        for log in logList:

            if log.getTaskTitle().find(stringInput) != -1 or \
                    log.getTaskNotes().find(stringInput) != -1:

                foundLogList.append(log)

        if foundLogList:
            searchActive = False
            displayResults(foundLogList)

        elif not foundLogList:
            searchActive = False
            inp = input("No results. Press enter to return to search menu")

def searchByTimeSpent(logList):

    foundLogList = []
    searchActive = True

    while searchActive:

        timeInput = input("""Enter minutes spent: """)

        try:
            timeInput = int(timeInput)
        except:
            print("Time spent should be in whole numbers")


        if type(timeInput) == int:
            for log in logList:

                if log.getTimeSpent() == timeInput:
                    foundLogList.append(log)

            if foundLogList:
                searchActive = False
                displayResults(foundLogList)

            elif not foundLogList:
                searchActive = False
                inp = input("No results. Press enter to return to search menu")

def displayResults(logList):

    logIter = 0

    while True:
        log = logList[logIter]
        print("""
        Date: {},
        Title: {},
        Time Spent: {},
        Notes: {},""".format((log.getTaskDate().strftime("%m/%d/%Y")), (log.getTaskTitle()),
                             (log.getTimeSpent()), (log.getTaskNotes())))

        print("\nResults {} of {}".format((logIter + 1), (len(logList))))

        displayOption = input("[P]revious, [N]ext, [R]eturn to search menu")

        if displayOption.lower() == "p":
            if logIter > 0:
                logIter -= 1
            else:
                print("No Previous Results!")
        elif displayOption.lower() == "n":
            if len(logList) > logIter + 1:
                logIter += 1
            else:
                print("No More Results")
        elif displayOption.lower() == "r":
            break
        else:
            print("Option not recognized")
