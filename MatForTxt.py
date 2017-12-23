import scipy.io as sc
import numpy as np
from Bio.SeqUtils.ProtParam import ProteinAnalysis

def GetFeatures (My_seq):

    Features = {}

    ProteinAnalysis(My_seq)
    analysed_seq = ProteinAnalysis(My_seq)
    #Caracteristicas monovaloradas

    Features["Molecular_weight"] = analysed_seq.molecular_weight()
    Features["Aromaticity"] = analysed_seq.aromaticity()
    Features["Instability_index"] = analysed_seq.instability_index()
    Features["Isoelectric_point"] = analysed_seq.isoelectric_point()


    #Caracteristicas multivaloradas

    Features["Flexibility"] = analysed_seq.flexibility() # List 580
    Features["Second_structure_fraction"] = analysed_seq.secondary_structure_fraction() #3 Tupla
    Features["Count_amino_acids"] = analysed_seq.count_amino_acids() #20 Dict
    Features["Amino_acids_percent"] = analysed_seq.get_amino_acids_percent() #20 Dict


    return Features


def MatForTxt(FileMat, NameTxt, key):

    N_protein = sc.loadmat(FileMat+'.mat')

    arquivo = open(NameTxt+".txt",'w')

    for p in N_protein.get(key):
        s1 = str(p).replace("[ array([ '", "")
        s2 = s1.replace("'], \n      dtype='<U", " ")
        s3 = s2.replace("')]", "")
        arquivo.write(s3+"\n")


    arquivo.close()

def MakeSCV(arquivo_c, X_protein_a,X_Protein_b,PPI):
    arquivo_a = open(X_protein_a + ".txt",'r')
    arquivo_b = open(X_Protein_b + ".txt",'r')

    for i,j in zip(arquivo_a.readlines(),arquivo_b.readlines()):

        # Obtendo caracteristicas de a
        lista_aux = i.split()
        Features = GetFeatures(lista_aux[0])
        #Elementos monovalorados
        #arquivo_c.write(str(lista_aux[1])+',')
        arquivo_c.write(str(Features.get("Molecular_weight"))+',')
        arquivo_c.write(str(Features.get("Aromaticity"))+',')
        arquivo_c.write(str(Features.get("Instability_index"))+',')
        arquivo_c.write(str(Features.get("Isoelectric_point"))+',')
        #Elementos multivalorados
        for a in Features.get("Second_structure_fraction"):
            arquivo_c.write(str(a)+',')

        #Elementos de Count_amino_acids

        arquivo_c.write(str(Features["Count_amino_acids"]["A"]) + ',')
        arquivo_c.write(str(Features["Count_amino_acids"]["R"]) + ',')
        arquivo_c.write(str(Features["Count_amino_acids"]["N"]) + ',')
        arquivo_c.write(str(Features["Count_amino_acids"]["D"]) + ',')
        arquivo_c.write(str(Features["Count_amino_acids"]["C"]) + ',')
        arquivo_c.write(str(Features["Count_amino_acids"]["E"]) + ',')
        arquivo_c.write(str(Features["Count_amino_acids"]["Q"]) + ',')
        arquivo_c.write(str(Features["Count_amino_acids"]["G"]) + ',')
        arquivo_c.write(str(Features["Count_amino_acids"]["H"]) + ',')
        arquivo_c.write(str(Features["Count_amino_acids"]["I"]) + ',')
        arquivo_c.write(str(Features["Count_amino_acids"]["L"]) + ',')
        arquivo_c.write(str(Features["Count_amino_acids"]["K"]) + ',')
        arquivo_c.write(str(Features["Count_amino_acids"]["M"]) + ',')
        arquivo_c.write(str(Features["Count_amino_acids"]["F"]) + ',')
        arquivo_c.write(str(Features["Count_amino_acids"]["P"]) + ',')
        arquivo_c.write(str(Features["Count_amino_acids"]["S"]) + ',')
        arquivo_c.write(str(Features["Count_amino_acids"]["T"]) + ',')
        arquivo_c.write(str(Features["Count_amino_acids"]["W"]) + ',')
        arquivo_c.write(str(Features["Count_amino_acids"]["Y"]) + ',')
        arquivo_c.write(str(Features["Count_amino_acids"]["V"]) + ',')

        #Elementos de Amino_acids_percent

        arquivo_c.write(str(Features["Amino_acids_percent"]["A"]) + ',')
        arquivo_c.write(str(Features["Amino_acids_percent"]["R"]) + ',')
        arquivo_c.write(str(Features["Amino_acids_percent"]["N"]) + ',')
        arquivo_c.write(str(Features["Amino_acids_percent"]["D"]) + ',')
        arquivo_c.write(str(Features["Amino_acids_percent"]["C"]) + ',')
        arquivo_c.write(str(Features["Amino_acids_percent"]["E"]) + ',')
        arquivo_c.write(str(Features["Amino_acids_percent"]["Q"]) + ',')
        arquivo_c.write(str(Features["Amino_acids_percent"]["G"]) + ',')
        arquivo_c.write(str(Features["Amino_acids_percent"]["H"]) + ',')
        arquivo_c.write(str(Features["Amino_acids_percent"]["I"]) + ',')
        arquivo_c.write(str(Features["Amino_acids_percent"]["L"]) + ',')
        arquivo_c.write(str(Features["Amino_acids_percent"]["K"]) + ',')
        arquivo_c.write(str(Features["Amino_acids_percent"]["M"]) + ',')
        arquivo_c.write(str(Features["Amino_acids_percent"]["F"]) + ',')
        arquivo_c.write(str(Features["Amino_acids_percent"]["P"]) + ',')
        arquivo_c.write(str(Features["Amino_acids_percent"]["S"]) + ',')
        arquivo_c.write(str(Features["Amino_acids_percent"]["T"]) + ',')
        arquivo_c.write(str(Features["Amino_acids_percent"]["W"]) + ',')
        arquivo_c.write(str(Features["Amino_acids_percent"]["Y"]) + ',')
        arquivo_c.write(str(Features["Amino_acids_percent"]["V"]) + ',')

        # Obtendo caracteristicas de b
        lista_aux = j.split()
        Features = GetFeatures(lista_aux[0])
        # Elementos monovalorados
        #arquivo_c.write(str(lista_aux[1]) + ',')
        arquivo_c.write(str(Features.get("Molecular_weight")) + ',')
        arquivo_c.write(str(Features.get("Aromaticity")) + ',')
        arquivo_c.write(str(Features.get("Instability_index")) + ',')
        arquivo_c.write(str(Features.get("Isoelectric_point")) + ',')
        # Elementos multivalorados
        for b in Features.get("Second_structure_fraction"):
            arquivo_c.write(str(b) + ',')

        # Elementos de Count_amino_acids

        arquivo_c.write(str(Features["Count_amino_acids"]["A"]) + ',')
        arquivo_c.write(str(Features["Count_amino_acids"]["R"]) + ',')
        arquivo_c.write(str(Features["Count_amino_acids"]["N"]) + ',')
        arquivo_c.write(str(Features["Count_amino_acids"]["D"]) + ',')
        arquivo_c.write(str(Features["Count_amino_acids"]["C"]) + ',')
        arquivo_c.write(str(Features["Count_amino_acids"]["E"]) + ',')
        arquivo_c.write(str(Features["Count_amino_acids"]["Q"]) + ',')
        arquivo_c.write(str(Features["Count_amino_acids"]["G"]) + ',')
        arquivo_c.write(str(Features["Count_amino_acids"]["H"]) + ',')
        arquivo_c.write(str(Features["Count_amino_acids"]["I"]) + ',')
        arquivo_c.write(str(Features["Count_amino_acids"]["L"]) + ',')
        arquivo_c.write(str(Features["Count_amino_acids"]["K"]) + ',')
        arquivo_c.write(str(Features["Count_amino_acids"]["M"]) + ',')
        arquivo_c.write(str(Features["Count_amino_acids"]["F"]) + ',')
        arquivo_c.write(str(Features["Count_amino_acids"]["P"]) + ',')
        arquivo_c.write(str(Features["Count_amino_acids"]["S"]) + ',')
        arquivo_c.write(str(Features["Count_amino_acids"]["T"]) + ',')
        arquivo_c.write(str(Features["Count_amino_acids"]["W"]) + ',')
        arquivo_c.write(str(Features["Count_amino_acids"]["Y"]) + ',')
        arquivo_c.write(str(Features["Count_amino_acids"]["V"]) + ',')

        # Elementos de Amino_acids_percent

        arquivo_c.write(str(Features["Amino_acids_percent"]["A"]) + ',')
        arquivo_c.write(str(Features["Amino_acids_percent"]["R"]) + ',')
        arquivo_c.write(str(Features["Amino_acids_percent"]["N"]) + ',')
        arquivo_c.write(str(Features["Amino_acids_percent"]["D"]) + ',')
        arquivo_c.write(str(Features["Amino_acids_percent"]["C"]) + ',')
        arquivo_c.write(str(Features["Amino_acids_percent"]["E"]) + ',')
        arquivo_c.write(str(Features["Amino_acids_percent"]["Q"]) + ',')
        arquivo_c.write(str(Features["Amino_acids_percent"]["G"]) + ',')
        arquivo_c.write(str(Features["Amino_acids_percent"]["H"]) + ',')
        arquivo_c.write(str(Features["Amino_acids_percent"]["I"]) + ',')
        arquivo_c.write(str(Features["Amino_acids_percent"]["L"]) + ',')
        arquivo_c.write(str(Features["Amino_acids_percent"]["K"]) + ',')
        arquivo_c.write(str(Features["Amino_acids_percent"]["M"]) + ',')
        arquivo_c.write(str(Features["Amino_acids_percent"]["F"]) + ',')
        arquivo_c.write(str(Features["Amino_acids_percent"]["P"]) + ',')
        arquivo_c.write(str(Features["Amino_acids_percent"]["S"]) + ',')
        arquivo_c.write(str(Features["Amino_acids_percent"]["T"]) + ',')
        arquivo_c.write(str(Features["Amino_acids_percent"]["W"]) + ',')
        arquivo_c.write(str(Features["Amino_acids_percent"]["Y"]) + ',')
        arquivo_c.write(str(Features["Amino_acids_percent"]["V"]) + ',')

        #PPI
        arquivo_c.write(PPI + "\n")

        #fechando arquivos
    arquivo_a.close()
    arquivo_b.close()



def main():


    arquivo_c = open("Database.csv", 'w')

    # Cabecarios .CSV
    arquivo_c.write("sep = ,\n")
    # Protein_a
    arquivo_c.write("a_Molecular_weight,a_Aromaticity,a_Instability_index,a_Isoelectric_point,"
                    "a_SSF_Helix,a_SSF_Turn,a_SSF_Sheet,"
                    "a_A,a_R,a_N,a_D,a_C,a_E,a_Q,a_G,a_H,a_I,a_L,a_K,a_M,a_F,a_P,a_S,a_T,a_W,a_Y,a_V,"
                    "a_Percent_A,a_Percent_R,a_Percent_N,a_Percent_D,a_Percent_C,a_Percent_E,a_Percent_Q,"
                    "a_Percent_G,a_Percent_H,a_Percent_I,a_Percent_L,a_Percent_K,a_Percent_M,a_Percent_F,"
                    "a_Percent_P,a_Percent_S,a_Percent_T,a_Percent_W,a_Percent_Y,a_Percent_V,")

    # Protein_b
    arquivo_c.write("b_Molecular_weight,b_Aromaticity,b_Instability_index,b_Isoelectric_point,"
                    "b_SSF_Helix,b_SSF_Turn,b_SSF_Sheet,"
                    "b_A,b_R,b_N,b_D,b_C,b_E,b_Q,b_G,b_H,b_I,b_L,b_K,b_M,b_F,b_P,b_S,b_T,b_W,b_Y,b_V,"
                    "b_Percent_A,b_Percent_R,b_Percent_N,b_Percent_D,b_Percent_C,b_Percent_E,b_Percent_Q,"
                    "b_Percent_G,b_Percent_H,b_Percent_I,b_Percent_L,b_Percent_K,b_Percent_M,b_Percent_F,"
                    "b_Percent_P,b_Percent_S,b_Percent_T,b_Percent_W,b_Percent_Y,b_Percent_V,")
    # PPI
    arquivo_c.write("PPI\n")

    MakeSCV(arquivo_c,"N_protein_a", "N_protein_b","0")
    MakeSCV(arquivo_c, "P_protein_a", "P_protein_b", "1")
    arquivo_c.close()


if __name__ == '__main__':
    main()
