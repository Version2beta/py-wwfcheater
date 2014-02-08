from flask import Flask, jsonify
from twords import Twords

app = Flask(__name__)

app.debug = True
app.host = "0.0.0.0"

@app.route('/health')
def health():
    return "OK\n"

@app.route('/matches/<tiles>')
def matches(tiles):
    t = Twords()
    return jsonify(matches = t.matches(tiles))

@app.route('/matches/<tiles>/<musts>')
def musts(tiles, musts):
    t = Twords
    return jsonify(matches = t.matches(tiles, musts))

if __name__ == '__main__':
    print "Hi, I'm %s and I'm here to help you." % __name__
    app.run(host = app.host)
