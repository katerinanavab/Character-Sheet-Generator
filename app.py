import json
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/class/<class_name>')
def class_page(class_name):
    with open('static/alignments.json', 'r') as f:
        alignment_options = json.load(f)
    with open('static/backgrounds.json', 'r') as f:
        background_options = json.load(f)
    with open('static/species.json', 'r') as f:
        species_options = json.load(f)
    return render_template(f'classes/{class_name}.html', class_name=class_name, alignment_options=alignment_options, background_options=background_options, species_options=species_options)

@app.route('/submit', methods=['POST'])
def submit():
    # Collect form data
    name = request.form.get('input_name')
    if not name:
        name = 'Tav'
    origin_data = {
        'name': name,
        'species': request.form.get('selected_species'),
        'background': request.form.get('selected_background'),
        'alignment': request.form.get('selected_alignment')
    }
    print(f"Received form data: {origin_data}")
    return render_template('sheet.html', user_data=origin_data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9999, debug=True)
