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

def registed(userID, date):
    cur.execute('SELECT * FROM scheduledate WHERE userID = %s AND day = %s', (userID, date))
    for row in cur.fetchall():
        if row[1] == None:
            break
        return row[1].day

    return -1
        