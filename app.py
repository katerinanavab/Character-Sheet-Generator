from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/class/<class_name>')
def class_page(class_name):
    return render_template(f'classes/{class_name}.html', class_name=class_name)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5421, debug=True)
