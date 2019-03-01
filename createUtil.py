import datetime


def collectTaskDate():

    while True:
        dateInput = input("""Date of the task
        Please use MM/DD/YYYY:
        """)
        try:
            dateTime = datetime.datetime.strptime(dateInput, '%m/%d/%Y').date()
            print(dateTime)
            return dateTime
        except ValueError as e:
            print("Invalid Date Format")


def collectTaskTitle():

    titleProvided = False
    while not titleProvided:
        titleInput = input("""Task Title: """)

        if titleInput:
            titleProvided = True
            return titleInput
        else:
            print("Title is a mandatory field")


def collectTaskNotes():
    taskNotes = input("Task Notes (Optional): ")
    return taskNotes


def collectMinutes():

    minutesValid = False

    while not minutesValid:
        minutes = input("Enter Task Minutes: ")

        try:
            return int(minutes)

        except BaseException:
            print("Enter only whole numbers")
