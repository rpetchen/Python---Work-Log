import os.path
import csv
import datetime
from workLog import workLog


class workLogDAO():

    WORK_LOG_FILE = 'workLog.csv'

    def addWorkLog(self, workLog):

        fileExists = os.path.isfile(workLogDAO.WORK_LOG_FILE)

        if fileExists is False:
            with open(workLogDAO.WORK_LOG_FILE, "w", newline='') as f:
                writer = csv.writer(f)
                row = ['task_date', 'task_title', 'task_notes', 'time_spent']
                writer.writerow(row)

        with open(workLogDAO.WORK_LOG_FILE, 'a', newline='') as f:
            writer = csv.writer(f)
            row = [
                workLog.getTaskDate(),
                workLog.getTaskTitle(),
                workLog.getTaskNotes(),
                workLog.getTimeSpent()]
            writer.writerow(row)

    def getWorkLog(self):

        workLogList = []

        fileExists = os.path.isfile(workLogDAO.WORK_LOG_FILE)

        if fileExists is False:

            print("No Work Log's Available.")

        else:
            f = open(workLogDAO.WORK_LOG_FILE)
            csv_f = csv.DictReader(f)

            for row in csv_f:

                taskTitle = row['task_title']
                taskNotes = row['task_notes']
                timeSpent = row['time_spent']
                taskDate = datetime.datetime.strptime(
                    row['task_date'], '%Y-%m-%d').date()

                log = workLog(taskTitle, int(timeSpent), taskDate, taskNotes)

                workLogList.append(log)

            workLogList.sort(key=lambda x: x.getTimeSpent())
            return workLogList
