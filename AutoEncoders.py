import numpy as np
import pandas as pd
from keras.models import Model
from keras.layers import Dense,Input
from sklearn.model_selection import train_test_split
#DropOut
def AutoEnconde(X,dim,ndim):
    X_train, X_test = train_test_split(X, test_size = 0.2)
    #Placeholder com as dimensões padrões
    input_feature = Input(shape=(dim,))

    # Camadas
    # dim-> ndim -> dim
    encoded = Dense(ndim,activation='relu')(input_feature)
    decoded = Dense(dim, activation='sigmoid')(encoded)

    #Modelos
    #AutoEncoder completo
    autoEncoder = Model(input_feature,decoded)
    #Encoder
    encoder = Model(input_feature, encoded)

    autoEncoder.compile(optimizer='adadelta', loss='binary_crossentropy',metrics=['accuracy'])
    autoEncoder.fit(X_train, X_train,
                    epochs=200,
                    batch_size=100,
                    shuffle=True,
                    validation_data=(X_test, X_test))

    encoded_feature = encoder.predict(X)
    return encoded_feature

