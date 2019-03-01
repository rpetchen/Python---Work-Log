
class workLog():

    def __init__(self, taskTitle, timeSpent, taskDate, taskNotes):

        self.taskTitle = taskTitle
        self.timeSpent = timeSpent
        self.taskDate = taskDate

        if taskNotes:
            self.taskNotes = taskNotes
        elif not taskNotes:
            self.taskNotes = ""

    def getTaskTitle(self):
        return self.taskTitle

    def getTimeSpent(self):
        return self.timeSpent

    def getTaskDate(self):
        return self.taskDate

    def getTaskNotes(self):
        if self.taskNotes:
            return self.taskNotes
        else:
            return None
