import pandas as pd
from keras.models import Sequential
from keras.layers import *
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.externals import joblib
from sklearn.metrics import mean_absolute_error

# Disable some useless pandas warnings to prevent some junk from showing up in the output window
pd.options.mode.chained_assignment = None

# Load our data set
df = pd.read_csv("house_data.csv")

# Create the X and y arrays
X = df[["sq_feet", "num_bedrooms", "num_bathrooms"]]
y = df[["sale_price"]]

# Data needs to be scaled to  0 to 1 for the neural network to train correctly.
X_scaler = MinMaxScaler(feature_range=(0, 1))
y_scaler = MinMaxScaler(feature_range=(0, 1))

print("X_scaler:", X_scaler)
print("y_scaler:", y_scaler)

# Scale both the training inputs and outputs
X[X.columns] = X_scaler.fit_transform(X[X.columns])
y[y.columns] = y_scaler.fit_transform(y[y.columns])

# Split the data set in a training set (75%) and a test set (25%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

# Create a Neural Network model
model = Sequential()

# This single line actually will create two layers—a three-node input layer and a 50-node hidden layer.
model.add(Dense(200, input_dim=3, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(50, activation='relu'))

# Since we are only predicting one final value (the value of a house), we only need one output node.
# And since we are predicting a real-world value, we’ll ask it to use a linear activation function,
# which is the same thing as doing nothing. This is because we want the final prediction to be a linear
# number so we don’t need to do anything special to it.
model.add(Dense(1, activation='linear'))


# We are using the Keras API to define our neural network, but it uses Ten- sorFlow behind the scenes to
# do all the math. Now that we’ve declared all the layers, we need to tell Keras to construct the neural
# network inside of TensorFlow for us. To do that, we’ll call the compile() function:
# Page 72.
model.compile(
    loss='mean_squared_error',
    optimizer='SGD'
)

# Train the model
model.fit(
    X_train,
    y_train,
    epochs=200,
    batch_size=8,
    shuffle=True,
    verbose=2
)

# Save the scalers to files so we can use it to pre-process new data later
joblib.dump(X_scaler, "X_scaler.pkl")
joblib.dump(y_scaler, "y_scaler.pkl")

# Save the trained model to a file so we can use it to make predictions later
model.save("house_value_model.h5")

# Report how well the model is performing
print("Model training results:")

# Report mean absolute error on the training set in a value scaled back to dollars so it's easier to understand.
predictions_train = model.predict(X_train, verbose=0)

mse_train = mean_absolute_error(
    y_scaler.inverse_transform(predictions_train),
    y_scaler.inverse_transform(y_train)
)
print(f" - Training Set Error: {mse_train}")

# Report mean absolute error on the test set in a value scaled back to dollars so it's easier to understand.
predictions_test = model.predict(X_test, verbose=0)

mse_test = mean_absolute_error(
    y_scaler.inverse_transform(predictions_test),
    y_scaler.inverse_transform(y_test)
)
print(f" - Test Set Error: {mse_test}")
