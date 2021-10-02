from flask import Flask,render_template,request,session
import pandas as pd
from sklearn.model_selection import train_test_split
import joblib


app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')





@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

@app.route('/prediction1',methods = ['POST','GET'])
def prediction1():
    a = []
    if request.method == "POST":
        date = (request.form['date'])
        prevclose = (request.form['pclose'])
        open = (request.form['open'])
        high = (request.form['high'])
        low = (request.form['low'])
        last = (request.form['last'])
        close = (request.form['close'])
        vwap = (request.form['vwap'])
        vol = (request.form['vol'])

        a.extend([date,prevclose,open,high,low,last,close,vwap,vol])
        model = joblib.load("datamodel56.pkl")
        y_pred = model.predict([a])
        return render_template('prediction.html',msg = "done",op=y_pred)
    return render_template("prediction.html")




if __name__ == '__main__':
    app.run(debug=True)