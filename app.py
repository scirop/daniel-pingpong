from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/ping")
def pong():
    return jsonify({'data':'pong'})

if __name__=='__main__':
    app.run()
