from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def page2():
    if (request.method == "POST"):
        name = request.form.get('name')
        nu = request.form.get('num')
        return name+nu
    return render_template("satya.html")


app.run(debug=True)
