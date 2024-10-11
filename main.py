from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

# Startseite
@app.route('/')
def index():
    return render_template('index.html')  # Stelle sicher, dass du diese Datei erstellst

# Nachrichten-Handling über WebSockets
@socketio.on('message')
def handle_message(msg):
    print(f"Message: {msg}")
    send(msg, broadcast=True)  # Nachricht an alle verbundene Clients senden

if __name__ == '__main__':
    socketio.run(app)
