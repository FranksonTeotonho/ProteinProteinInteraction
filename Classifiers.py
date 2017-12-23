from sklearn import metrics
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import VotingClassifier

#Melhores resultados

def DataKNN(X,Y):
    
    metrics = {}
    knn = KNeighborsClassifier(n_neighbors = 3)
    accuracy = cross_val_score(knn, X, Y, cv = 10, scoring = 'accuracy')
    metrics['accuracy'] = accuracy.mean()
    precision = cross_val_score(knn, X, Y, cv = 10, scoring = 'precision')
    metrics['precision'] = precision.mean()
    recall = cross_val_score(knn, X, Y, cv = 10, scoring = 'recall')
    metrics['recall'] = recall.mean()
    Fmeasure = cross_val_score(knn, X, Y, cv = 10, scoring = 'f1')
    metrics['Fmeasure'] = Fmeasure.mean()
    return metrics


def DataArvoreDecisao(X, Y):
    metrics = {}
    clf = tree.DecisionTreeClassifier()
    accuracy = cross_val_score(clf, X, Y, cv=10, scoring='accuracy')
    metrics['accuracy'] = accuracy.mean()
    precision = cross_val_score(clf, X, Y, cv=10, scoring='precision')
    metrics['precision'] = precision.mean()
    recall = cross_val_score(clf, X, Y, cv=10, scoring='recall')
    metrics['recall'] = recall.mean()
    Fmeasure = cross_val_score(clf, X, Y, cv=10, scoring='f1')
    metrics['Fmeasure'] = Fmeasure.mean()
    return metrics


def DataRandomForest(X, Y):
    metrics = {}
    clf = RandomForestClassifier(n_estimators=13)
    accuracy = cross_val_score(clf, X, Y, cv=10, scoring='accuracy')
    metrics['accuracy'] = accuracy.mean()
    precision = cross_val_score(clf, X, Y, cv=10, scoring='precision')
    metrics['precision'] = precision.mean()
    recall = cross_val_score(clf, X, Y, cv=10, scoring='recall')
    metrics['recall'] = recall.mean()
    Fmeasure = cross_val_score(clf, X, Y, cv=10, scoring='f1')
    metrics['Fmeasure'] = Fmeasure.mean()
    return metrics


def DataAdaBoost(X, Y):
    metrics = {}
    clf = AdaBoostClassifier(n_estimators=100)
    accuracy = cross_val_score(clf, X, Y, cv=10, scoring='accuracy')
    metrics['accuracy'] = accuracy.mean()
    precision = cross_val_score(clf, X, Y, cv=10, scoring='precision')
    metrics['precision'] = precision.mean()
    recall = cross_val_score(clf, X, Y, cv=10, scoring='recall')
    metrics['recall'] = recall.mean()
    Fmeasure = cross_val_score(clf, X, Y, cv=10, scoring='f1')
    metrics['Fmeasure'] = Fmeasure.mean()
    return metrics


def DataExtraTree(X, Y):
    metrics = {}
    clf = ExtraTreesClassifier(n_estimators=10, max_depth=None, min_samples_split=2, random_state=0)
    accuracy = cross_val_score(clf, X, Y, cv=10, scoring='accuracy')
    metrics['accuracy'] = accuracy.mean()
    precision = cross_val_score(clf, X, Y, cv=10, scoring='precision')
    metrics['precision'] = precision.mean()
    recall = cross_val_score(clf, X, Y, cv=10, scoring='recall')
    metrics['recall'] = recall.mean()
    Fmeasure = cross_val_score(clf, X, Y, cv=10, scoring='f1')
    metrics['Fmeasure'] = Fmeasure.mean()
    return metrics


def DataEnsemble(X, Y):
    metrics = {}

    clf1 = AdaBoostClassifier(n_estimators=101)
    clf2 = KNeighborsClassifier(n_neighbors=3)
    clf3 = RandomForestClassifier(n_estimators=13)
    eclf = VotingClassifier(estimators=[('AdaBoost', clf1), ('KNN5', clf2),
                                        ('RandomForest', clf3)], voting='hard', weights=[2, 1, 2])
    accuracy = cross_val_score(eclf, X, Y, cv=10, scoring='accuracy')
    metrics['accuracy'] = accuracy.mean()
    precision = cross_val_score(eclf, X, Y, cv=10, scoring='precision')
    metrics['precision'] = precision.mean()
    recall = cross_val_score(eclf, X, Y, cv=10, scoring='recall')
    metrics['recall'] = recall.mean()
    Fmeasure = cross_val_score(eclf, X, Y, cv=10, scoring='f1')
    metrics['Fmeasure'] = Fmeasure.mean()
    return metrics

#Resultados não tão bons
def DataSVM(X,Y):
    
    metrics = {}
    clf = SVC(kernel= 'rbf')
    accuracy = cross_val_score(clf, X, Y, cv = 10, scoring = 'accuracy')
    metrics['accuracy'] = accuracy.mean()
    precision = cross_val_score(clf, X, Y, cv = 10, scoring = 'precision')
    metrics['precision'] = precision.mean()
    recall = cross_val_score(clf, X, Y, cv = 10, scoring = 'recall')
    metrics['recall'] = recall.mean()
    Fmeasure = cross_val_score(clf, X, Y, cv = 10, scoring = 'f1')
    metrics['Fmeasure'] = Fmeasure.mean()
    return metrics
    
def DataNaiveBayers(X,Y):
    
    metrics = {}
    gnb = GaussianNB()
    accuracy = cross_val_score(gnb, X, Y, cv = 10, scoring = 'accuracy')
    metrics['accuracy'] = accuracy.mean()
    precision = cross_val_score(gnb, X, Y, cv = 10, scoring = 'precision')
    metrics['precision'] = precision.mean()
    recall = cross_val_score(gnb, X, Y, cv = 10, scoring = 'recall')
    metrics['recall'] = recall.mean()
    Fmeasure = cross_val_score(gnb, X, Y, cv = 10, scoring = 'f1')
    metrics['Fmeasure'] = Fmeasure.mean()
    return metrics
    
#Analisar mais
def DataMLP(X,Y):
    
    metrics = {}
    clf = MLPClassifier(solver='sgd', alpha=1e-5,
                    hidden_layer_sizes=(5, 2), random_state=1)
    accuracy = cross_val_score(clf, X, Y, cv = 10, scoring = 'accuracy')
    metrics['accuracy'] = accuracy.mean()
    precision = cross_val_score(clf, X, Y, cv = 10, scoring = 'precision')
    metrics['precision'] = precision.mean()
    recall = cross_val_score(clf, X, Y, cv = 10, scoring = 'recall')
    metrics['recall'] = recall.mean()
    Fmeasure = cross_val_score(clf, X, Y, cv = 10, scoring = 'f1')
    metrics['Fmeasure'] = Fmeasure.mean()
    return metrics
