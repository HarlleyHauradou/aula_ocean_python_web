from flask import Flask

app = Flask('meu app')

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/thanks')
def thanks():
    return '<h1>Valeu professor e galera OCEAN</h1>'