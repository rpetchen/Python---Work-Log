from workLog import workLog
from createUtil import collectTaskDate, collectTaskNotes, collectTaskTitle, \
    collectMinutes
from workLogDAO import workLogDAO
from searchUtil import searchByDate, searchByRegex, searchByString


def main():

    workLogInit()


def workLogInit():

    logDAO = workLogDAO()

    while True:
        optionMain = \
            input("""What would you like to do?

        a) Add new entry
        b) Search in existing entries
        c) Quit program
        """)

        if optionMain.lower() == 'a':
            createWorkLog(logDAO)
        elif optionMain.lower() == 'b':
            searchWorkLog(logDAO)
        elif optionMain.lower() == 'c':
            print("Good-Bye!")
            break
        else:
            print('Invalid option selected.\n')


def createWorkLog(logDAO):

    taskDate = collectTaskDate()

    taskTitle = collectTaskTitle()

    taskNotes = collectTaskNotes()

    timeSpent = collectMinutes()

    log = workLog(taskTitle, timeSpent, taskDate, taskNotes)

    logDAO.addWorkLog(log)


def searchWorkLog(logDAO):

    logList = logDAO.getWorkLog()

    while True:
        searchOption = \
            input("""Do you want to search by:

                a) Exact Date
                b) Exact Search
                c) Regex Pattern
                d) Return to menu
                """)

        if searchOption.lower() == 'a':
            searchByDate(logList)
        elif searchOption.lower() == 'b':
            searchByString(logList)
        elif searchOption.lower() == 'c':
            searchByRegex(logList)
        elif searchOption.lower() == 'd':
            break
        else:
            print('Invalid option selected.\n')


main()
