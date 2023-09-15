import pickle
import numpy as np

with open(r'C:\Users\vs\Desktop\sales_ml_project\model\linear_regression_model.pkl', 'rb') as file:
    model = pickle.load(file)

def predict_discounted_price(tv:float, radio:float, newspaper:float)->float:
    """predicts discounted price based on rating ...
    Args:

    Returns:

    Raise:
    """
    try:
        #input = None # (rating, rating_count, actual_price)
        input = np.array([tv, radio, newspaper]).reshape(1,-1)
        predictions = model.predict(input)
        return predictions
    except Exception as e:
        raise ValueError(str(e))
    

if __name__ == "__main__":
    tv = float(input("TV : "))
    radio = float(input("Radio: "))
    newspaper = float(input("Newspaper: "))

    predicted_discount = predict_discounted_price(tv, radio, newspaper)

    print(predicted_discount)