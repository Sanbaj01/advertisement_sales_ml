import pickle
import sys
import numpy as np
from flask import Flask, request, jsonify
            
sys.path.append("C:/Users/vs/Desktop/sales_ml_project/")
from src.main import predict_sales

model = pickle.load(open(r'../models/linear_regression_model.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    response = "sales predictions..."
    return jsonify({"res": response})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        tv = float(data.get("tv"))
        radio = float(data.get("radio"))
        newspaper = float(data.get("newspaper"))
        
        input = np.array([tv, radio, newspaper]).reshape(1,-1)
        predicted_sales = model.predict(input)
        
        response = round(predicted_sales[0], 4)
        
        return jsonify({"response": response})
    
    except Exception as e:
        response = str(e)
        
        return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)



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
