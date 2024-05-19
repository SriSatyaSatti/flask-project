from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from flask import Flask, render_template, redirect, url_for, request, flash, session
from sklearn.datasets import load_iris
import numpy as np
dataset = load_iris()
x = dataset.data
y = dataset.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
modelGNB = GaussianNB()
modelGNB.fit(x_train, y_train)
y_pred = modelGNB.predict(x_test)

app = Flask(__name__)
app.secret_key = "satya"


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
        arr = np.array([[int(p1), int(p2), int(s1), int(s2)]])
        output = modelGNB.predict(arr)
        t = int(output[0])
        if t == 0:
            output = "Setosa"
        elif t == 1:
            output = "Versicolor"
        else:
            output = "verginica"
        return render_template("page2.html", p1=p1, p2=p2, s1=s1, s2=s2, result=y_pred, output=output)


app.run(debug=True)
