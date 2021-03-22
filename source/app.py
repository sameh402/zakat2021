from flask import Flask, render_template, request
from functions.gold import gold
from functions.plants import plants
from functions.money import money

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def landing_page():
    return render_template("intro.html")
@app.route("/zakat1.html", methods=["POST", "GET"])
def zakat1():
    return render_template("zakat1.html")
@app.route("/zakat2.html", methods=["POST", "GET"])
def zakat2():
    return render_template("zakat2.html")

@app.route("/calc1", methods=["POST", "GET"])
def calculation():
    a = float(request.form["x"])
    c = float(request.form["y"])
    z=money(c)-gold(a)
    my_result = z
    if(my_result<0):
    	return render_template("error.html")
    return render_template("zakat1.html", result=money(c)*(1/40))
@app.route("/calc2", methods=["POST", "GET"])
def calculation1():

    b = float(request.form["q"])
    z=plants(b)
    my_result2 = z
    return render_template("zakat2.html", result=my_result2)


if __name__=="__main__":
    app.run(debug=True)