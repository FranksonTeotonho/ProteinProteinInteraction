from sklearn.preprocessing import StandardScaler


def FeatureScaling(X):
    sc_X = StandardScaler()
    X = sc_X.fit_transform(X)
    return X