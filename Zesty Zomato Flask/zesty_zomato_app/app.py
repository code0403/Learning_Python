import json
from flask import Flask, render_template, request, redirect, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'


def load_data_from_json():
    with open('data.json') as json_file:
        data = json.load(json_file)
    return data


def save_data_to_json(data):
    with open('data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/menu')
def menu():
    data = load_data_from_json()
    return render_template('menu.html', menu=data['menu'])


@app.route('/menu/add', methods=['GET', 'POST'])
def add_menu_item():
    if request.method == 'POST':
        data = load_data_from_json()

        dish_name = request.form['dish_name']
        price = float(request.form['price'])
        availability = request.form['availability']

        new_menu_item = {
            'id': len(data['menu']) + 1,
            'name': dish_name,
            'price': price,
            'availability': availability
        }

        data['menu'].append(new_menu_item)
        save_data_to_json(data)

        flash('Menu item added successfully!')
        return redirect('/menu')

    return render_template('add_menu.html')


@app.route('/menu/edit/<int:menu_id>', methods=['GET', 'POST'])
def edit_menu_item(menu_id):
    data = load_data_from_json()

    menu_item = next((item for item in data['menu'] if item['id'] == menu_id), None)

    if menu_item:
        if request.method == 'POST':
            dish_name = request.form['dish_name']
            price = float(request.form['price'])
            availability = request.form['availability']

            menu_item['name'] = dish_name
            menu_item['price'] = price
            menu_item['availability'] = availability

            save_data_to_json(data)
            flash('Menu item updated successfully!')
            return redirect('/menu')

        return render_template('edit_menu.html', menu_item=menu_item)

    flash('Menu item not found!')
    return redirect('/menu')


@app.route('/menu/delete/<int:menu_id>', methods=['GET', 'POST'])
def delete_menu_item(menu_id):
    data = load_data_from_json()

    menu_item = next((item for item in data['menu'] if item['id'] == menu_id), None)

    if menu_item:
        if request.method == 'POST':
            data['menu'].remove(menu_item)
            save_data_to_json(data)

            flash('Menu item deleted successfully!')
            return redirect('/menu')

        return render_template('delete_menu.html', menu_item=menu_item)

    flash('Menu item not found!')
    return redirect('/menu')


@app.route('/orders', methods=['GET', 'POST'])
def orders():
    data = load_data_from_json()

    if request.method == 'POST':
        customer_name = request.form['customer_name']
        dish_ids = request.form.getlist('dish_ids')
        dish_order_status = request.form['status']
        print(dish_order_status)

        valid_dish_ids = []
        for dish_id in dish_ids:
            dish = next((item for item in data['menu'] if item['id'] == int(dish_id)), None)
            if dish and dish['availability'] == 'yes':
                valid_dish_ids.append(int(dish_id))

        if len(valid_dish_ids) == len(dish_ids):
            order = {
                'order_id': len(data['orders']) + 1,
                'customer_name': customer_name,
                'dish_ids': valid_dish_ids,
                'status': dish_order_status,
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }

            data['orders'].append(order)
            save_data_to_json(data)

            flash('Order placed successfully!')
            return redirect('/orders')
        else:
            flash('Invalid dish ID(s) or item(s) not available!')
            return redirect('/orders')

    return render_template('orders.html', menu=data['menu'], orders=data['orders'])


@app.route('/orders/update/<int:order_id>', methods=['GET', 'POST'])
def update_order_status(order_id):
    data = load_data_from_json()

    order = next((item for item in data['orders'] if item['order_id'] == order_id), None)

    if order:
        if request.method == 'POST':
            new_status = request.form['status']
            order['status'] = new_status

            save_data_to_json(data)
            flash('Order status updated successfully!')
            return redirect('/orders')

        return render_template('update_order.html', order=order)

    flash('Order not found!')
    return redirect('/orders')


@app.route('/review_orders')
def review_orders():
    data = load_data_from_json()
    return render_template('review_order.html', orders=data['orders'])


@app.route('/exit')
def exit():
    return render_template('exit.html')


if __name__ == '__main__':
    app.run(debug=True)
