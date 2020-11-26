import math
import statistics

ref_arquivo2=open("column_3C.dat","r")
ref_arquivo =open("column_3C_test.dat","r")
ref_arquivo3=open("teste.txt","w")


def k_menor_lista(lista1,lista2):
    l=[]
    m=[]

    for i in range(9):
        menor= min(lista1)
        x=lista1.index(menor)
        l.append(menor)
        m.append(lista2[x])
        lista1.remove(menor)
        lista2.remove(lista2[x])
    st=statistics.mode(m)



    return l, m, st

def arquivo_para_lista(arq):
   
    linha=arq.readline()
    lista=[]
    while linha:
        valores=linha.split()
        lista.append(valores)
        linha=arq.readline()

    ref_arquivo.close()

    return lista




def diagnostico_K_vizinhos(lista,lista2):
    lista3=[]
    lista4=[]
    cont=0
    for i in range(len(lista)):
        print("Paciente %i  :" %(i+1))
        diagnostico1=lista[i][6]

        for j in range(len(lista2)):
            dist=round(math.sqrt(pow(float(lista[i][0])-float(lista2[j][0]),2)+pow(float(lista[i][1])-float(lista2[j][1]),2)+pow(float(lista[i][2])-float(lista2[j][2]),2)+pow(float(lista[i][3])-float(lista2[j][3]),2)+pow(float(lista[i][4])-float(lista2[j][4]),2)+pow(float(lista[i][5])-float(lista2[j][5]),2)),2)
            diag=lista2[j][6]
            lista3.append(dist)
            lista4.append(diag)

        print('\n')
        print('Diagnóstico real :' , diagnostico1)
        print('Dados do paciente : ',lista[i])
        print('Diagnostico do software' ,k_menor_lista(lista3,lista4)[2])
        print('Dados dos K_vizinhos do software', k_menor_lista(lista3, lista4))
        if k_menor_lista(lista3, lista4)[2] == diagnostico1:
            cont+=1
               

        ref_arquivo3.write('Atributos  do Paciente'+ str(lista[i]))
        ref_arquivo3.write('\n')
        ref_arquivo3.write('Classificação pelo algoritmo  :'+str(k_menor_lista(lista3, lista4)[2]))
        ref_arquivo3.write('\n')
        ref_arquivo3.write('Classificação  real :'+str(diagnostico1))
        ref_arquivo3.write('\n')
    print(cont)
    print('A porcentagem de acertos do software é de %.2f e de erros é %.2f  '%((cont/155)*100,100 -(cont/155)*100))
    acertos=round((cont/155)*100,2)
    erros=100-acertos
    ref_arquivo3.write('A porcentagem de acertos do software é de '+str(acertos))
    ref_arquivo3.write('\n')
    ref_arquivo3.write('A porcentagem de erros do software é de '+str(erros))

    ref_arquivo3.close()
  

        
    
diagnostico_K_vizinhos(arquivo_para_lista(ref_arquivo),arquivo_para_lista(ref_arquivo2))

