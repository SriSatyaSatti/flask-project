from flask import Flask, render_template, request, redirect, url_for,flash,session
app = Flask(__name__)
app.secret_key="satya"
name="satya"
@app.route('/')
def fun1():    
    return render_template("satya.html")



@app.route('/page3', methods=["POST", "GET"])
def page3():
    if (request.method == "POST"):
        name = request.form.get("name")
        if(name=="satya"):
           return render_template("page3.html",x=name)
        else:
            flash("wrong!!","warning")
            return render_template("satya.html")


app.run(debug=True)
