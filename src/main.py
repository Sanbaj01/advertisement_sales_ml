import pickle

model = pickle.load("models\linear_regression_model.pkl")

def predict_discounted_price(rating:float, rating_count:int, actual_price:float)->float:
    """predicts discounted price based on rating ...
    Args:

    Returns:

    Raise:
    """
    try:
        input = None # (rating, rating_count, actual_price)
        predictions = model.predict(input)
        return predictions
    except:
        raise ValueError("")
    

if __name__ == "__main__":
    rating = input("rating: ")
    rating_count = input("rating count: ")
    actual_price = input("actual price: ")

    predicted_discount = predict_discounted_price(rating, rating_count, actual_price)

    print(predicted_discount)