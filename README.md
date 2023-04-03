# Diabetes Neural Network
 Simple neural network that predicts the onset of diabetes in 5 years using patient medical record data. Trained on the Pima Indians Diabetes Database.

 ## Built With
Keras, the high-level API of the TensorFlow platform.

 ## Usage
 Download the **Model** directory into your current directory
 Launch python
 Then (example where the input is *5.0, 187, 82, 60, 207, 40, 1, 100*):
 ```
import keras from tensorflow
model=keras.models.load_model("Model")
model.predict([[5.0, 187, 82, 60, 207, 40, 1, 100]])[0][0]
 ```
