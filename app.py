from flask import Flask, render_template, request
from sklearn.ensemble import RandomForestRegressor
import gunicorn
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/prediction", methods=["GET", "POST"])
def predict():
    if request.method == "POST":

        transmission = request.form['transmission']
        power = request.form['power']
        gap = request.form['gap']
        fuel = request.form['fuel']
        
        res = round(model.predict([[transmission,power,gap,fuel]])[0], 3)

        result = 'Predicted Price is {} Lakh'.format(res) 
        return render_template('result.html', results = result)
        
    else : 
        return render_template('predict.html')

if __name__ == '__main__':
    app.run(debug=True)

