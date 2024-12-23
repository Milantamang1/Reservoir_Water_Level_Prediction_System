from tensorflow.keras.models import load_model
import numpy as np

# Load the model
model_path = "/Users/nashipacharya/Home/Django/forecast_project/forecast/my_custom_lstm_model.h5"  # Adjust if using SavedModel format
model = load_model(model_path)

def predict_water_level(input_data):
    """
    Function to make predictions using the LSTM model.
    :param input_data: Preprocessed NumPy array (e.g., scaled features).
    :return: Predicted value (scaled back).
    """
    # Ensure input_data has the correct shape for LSTM
    input_data = np.expand_dims(input_data, axis=0)  # Add batch dimension
    prediction = model.predict(input_data)
    return prediction[0][0]
