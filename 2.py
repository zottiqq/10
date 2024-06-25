from flask import *

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('indxe.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        task = request.form.get('task')
        if task:
            tasks.append(task)
        return redirect(url_for('indxe'))
    return render_template('add_post.html')



if __name__ == '__main__':
    app.run()