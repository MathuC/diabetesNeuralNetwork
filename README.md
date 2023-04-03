# Diabetes Neural Network
 Simple neural network that predicts the onset of diabetes in 5 years using patient medical record data. Trained on the Pima Indians Diabetes Database.

 ## Built With
Keras, the high-level API of the TensorFlow platform.

 ## Input data format
 [[x0,x1,x2,x3,x4,x5,x6,x7]]
 * x0: Number of times pregnant
 * x1: Plasma glucose concentration at 2 hours in an oral glucose tolerance test
 * x2: Diastolic blood pressure (mm Hg)
 * x3: Triceps skin fold thickness (mm)
 * x4: 2-hour serum insulin (mu U/ml)
 * x5: Body mass index (weight in kg/(height in m)^2)
 * x6: Diabetes pedigree function
 * x7: Age (years)

 ## Usage
 * Download the **Model** directory into your current directory.
 * Launch python
 * Import keras and load the model
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
This imaginary patient has a 98.98% chance of getting diabetes in the next 5 years.

