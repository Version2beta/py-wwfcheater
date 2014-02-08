from flask import Flask, jsonify
from twords import Twords

app = Flask(__name__)

app.debug = True
app.host = "0.0.0.0"

t = Twords()

@app.route('/health')
def health():
    return "OK\n"

@app.route('/matches/<tiles>', defaults = {'required': ''})
@app.route('/matches/<tiles>/', defaults = {'required': ''})
@app.route('/matches/<tiles>/<required>')
def matches(tiles, required):
    return jsonify(matches = t.matches(tiles, required))

if __name__ == '__main__':
    print "Hi, I'm %s and I'm here to help you." % __name__
    app.run(host = app.host)
