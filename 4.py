from flask import *

app = Flask(__name__)

# Список товаров на складе
table = [
    {'name': 'Банан', 'description': 'Фрукт', 'weight': 0.3, 'quantity': 545, 'price': 35.0},
    {'name': 'Клубника', 'description': 'Ягода', 'weight': 0.05, 'quantity': 1500, 'price': 33.0},
    {'name': 'Арбуз', 'description': 'Ягода', 'weight': 1.5, 'quantity': 650, 'price': 45.0},
]

@app.route('/')
def index():
    return render_template('table.html', table=table)

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.form['name']
        description = request.form['description']
        weight = float(request.form['weight'])
        quantity = int(request.form['quantity'])
        price = float(request.form['price'])

        # Добавляем новый товар в список
        new_item = {
            'name': name,
            'description': description,
            'weight': weight,
            'quantity': quantity,
            'price': price
        }
        table.append(new_item)

        # Перенаправляем на главную страницу
        return redirect(url_for('indxe'))
    return render_template('additem.html')

if __name__ == '__main__':
    app.run()