import numpy
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import random

#load the dataset
'''
It describes patient medical record data for Pima Indians and whether they had an onset of diabetes within five years.
Data (ordered):
Number of times pregnant
Plasma glucose concentration at 2 hours in an oral glucose tolerance test
Diastolic blood pressure (mm Hg)
Triceps skin fold thickness (mm)
2-hour serum insulin (mu U/ml)
Body mass index (weight in kg/(height in m)^2)
Diabetes pedigree function
Age (years)
'''
dataset = numpy.loadtxt("pima-indians-diabetes.csv", delimiter=",")

#split into input (x) and output (y) variables
x=dataset[:,0:8] #this doesn't work on python arrays, only on numpy arrays. For python arrays, you need to do x=dataset[:][0:8]
y=dataset[:,8]

#define the keras model
#sequential model: plain stack of layers where each layer has exactly one input tensor and one output tensor.
model=Sequential()
model.add(Dense(12, input_shape=(8,), activation='relu')) #relu(x)=max(x,0), so it is 0 when x is negative or itself when x is 0 or positive
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid')) #returns between 0 and 1, 1/(1+e^-x)

#compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
#adam is an optimization algorithm that can be used instead of the classical stochastic gradient descent procedure to update network weights
# iterative based in training data.
#cross entropy loss is a metric used to measure how well a classification model in machine learning performs.

#fit the keras model on the dataset
model.fit(x, y, epochs=150, batch_size=10)

#evaluate the keras model
_, accuracy=model.evaluate(x, y)
print('Accuracy: %.2f' % (accuracy*100))

#make predictions with the model
predictions=(model.predict(x)>0.5).astype(int)

#choose 10 random inputs to check if model's outputs is correct
for i in range(10):
    j=random.randint(0,x.shape[0]-1)
    if (predictions[j]==y[j]):
        message="Success!"
    else:
        message="Failure."
    print('%s => %d Expected:%d %s' % (x[j].tolist(), predictions[j], y[j], message))
