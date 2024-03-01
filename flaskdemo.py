from flask import Flask, render_template, request
import os
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    phone = request.form['phone']

    # Create a folder if it doesn't exist
    folder_path = 'data'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Save data to a JSON file
    data = {'username': username, 'phone': phone}
    with open(f'{folder_path}/{username}.json', 'w') as f:
        json.dump(data, f)

    return 'Data saved successfully!'

if __name__ == '__main__':
    app.run(debug=True)
