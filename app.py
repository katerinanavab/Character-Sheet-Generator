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
    name = request.form.get('name')
    if not name:
        name = 'Tav'
    origin_data = {
        'name': name,
        'species': request.form.get('species'),
        'background': request.form.get('background'),
        'alignment': request.form.get('alignment')
    }
    print(f"Received form data: {origin_data}")
    return render_template('sheet.html', user_data=origin_data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9999, debug=True)
