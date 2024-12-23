import numpy as np
import pickle
import tensorflow as tf

from tensorflow.keras.utils import get_custom_objects
from django.shortcuts import render
from .custom_layers import CustomLSTM
from .models import WaterLevelPrediction
from datetime import datetime

def render_form(request):
   return render(request, 'forecast/predict.html')



# Register CustomLSTM globally
get_custom_objects()["CustomLSTM"] = CustomLSTM

# Function to load the model and scalers
def load_model_and_scalers():
    # Load the model
    model = tf.keras.models.load_model("C:/Users/Milan Tamang/Desktop/final_One/forecast_project_copy_final/forecast/my_custom_lstm_model.keras")
    
    # Load the scalers
    with open('C:/Users/Milan Tamang/Desktop/final_One/forecast_project_copy_final/forecast/scaler.pkl', 'rb') as f:
        scalers = pickle.load(f)
    
    return model, scalers


# Function to make predictions
def predict_water_level(input_features):
    """
    Predict water level based on input features.
    :param input_features: List of input features [Rainfall, Temperature, Humidity, etc.]
    :return: Predicted water level
    """
    # Load model and scalers
    model, scalers = load_model_and_scalers()
    scaler_X = scalers['scaler_X']
    scaler_y = scalers['scaler_y']

    # Reshape input features
    n_steps = 20  # The same value used during training
    input_data = np.array(input_features).reshape(1, -1)  # 2D array
    input_data_reshaped = np.repeat(input_data, n_steps, axis=0)  # Repeat data for n_steps
    input_data_reshaped = input_data_reshaped.reshape(1, n_steps, input_data.shape[1])  

    # Scale input features
    input_data_scaled = scaler_X.transform(input_data_reshaped.reshape(-1, input_data_reshaped.shape[2]))
    input_data_scaled = input_data_scaled.reshape(1, n_steps, input_data.shape[1])  # Back to 3D

    # Predict water level
    predicted_scaled = model.predict(input_data_scaled)
    predicted_water_level = scaler_y.inverse_transform(predicted_scaled)  # Rescale to original scale

    return predicted_water_level[0][0]


# Django view to handle predictions
from django.db.models import Max
def water_level_prediction_view(request):
    """
    Django view to predict water levels based on user input.
    :param request: HTTP GET or POST request with input features.
    :return: JSON response with predicted water level.
    """
    if request.method == 'POST':
        try:
            # Get input features from the request
            rainfall = request.POST.get('rainfall')
            temperature = request.POST.get('temperature')
            humidity = request.POST.get('humidity')
            specific_humidity = request.POST.get('specific_humidity')
            water_level = request.POST.get('water_level')  # Optional field

            # Check if the primary input fields are valid
            if None in [rainfall, temperature, humidity, specific_humidity] or \
               "" in [rainfall, temperature, humidity, specific_humidity]:
                raise ValueError("Rainfall, Temperature, Humidity, and Specific Humidity fields are required.")
            
            # Convert inputs to float and validate they are non-negative
            rainfall = float(rainfall)
            temperature = float(temperature)
            humidity = float(humidity)
            specific_humidity = float(specific_humidity)

            # Validate that input values are non-negative
            if any(val < 0 for val in [rainfall, temperature, humidity, specific_humidity]):
                raise ValueError("Input values cannot be negative.")

            # Check and handle the water level value
            if not water_level or water_level == "":
                # Retrieve the most recent water level from the database
                recent_prediction = WaterLevelPrediction.objects.aggregate(Max('predicted_level'))
                water_level = recent_prediction['predicted_level__max']  # Use the most recent water level
                if water_level is None:
                    raise ValueError("No previous water level data available in the database. Provide the water level value manually.")
            else:
                water_level = float(water_level)

            # Validate that water level is non-negative
            if water_level < 0:
                raise ValueError("Water level cannot be negative.")

            # Prepare input features
            input_features = [rainfall, temperature, humidity, specific_humidity, water_level]

            # Predict water level
            predicted_level = predict_water_level(input_features)

            # Save prediction to the database
            WaterLevelPrediction.objects.create(predicted_level=predicted_level)

            # Return predicted water level to the template
            return render(request, 'forecast/predict.html', {'predicted_water_level': predicted_level})

        except ValueError as e:
            # Handle errors such as invalid float conversion, missing inputs, or negative values
            return render(request, 'forecast/predict.html', {'error': str(e)})

        except Exception as e:
            # Handle any other unexpected errors
            return render(request, 'forecast/predict.html', {'error': f"An error occurred: {str(e)}"})

    else:
        return render(request, 'forecast/predict.html', {'error': 'Invalid request method. Use POST.'})