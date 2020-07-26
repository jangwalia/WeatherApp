from flask import Flask, render_template, jsonify
from flask_bootstrap import Bootstrap
from getweather import showweather
app = Flask(__name__)
Bootstrap(app)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result")
def result():
    weather = showweather()
    return jsonify(weather)

if __name__ == '__main__':
    app.run(debug=True)