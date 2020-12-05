import psycopg2
import os
from datetime import datetime


dsn = os.environ.get('DATABASE_URL')
conn = psycopg2.connect(dsn)
conn.set_client_encoding('utf-8')
cur = conn.cursor()

def contentInSchedule(userID, date):
    cur.execute('SELECT content FROM scheduledate WHERE userid = %s AND hinichi = %s', (userID, date))
    contents = []
    for content in cur.fetchall():
        contents.append(content[0])
    return contents


def scheList(userID, date):
    contents = contentInSchedule(userID, date)

    schedules = []
    for content in contents:
        schedule_info = []

        while True:
            try:
                conn = psycopg2.connect(dsn)
                conn.set_client_encoding('utf-8')
                cur = conn.cursor()
                cur.execute('SELECT * FROM schedule WHERE userid = %s AND content = %s', (userID, content))
            except psycopg2.InterfaceError:
                continue
            break
        
        for row in cur.fetchall():
            if (row[1].year == date.year) and (row[1].month == date.month) and (row[1].day == date.day):
                schedule_info.append(row[0])
                schedule_info.append(row[1])
                schedule_info.append(row[2])
                schedule_info.append(row[3])

        schedules.append(schedule_info)

    return schedules
