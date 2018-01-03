from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from sklearn.model_selection import cross_val_score
from keras.wrappers.scikit_learn import KerasClassifier

def NeuralNetworkModel():

    model = Sequential()
    model.add(Dense(50, input_dim = 96, activation= 'relu'))
    model.add(Dropout(0.2))
    model.add(Dense(25, activation= 'relu'))
    model.add(Dense(1, activation = 'sigmoid'))

    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    return model

def NeuralNetworkClassifier(X,Y):

    neural_network = KerasClassifier(build_fn=NeuralNetworkModel,
                                 epochs=40,
                                 batch_size=10)

    accuracy = cross_val_score(neural_network, X, Y, cv=10, scoring='accuracy')
    x = accuracy.mean()

    return x
