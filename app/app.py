from flask import Flask, render_template
from flask_sockets import Sockets

app = Flask(__name__)
sockets = Sockets(app)

@app.route('/')
def index():
    return render_template('index.html', title='EMArgency')

@sockets.route('/echo')
def echo_socket(ws):
    while True:
        message = ws.receive()
        ws.send(message)

if __name__ == '__main__':
    app.run(debug=True, port=8000, host="0.0.0.0")
