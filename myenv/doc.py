from flask import Flask, render_template, redirect, url_for, request, flash, session

app = Flask(__name__)
app.secret_key = "satya"

li1 = ["satya", "mahi"]
li2 = ["123", "123"]


@app.route('/')
def fun1():
    return render_template("ml.html")


@app.route('/sub', methods=["POST", "GET"])
def fun2():
    if (request.method == "POST"):
        p1 = request.form.get('petal length')
        p2 = request.form.get('petal width')
        s1 = request.form.get('sepal length')
        s2 = request.form.get('sepal width')
        return render_template("page2.html", p1=p1, p2=p2, s1=s1, s2=s2)


@app.route('/newsub', methods=["POST", "GET"])
def fun9():
    if (request.method == "POST"):
        li1.append(request.form.get('name'))
        li2.append(request.form.get('pas'))


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/new')
def new():
    return render_template("new.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


app.run(debug=True)
