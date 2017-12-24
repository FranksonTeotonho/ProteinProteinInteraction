#import numpy as np
import pandas as pd
#import Classifiers
import Preprocessing
#import AutoEncoders
import NeuralNetwork
#from sklearn.decomposition import KernelPCA
#from sklearn.decomposition import PCA

def main():

    """"
    # BioPython - Yeast
    dataset_BioPython = pd.read_csv('DatabasesCSV/Yeast/DatabaseBioPython.csv')
    X1 = dataset_BioPython.iloc[:, :-1].values
    Y1 = dataset_BioPython.iloc[:, 96].values  # BioPython 94, MMI 238

    # MMI - Yeast
    dataset_MMI = pd.read_csv('DatabasesCSV/Yeast/DataBaseMMI.csv')
    X2 = dataset_MMI.iloc[:, :-1].values
    Y2 = dataset_MMI.iloc[:, 238].values  # BioPython 94, MMI 238

    # NMBAC - Yeast
    dataset_NMBAC = pd.read_csv('DatabasesCSV/Yeast/DataBaseBAC.csv')
    X3 = dataset_NMBAC.iloc[:, :-1].values
    Y3 = dataset_NMBAC.iloc[:, 400].values  # BioPython 94, MMI 238

    # BioPython - Matine
    dataset_BioPython = pd.read_csv('DatabasesCSV/Matine/Matine_Database_BioPython.csv')
    X1 = dataset_BioPython.iloc[:, :-1].values
    Y1 = dataset_BioPython.iloc[:, 94].values  # BioPython 94, MMI 238

    # MMI - Matine
    dataset_MMI = pd.read_csv('DatabasesCSV/Matine/Matine_DataBase_MMI.csv')
    X2 = dataset_MMI.iloc[:, :-1].values
    Y2 = dataset_MMI.iloc[:, 238].values  # BioPython 94, MMI 238

    # NMBAC - Matine
    dataset_NMBAC = pd.read_csv('DatabasesCSV/Matine/Matine_database_NMBAC.csv')
    X3 = dataset_NMBAC.iloc[:, :-1].values
    Y3 = dataset_NMBAC.iloc[:, 400].values  # BioPython 94, MMI 238

    #BioPython - Human
    dataset_BioPython = pd.read_csv('DatabasesCSV/Human/Human_Database_BioPython.csv')
    X1 = dataset_BioPython.iloc[:, :-1].values
    Y1 = dataset_BioPython.iloc[:, 94].values  # BioPython 94, MMI 238
    X1 = Preprocessing.FeatureScaling(X1)

    #MMI - Human
    dataset_MMI = pd.read_csv('DatabasesCSV/Human/Human_Database_MMI.csv')
    X2 = dataset_MMI.iloc[:, :-1].values
    Y2 = dataset_MMI.iloc[:, 238].values  # BioPython 94, MMI 238

    #NMBAC - Human
    dataset_NMBAC = pd.read_csv('DatabasesCSV/Human/Human_Database_NMBAC.csv')
    X3 = dataset_NMBAC.iloc[:, :-1].values
    Y3 = dataset_NMBAC.iloc[:, 400].values #BioPython 94, MMI 238


    """

    #X3 = AutoEncoders.AutoEnconde(X3,400,200)
    #print(X1)


    # BioPython - Yeast
    dataset_BioPython = pd.read_csv('DatabasesCSV/Yeast/DatabaseBioPython.csv')
    X1 = dataset_BioPython.iloc[:, :-1].values
    Y1 = dataset_BioPython.iloc[:, 96].values  # BioPython 94, MMI 238
    X1 = Preprocessing.FeatureScaling(X1)

    Accuracy = NeuralNetwork.NeuralNetworkClassifier(X1,Y1)

    print("\n Accuracy: ", Accuracy)
   # print("===================NMBAC 3===============")
   # print("Accuracy:", metrics3['accuracy'])
   # print("Precision:", metrics3['precision'])
   # print("Recall:", metrics3['recall'])
   # print("Fmeasure:", metrics3['Fmeasure'])



if __name__ == '__main__':
    main()
