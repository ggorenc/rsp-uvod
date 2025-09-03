import random
from flask import Flask, render_template, request
#pip install flask
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", spr="karkoli")

app.route("/calclove", methods=["POST"])
def calclove():
    tmp=dict(request.form)
    ime1=tmp.get("ime1")
    ime2=tmp.get("ime2")
    r=f"{ime1}+{ime2}={random.randint(0,100)} %"

    if len(ime1)==0 or len(ime2)==0:
        return "0%"
    
    if ime1=="mark":
        return f"{ime1}+{ime2}={random.randint(90,100)} %"
    
    if ime1=="jovan":
        return f"{ime1}+{ime2}={random.randint(0,5)} %"
    
    return render_template("index.html", rezultat=r)

app.run(debug=True)