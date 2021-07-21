import math
def criterio_linhas(matriz):
    guardar_resultado=[]
    cont=0
    while cont< len(matriz):
        equaçao=matriz[cont]
        tamanhoequação=len(equaçao)-1
        cont2=0
        
        alpha=0
        while cont2< tamanhoequação:
            if cont2 == cont:
                cont2=cont2+1
               
                if cont2 >= tamanhoequação:
                    break
            
            alpha=alpha+math.fabs(int(equaçao[cont2]))
            
            cont2=cont2+1
        guardar_resultado.append(alpha/int(equaçao[cont]))
        
        cont=cont+1
    cont=0
    
    while cont< len(guardar_resultado):
        if guardar_resultado[cont]>1:
            print("nao converge")
            return(0)
        cont=cont+1
    return(1)
    
def x0(matriz):
    cont=0
    x0=[]
    while cont< len(matriz):
        equação=matriz[cont]
        x0.append(int(equação[-1])/int(equação[cont]))
        cont=cont+1
    
    return(x0)
    
def criterio_parada(k):
    
    equação_ultima=k[-1]
    penultima_equação=k[-2]
    cont=0
    maior_diferença=0
    

    while cont<len(penultima_equação):
        
        x=math.fabs(equação_ultima[cont]-penultima_equação[cont])
        if x>maior_diferença:
            maior_diferença=x       
        cont=cont+1
        
    valor_maior=max(equação_ultima,key=int)
    porcentagem_erro=maior_diferença/valor_maior
    return(porcentagem_erro)

def calculo_variaveis(matriz,k):   
    cont=0
    guardar_resultado=[]
    

    while cont< len(matriz):
        #print("cont1="+str(cont))
        cont2=0
        equação=matriz[cont]
        alpha=int(equação[-1])
        ultimo=k[-1]
        
        
        while cont2< len(equação)-1:
            if cont2 == cont:
                cont2=cont2+1           
            #print("cont2="+str(cont2))
            if cont2<len(equação)-1:
                alpha=float(alpha)-float(equação[cont2])*float(ultimo[cont2])
                cont2=cont2+1        
                
                
        guardar_resultado.append(alpha/int(equação[cont]))
        
        
        cont=cont+1
    return(guardar_resultado)
matriz=[]
numero_equacoes=int(input("Digite o numero de equacoes: "))
precisao=float(input("Digite a precisao: "))
cont=0
while cont<numero_equacoes:
    vetor=input("Digite as constantes separadas por espaço, e apos a ultima constante digite o resultado separado por espaço: ")
    matriz.append(vetor.split( ))
    cont=cont+1
cont=0
while cont <numero_equacoes:
    
    cont=cont+1
resultado=criterio_linhas(matriz)

if resultado==1:
    k=[]
    k.append(x0(matriz))
    
    erro=9999999999
    while erro> precisao: 
        
        k.append(calculo_variaveis(matriz,k))
        
        erro=criterio_parada(k)
              
    print("O vetor solução encontrado foi :"+str(k[-1])+"Com um erro igual a:"+str(erro)) 
        
### 4 -2 -1 0 10  Exemplo de como digitar as constantes do vetor
### -2 9 0 -5 -5
### -1 0 6 -3 0
###0 -5 -3 10 0

