from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/class/<class_name>')
def class_page(class_name):
    return render_template(f'classes/{class_name}.html', class_name=class_name)

@app.route('/submit', methods=['POST'])
def submit():
    # Collect form data
    user_data = {
        'name': request.form.get('name'),
        'age': request.form.get('age'),
        'favorite_color': request.form.get('favorite_color'),
        'favorite_hobby': request.form.get('favorite_hobby'),
        'lucky_number': request.form.get('lucky_number')
    }
    return render_template('sheet.html', user_data=user_data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5421, debug=True)
