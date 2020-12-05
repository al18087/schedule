import re
import psycopg2
import os
from datetime import datetime


dsn = os.environ.get('DATABASE_URL')
conn = psycopg2.connect(dsn)
conn.set_client_encoding('utf-8')
cur = conn.cursor()

def register(userID, start_time, end_time, content):
    flag = 0
    cur.execute('SELECT * FROM schedule WHERE userid = %s'
        'AND starttime >= %s AND starttime <= %s',
        (userID, start_time, end_time))

    if cur.rowcount >= 1:
        flag = 1

    cur.execute('SELECT * FROM schedule WHERE userid = %s'
        'AND endtime >= %s AND endtime <= %s',
        (userID, start_time, end_time))

    if cur.rowcount >= 1:
        flag = 1

    cur.execute('SELECT * FROM schedule WHERE userid = %s'
        'AND starttime <= %s AND endtime >= %s',
        (userID, start_time, end_time))

    if cur.rowcount >= 1:
        flag = 1

    cur.execute('SELECT * FROM schedule WHERE userid = %s'
        'AND starttime >= %s AND endtime <= %s',
        (userID, start_time, end_time))

    if cur.rowcount >= 1:
        flag = 1
    
    if flag == 0:
        cur.execute('INSERT INTO schedule (userid, starttime, endtime, content)'
            'VALUES (%s, %s, %s, %s)', (userID, start_time, end_time, content))
        conn.commit()
        return 0
    
    return 1



def registerDate(userID, date, content): 
    cur.execute('INSERT INTO scheduledate (userid, hinichi, content)'
        'VALUES (%s, %s, %s)', (userID, date, content))
    conn.commit()


def deleteSchedule(userID, start_time):
    year = int(start_time.year)
    month = int(start_time.month)
    day = int(start_time.day)
    #hour = int(start_time.hour)
    #minute = int(start_time.minute)
    #start_time = datetime(year, month, day, hour, minute)
    cur.execute('SELECT content FROM schedule WHERE userid = %s'
        'AND starttime = %s',
        (userID, start_time))
    content = cur.fetchone()[0]
    
    cur.execute('DELETE FROM schedule WHERE userid = %s'
        'AND starttime = %s',
        (userID, start_time))
    conn.commit()


    start_date = datetime(year, month, day)

    cur.execute('DELETE FROM scheduledate WHERE userid = %s'
        'AND hinichi = %s AND content = %s',
        (userID, start_date, content))
    conn.commit()



