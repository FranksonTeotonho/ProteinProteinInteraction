 #Lendo o arquivo
    arquivo = open("teste.luiz.csv", "r")
    lines = []
    features = []

    #percorrendo cada linha
    for i in arquivo.readlines():
        lines.append(i)

    for j in lines:
        #Recebendo cada linha
        str = j
        #Fazendo o corte com , como delimitador de cada coluna na linha
        aux = str.split(",")
        #Realizando a conversão para float de cada coluna na linha
        #Importante que sua string seja numeros separados com .
        aux_features = np.asarray([float (elemento) for elemento in aux])
        #Adicionando o vetor convertido no vetor features (resultando em uma matriz)
        features.append(aux_features)