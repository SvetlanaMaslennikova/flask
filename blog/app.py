from flask import Flask

app = Flask(__name__)

count = 0

@app.route('/')
def index():
    global count
    count += 1
    return f'Посещений: {count}'
