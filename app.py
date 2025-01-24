from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')  # Or a separate homepage template

@app.route('/class/<class_name>')
def class_page(class_name):
    valid_classes = ['barbarian', 'wizard', 'rogue']  # Add all valid classes
    if class_name not in valid_classes:
        return "Class not found", 404
    return render_template(f'classes/{class_name}.html', class_name=class_name)

if __name__ == '__main__':
    app.run(debug=True)
