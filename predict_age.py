import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import argparse
import os

# Load the model (ensure 'Age_detection.h5' is in the same directory or provide full path)
MODEL_PATH = 'Age_detection.h5'

def prediction(image_path, model):
    """
    Predicts the age category from an image.
    Args:
        image_path (str): The path to the image file.
        model (keras.Model): The loaded Keras model.
    Returns:
        str: The predicted age category ('Middle', 'Old', 'Young') or an error message.
    """
    try:
        image = load_img(image_path, target_size=(100, 100))
        image = img_to_array(image)
        image = image.reshape(1, 100, 100, 3) # Reshape for the model
        image = image / 255.0 # Rescale pixel values if model was trained with rescaled data

        result = model.predict(image)
        result_class_index = np.argmax(result)

        if result_class_index == 0:
            return 'Middle'
        elif result_class_index == 1:
            return 'Old'
        else: # Assuming class index 2
            return 'Young'
    except FileNotFoundError:
        return f"Error: Image file not found at {image_path}"
    except Exception as e:
        return f"An error occurred during prediction: {str(e)}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Predict age from an image.")
    parser.add_argument("image_path", type=str, help="Path to the image file for prediction.")

    args = parser.parse_args()

    if not os.path.exists(MODEL_PATH):
        print(f"Error: Model file '{MODEL_PATH}' not found. Please ensure the model is trained and saved.")
    else:
        try:
            model = load_model(MODEL_PATH)
            predicted_age = prediction(args.image_path, model)
            print(f"The predicted age category is: {predicted_age}")
        except Exception as e:
            print(f"An error occurred loading the model: {str(e)}")
