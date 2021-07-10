import socketio

sio = socketio.Client()
sio.connect("http://localhost:5000")
print("my sid is", sio.sid)
sio.emit("from-cli", "data from cli")
print("done")
sio.disconnect()
