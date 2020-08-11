from flask import Flask, render_template, jsonify, request
from flask_bootstrap import Bootstrap
from getweather import showweather
import pycountry


app = Flask(__name__)
Bootstrap(app)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result")
def result():
    city = request.args.get('city')
    country = request.args.get('country')
    code_country = pycountry.countries.get(name = country).alpha_2
    Todays_weather = showweather(city,code_country)
    return render_template('result.html',result=Todays_weather)





if __name__ == '__main__':
    app.run(debug=True)