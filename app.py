from flask import *
from werkzeug.exceptions import BadRequestKeyError
from src.calendrier import calendar
from src.login import userInput, userOutput
from src.registSchedule import register, registerDate, deleteSchedule
from src.registedSchedule import registed
from src.scheduleList import scheList
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'calendar key'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        # ログイン画面に遷移
        return render_template('login.html')

    try:
        back = request.form['back']
    except BadRequestKeyError:
        pass

    # ログインフォームから送られてきた、ユーザー名とパスワードを取得
    userID = request.form['userID']
    passWord = request.form['password']

    # DBと接続
    db = userOutput(userID, passWord)

    # ユーザー名とパスワードのチェック
    error_message = None
    if not userID:
        error_message = 'ユーザー名の入力は必須です'
    elif not passWord:
        error_message = 'パスワードの入力は必須です'
    elif db == 1:
        error_message = 'ユーザー名もしくはパスワードが正しくありません'

    if error_message is not None:
        # エラーがあればそれを表示したうえでログイン画面に遷移
        flash(error_message, category='alert alert-info')
        return redirect(url_for('login'))

    # エラーがなければ、セッションにユーザーIDを追加してインデックスページへ遷移
    session.clear()
    session['username'] = userID
    #flash('{}さんとしてログインしました'.format(userID), 'message')

    return redirect(url_for('home', userID=userID))


@app.route('/createUser', methods=['GET', 'POST'])
def createUser():
    if request.method == 'GET':
        # ユーザー登録画面に遷移
        return render_template('createUser.html')

    # 登録フォームから送られてきた、ユーザー名とパスワードを取得
    userID = request.form['userID']
    passWord = request.form['password']


    # DBと接続
    db = userInput(userID, passWord)

    # エラーチェック
    error_message = None
    if not userID:
        error_message = 'ユーザー名の入力は必須です'
    elif not passWord:
        error_message = 'パスワードの入力は必須です'
    elif db == 1:
        error_message = 'ユーザー名 {} はすでに使用されています'.format(userID)
    elif db == 2:
        error_message = 'ユーザー名は英数字とアンダーバーのみ使用できます'
    elif db == 3:
        error_message = 'パスワードには英数字を1字以上含めてください'
    elif db == 4:
        error_message = 'パスワードが短いです'
    elif db == 5:
        error_message = 'パスワードが長いです'

    # エラーがあれば、それを画面に表示させる
    if error_message is not None:
        flash(error_message, category='alert alert-info')
        return redirect(url_for('createUser'))

    # ログイン画面へ遷移
    flash('ユーザー登録が完了しました。登録した内容でログインしてください', category='alert alert-info')
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    # ログアウトする
    session.clear()
    flash('ログアウトしました', category='alert alert-info')
    return redirect(url_for('login'))


@app.route('/home/<userID>', methods=['GET', 'POST'])
def home(userID):
    try:
        year = int(request.form['year'])
        month = int(request.form['month'])
        hinichi = 0

    except BadRequestKeyError:
        time = datetime.now()
        year = time.year
        month = time.month
        hinichi = time.day

    try:
        logoff = request.form['logout']
        return redirect(url_for('logout'))
    except BadRequestKeyError:
        pass

    try:
        start_time = datetime.strptime(request.form['delete'], '%Y-%m-%d %H:%M:%S')
        deleteSchedule(userID, start_time)
        flash('削除しました', category='alert alert-info')
        return render_template('deleteSchedule.html', userID=userID)
    except BadRequestKeyError:
        pass

    kalendae = calendar(year, month)
    #print(kalendae)

    day_stars = []
    for week in kalendae:
        for day in week:
            if day <= 0:
                continue

            date = datetime(int(year), int(month), int(day))
            day_stars.append(registed(userID, date))

    return render_template('home.html', userID=userID, year=year, month=month, 
        hinichi=hinichi, kalendae=kalendae, day_stars=day_stars)


@app.route('/schedule/<userID>/<year>/<month>', methods=['GET', 'POST'])
def schedule(userID, year, month):
    day = int(request.form['day'])
    return render_template('schedule.html', userID=userID, year=int(year), month=int(month), day=day)


@app.route('/regist/<userID>/<year>/<month>/<day>', methods=['GET', 'POST'])
def regist(userID, year, month, day):
    try:
        back = request.form['back']
        return redirect(url_for('home', userID=userID))
    except BadRequestKeyError:
        pass

    try:
        start_hour = int(request.form['start_hour'])
        start_minute = int(request.form['start_minute'])
        end_hour = int(request.form['end_hour'])
        end_minute = int(request.form['end_minute'])
        content = request.form['content']
    except BadRequestKeyError:
        flash('選択または入力していない項目があります', category='alert alert-info')
        return render_template('schedule.html', userID=userID, year=int(year), month=int(month), day=int(day))


    start_time = datetime(int(year), int(month), int(day), start_hour, start_minute) #開始時刻
    #print(start_time)
    end_time = datetime(int(year), int(month), int(day), end_hour, end_minute)       #終了時刻
    date = datetime(int(year), int(month), int(day)) #予定の日付
    #print('date:', date)
    
    if start_time >= end_time:
        flash('開始時刻が終了時刻よりも遅いです', category='alert alert-info')
        return render_template('schedule.html', userID=userID, year=int(year), month=int(month), day=int(day))

    if register(userID, start_time, end_time, content) == 0:
        registerDate(userID, date, content)
        flash('予定が登録されました', category='alert alert-info')
    else:
        flash('予定の時刻が重なっています', category='alert alert-info')
        return render_template('schedule.html', userID=userID, year=int(year), month=int(month), day=int(day))

    return render_template('regist.html', userID=userID)


@app.route('/scheduleList/<userID>/<year>/<month>', methods=['POST'])
def scheduleList(userID, year, month):
    day = int(request.form['list'])
    date = datetime(int(year), int(month), day)
    schedules = scheList(userID, date)
    return render_template('scheduleList.html', userID=userID, schedules=schedules)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port)