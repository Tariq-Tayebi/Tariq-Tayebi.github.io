from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def index():
    messages = []
    with open('messages.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            messages.append({'username': row[0], 'message': row[1]})
    return render_template('index.html', messages=messages)

@app.route('/send', methods=['POST'])
def send():
    username = request.form['username']
    message = request.form['message']
    with open('messages.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, message])
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
