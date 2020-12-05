import re
import psycopg2
import os
from werkzeug.security import generate_password_hash, check_password_hash


dsn = os.environ.get('DATABASE_URL')
conn = psycopg2.connect(dsn)
conn.set_client_encoding('utf-8')
cur = conn.cursor()


def userInput(userID, passWord):
    # 利用者名は英数字と"_"のみ
    if re.search('\W', userID):
        return 2
    # パスワードに英数字が1文字も含まれていない
    if re.search('[a-zA-Z0-9]', passWord) == None:
        return 3
    # パスワードの長さ制限
    if len(passWord) < 8:
        return 4
    if len(passWord) > 16:
        return 5

    # パスワードをハッシュ化
    passWord = generate_password_hash(passWord)

    while True:
        try:
            conn = psycopg2.connect(dsn)
            conn.set_client_encoding('utf-8')
            cur = conn.cursor()
            cur.execute('SELECT userid FROM info WHERE userid = %s', (userID,))
        except psycopg2.InterfaceError:
            continue

        break

    if cur.rowcount == 1:
        cur.close()
        conn.close()
        return 1
    elif (cur.rowcount == 0):
        cur.execute('INSERT INTO info (userid, password) VALUES (%s, %s)', (userID, passWord))
        conn.commit()
        cur.close()
        conn.close()
        return 0



def userOutput(userID, passWord):
    while True:
        try:
            conn = psycopg2.connect(dsn)
            conn.set_client_encoding('utf-8')
            cur = conn.cursor()
            cur.execute('SELECT password FROM info WHERE userid = %s', (userID,))
        except psycopg2.InterfaceError:
            continue

        break


    if cur.rowcount == 0:
        return 1
    else:
        data = cur.fetchone()
        
        if check_password_hash(data[0], passWord) == 1:
            return 0
        
        return 1

