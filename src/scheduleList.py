import psycopg2
import os
from datetime import datetime

"""
conn = psycopg2.connect(
    user = 'calendaruser',
    password = 'kn8@Noda',
    dbname = 'calendar',
    port = 5432
)
"""
dsn = os.environ.get('DATABASE_URL')
conn = psycopg2.connect(dsn)
conn.set_client_encoding('utf-8')
cur = conn.cursor()

def contentInSchedule(userID, date):
    cur.execute('SELECT content FROM nodadate WHERE userID = %s AND hinichi = %s', (userID, date))
    contents = []
    for content in cur.fetchall():
        contents.append(content[0])
    return contents


def scheList(userID, date):
    contents = contentInSchedule(userID, date)

    schedules = []
    for content in contents:
        schedule_info = []
        cur.execute('SELECT * FROM schedule WHERE userID = %s AND content = %s', (userID, content))
        
        for row in cur.fetchall():
            if (row[1].year == date.year) and (row[1].month == date.month) and (row[1].day == date.day):
                schedule_info.append(row[0])
                schedule_info.append(row[1])
                schedule_info.append(row[2])
                schedule_info.append(row[3])

        schedules.append(schedule_info)

    return schedules
