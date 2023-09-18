import pickle
import sys
import numpy as np
from flask import Flask, render_template, request, jsonify
            
sys.path.append("C:/Users/vs/Desktop/sales_ml_project/")
from src.main import predict_sales

model = pickle.load(open(r'C:\Users\vs\Desktop\sales_ml_project\models\linear_regression_model.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        tv = float(request.form['tv'])
        radio = float(request.form['radio'])
        newspaper = float(request.form['newspaper'])
        predicted_sales = predict_sales(tv, radio, newspaper)
        print(predicted_sales)
        return render_template('result.html', predicted_sales= round(predicted_sales[0], 4))
    except Exception as e:
        return str(e)

@app.route('/results', methods=['POST'])
def results():
    data = request.get_json(force=True)
    print(data)
    
    prediction = model.predict([np.array(list(data.value()))])
    return jsonify(prediction)

if __name__ == "__main__":
    app.run(debug=True)
