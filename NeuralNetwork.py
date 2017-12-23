from keras.models import  Sequential
from keras.layers import Dense
from sklearn.model_selection import cross_val_score
from keras.wrappers.scikit_learn import KerasClassifier

def NeuralNetworkModel():

    model = Sequential()
    model.add(Dense(200, input_dim = 400, activation= 'relu'))
    model.add(Dense(100, activation= 'relu'))
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
