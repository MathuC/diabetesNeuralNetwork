# Diabetes Neural Network
 Simple neural network that predicts the onset of diabetes in 5 years using patient medical record data. Trained on the Pima Indians Diabetes Database.

 ## Built With
Keras, the high-level API of the TensorFlow platform.

 ## Input data format
 * Number of times pregnant
 * Plasma glucose concentration at 2 hours in an oral glucose tolerance test
 * Diastolic blood pressure (mm Hg)
 * Triceps skin fold thickness (mm)
 * 2-hour serum insulin (mu U/ml)
 * Body mass index (weight in kg/(height in m)^2)
 * Diabetes pedigree function
 * Age (years)

 ## Usage
 * Download the **Model** directory into your current directory.
 * Launch python
 * Then:
 ```
import keras from tensorflow
model=keras.models.load_model("Model")
 ```

 * Example where the input is [5.0, 187, 82, 60, 207, 40, 1, 100]
 ```
model.predict([[5.0, 187, 82, 60, 207, 40, 1, 100]])[0][0]
 ```

 * Output of the previous example
 ```
 1/1 [==============================] - 0s 57ms/step
 0.98982555
 ```

