from flask import Flask, render_template,  request
import os
import numpy as np
import pandas as pd
from mlopsCreditRisk.pipeline.stage_06_prediction import PredictionPipeline


app = Flask(__name__) # initialize a flask app

@app.route('/', methods=['GET']) # route to display the home page
def homePage():
    return render_template("index.html")

@app.route('/train', methods=['GET']) # route to train the pipeline
def training():
    os.system("python main.py")
    return "Training completed!"

@app.route('/predict', methods=['GET','POST']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            credit_lines_outstanding = request.form.get('credit_lines_outstanding', type=int)
            loan_amt_outstanding = request.form.get('loan_amt_outstanding', type=float)
            total_debt_outstanding = request.form.get('total_debt_outstanding', type=float)
            income = request.form.get('income', type=float)
            years_employed = request.form.get('years_employed', type=int)
            fico_score = request.form.get('fico_score', type=int)

            data = np.array([credit_lines_outstanding, loan_amt_outstanding, total_debt_outstanding, income, years_employed, fico_score])

            pred_obj = PredictionPipeline()
            predict = pred_obj.predict(data.reshape(1, -1)) # scikit learn expects 2D array for prediction

            if predict==1:
                return render_template("results.html", prediction = str('Default'))
            elif predict==0:
                return render_template("results.html", prediction = str('No default'))
    
        except Exception as e:
            print("The exception message is: ", e)
            return "Something went wrong."
        
    else:
        return render_template("index.html")

if __name__ == '__main__':
    #app.run(host="0.0.0.0", port=8080, debug=True)
    app.run(host="0.0.0.0", port=8080)