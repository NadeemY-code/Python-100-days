# Import necessary libraries
import tensorflow as tf
import numpy as np
from PIL import Image

# Load the pre-trained model
model = tf.keras.applications.ResNet50(weights='imagenet')

# Load and preprocess the image
image_path = 'D:\saffron images'
image = Image.open(image_path)
image = image.resize((224, 224))  # Resize the image to match the input size of the model
image_array = np.array(image)
image_array = np.expand_dims(image_array, axis=0)
preprocessed_image = tf.keras.applications.resnet50.preprocess_input(image_array)

# Perform image classification
predictions = model.predict(preprocessed_image)
decoded_predictions = tf.keras.applications.resnet50.decode_predictions(predictions, top=3)[0]

# Display the results
for _, label, probability in decoded_predictions:
    print(f"{label}: {probability * 100}%")
