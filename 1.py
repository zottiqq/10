from flask import *
import datetime as dt

app = Flask(__name__)


@app.route('/')
def index():
    time_today = dt.datetime.today()
    time_now = time_today.strftime('%H:%M')
    if (time_now > '6:00') and (time_now < '12:00'):
        time = 'Доброе утро!'
    elif (time_now > '12:00') and (time_now < '18:00'):
        time = 'Доброе день!'
    elif (time_now > '18:00') and (time_now < '24:00'):
        time = 'Добрый вечер!'
    elif (time_now > '0:00') and (time_now < '6:00'):
        time = 'Доброй ночи!'
    return render_template('indx.html', time=time)

if __name__ == '__main__':
    app.run()