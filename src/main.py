import pickle
import numpy as np

with open(r'C:\Users\vs\Desktop\sales_ml_project\models\linear_regression_model.pkl', 'rb') as file:
    model = pickle.load(file)

def predict_sales(tv:float, radio:float, newspaper:float)->float:
    """predicts discounted price based on rating ...
    Args:

    Returns:

    Raise:
    """
    try:
        #input = None # (rating, rating_count, actual_price)
        input = np.array([tv, radio, newspaper]).reshape(1,-1)
        prediction = model.predict(input)
        return prediction
    except Exception as e:
        raise ValueError(str(e))
    

if __name__ == "__main__":
    tv = float(input("TV : "))
    radio = float(input("Radio: "))
    newspaper = float(input("Newspaper: "))

    predicted_sales = predict_sales(tv, radio, newspaper)

    print(predicted_sales)