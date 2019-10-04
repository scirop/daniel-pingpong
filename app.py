from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/ping")
def pong():
    return jsonify({'data':'pong'})

    
@app.errorhandler(404)
def page_not_found(e):
    return 'Use /ping endpoint', 404


if __name__=='__main__':
    app.run()