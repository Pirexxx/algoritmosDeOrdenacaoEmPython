#Importação das Bibliotecas  :D
import time
import random

#Definindo as funções que serão usadas!
def bubble_sort(lista):#TIPO DE ORDENAÇÃO EM BOLHA!!!
    final_lista = len(lista) #Define o tamanho da lista, para percorrê-la
    for i in range(final_lista-1,0,-1):#Usando o (tamanho da lista -1) para evitar erros de Out of Index range
        for j in range(i):#J sera usado como index do elemento!Por isso optamos pelo range(i) que retorna um valor int
            if lista[j]>lista[j+1]:#Testa se o elemento j é maior que elemento seguinte!
                lista[j],lista[j+1] = lista[j+1],lista[j] #Caso seja, amobos elementos trocam de lugar!
    return(lista)
    """Ao final do laço for, todos os valores serão ordenados de forma crescente,
    pois a cada itereção do laço for mais externo, a lista estará mais ordenada.
    E na última itereção, a lista estará totalmente ordenada. :^) """

def ord_selecao(lista):#TIPO DE ORDENAÇÃO POR SELEÇÃO!!!
    n = len(lista) #Tamanho da lista
    for i in range(n):# Percorre a lista, utilizando o tamanho da lista busca o menor valor da lista.
        min = i 
        for j in range(i + 1, n): # i + 1 pois o valor minimo ja é i, começando assim pelo i + 1...
            if lista[min] > lista[j]: #...e trocando caso haja algum valor menor.
                min = j
        lista[i], lista[min] = lista[min], lista[i] # Colocando o elemento mínimo na posição correta(trocando de lugar com o valor na posição incorreta).
    return(lista)

def ord_insercao(lista):#TIPO DE ORDENAÇÃO POR INSERÇÃO!!!
    n = len(lista) #Tamanho da lista, utilizado nos laços
    for i in range(1,n):
        chave = lista[i] #Chave é o elemento que está na posição...
        #... que utilizamos para testa-lo e ver se ele é menor que o elementos ja presentes na lista
        j = i - 1 # Começamos na parcela da lista que ja esta ordenada no caso o (i-1)
        while j >= 0 and lista[j] > chave:#2ª condição: Verificamos se o numero que está sendo analisado...
        #... é menor que a chave, caso seja, a lista ja está ordenada e podemos parar a iteração 
            lista[j+1] = lista[j] #Caso a condição seja verdadeira, o valor j será inserido no lugar do valor seguinte
            j = j - 1
        lista[j+1] = chave #Encontramos a posição em que o valor chave deve ser inserido...
        #... no caso, uma posição antes do local em que o numero deve ser inserido...
        # (i-1), que somado a 1 [(i-1) + 1] = i.
    return(lista)

#A função sort ja é padrão do Python : )
#Bloco principal do código!

valores_100 = 100 # Quantidade de valores a serem gerados!
valores_1000 = 1000 # Quantidade de valores a serem gerados!
valores_10k = 10000 # Quantidade de valores a serem gerados!

#Montando as Listas de números
lista100 = [random.randint(0,valores_100) for num in range(valores_100)] #Insere numeros aleatórios na lista de 100 valores.
lista_copia_100 = [] #Montando...
for valor in lista100: #...Uma cópia...
    lista_copia_100.append(valor) #...Da lista de 100 Valores

lista1000 = [random.randint(0,valores_1000) for num in range(valores_1000)] #Insere numeros aleatórios na lista de 1000 valores.
lista_copia_1000 = [] #Montando...
for valor in lista1000: #...Uma cópia...
    lista_copia_1000.append(valor) #...Da lista de 1000 Valores

lista10k = [random.randint(0,valores_10k) for num in range(valores_10k)] #Insere numeros aleatórios na lista de 10 mil valores.
lista_copia_10k = [] #Montando...
for valor in lista10k: #...Uma cópia...
    lista_copia_10k.append(valor) #...Da lista de 10k de Valores

lista_tempo_bubble,lista_tempo_selection,lista_tempo_insert,lista_tempo_sort = [],[],[],[]

#Bloco de chamada das funções e medição do tempo:

''' ----------------------------------ORDENAÇÕES EM BOLHA (BUBBLE SORT)-----------------------------------'''

start = float(time.time()) #1 - Inicia a contagem do tempo 
x100 = bubble_sort(lista_copia_100) # Chama a função de ordenação em bolhas para 100 números
#end = float(time.time()) #1 - Finaliza a contagem do tempo 
time.sleep(0.000000000000002)
delta = (time.time()) - start #Calcula o tempo de execução total do código
tempo1 = delta #Salvando o tempo em uma váriavel diferente (Só estou salvando nas ordenções com listas de 100 valores)
lista_tempo_bubble.append(delta) #Salvando os valores de Bubble para comparar com os outros!
print(f"Usando a Ordenação por Bolhas, o tempo total de execução do programa com 100 numeros, foi de: {delta:.20f}")

start = float(time.time()) #2 - Inicia a contagem do tempo
x1000 = bubble_sort(lista_copia_1000) #Chama a função de ordenação em bolhas para 1000 números
#end = float(time.time()) #2 - Finaliza a contagem do tempo.
time.sleep(0.000000000000002)
delta = (time.time()) - start #Calcula o tempo d eexecução total do código
lista_tempo_bubble.append(delta) #Salvando os valores de Bubble para comparar com os outros!
print(f"Usando a Ordenação por Bolhas, o tempo total de execução do programa com 1000 numeros foi de: {delta:.20f}")

start = float(time.time()) #3 - Inicia a contagem do tempo 
x10k = bubble_sort(lista_copia_10k) # Chama a função de ordenação em bolhas para 10 mil números
#end = float(time.time()) #3 - Finaliza a contagem do tempo
time.sleep(0.000000000000002)
delta = (time.time()) - start # Calcula o tempo de execução final do código
lista_tempo_bubble.append(delta) #Salvando os valores de Bubble para comparar com os outros!
print(f"Usando a Ordenação por Bolhas, o tempo total de execução do programa com 10000 foi de: {delta:.20f}")

''' -----------------------------------------ORDENAÇÕES POR SELEÇÃO---------------------------------------'''

start = float(time.time()) #1 - Inicia a contagem do tempo 
y100 = ord_selecao(lista_copia_100) # Chama a função de ordenação por seleção para 100 números
#end = float(time.time()) #1 - Finaliza a contagem do tempo
time.sleep(0.000000000000002)
delta = (time.time()) - start # Calcula o tempo de execução final da função
tempo2 = delta #Salvando o tempo em uma váriavel diferente (Só estou salvando nas ordenações com listas de 100 valores)
lista_tempo_selection.append(delta) #Salvando os valores de Selection para comparar com os outros!
print(f"Usando a Ordenação por Seleção, o tempo total de execução do programa com 100 foi de: {delta:.20f}")

start = float(time.time()) #2 - Inicia a contagem do tempo 
y1000 = ord_selecao(lista_copia_1000) # Chama a função de ordenação por seleção para 1000 números
#end = float(time.time()) #2 - Finaliza a contagem do tempo
time.sleep(0.000000000000002)
delta = (time.time()) - start # Calcula o tempo de execução final da função
lista_tempo_selection.append(delta) #Salvando os valores de Selection para comparar com os outros!
print(f"Usando a Ordenação por Seleção, o tempo total de execução do programa com 1000 foi de: {delta:.20f}")

start = float(time.time()) #3 - Inicia a contagem do tempo
y10k = ord_selecao(lista_copia_10k) # Chama a função de ordenação por seleção para 10 mil números
#end = float(time.time()) #3 - Finaliza a contagem do tempo
time.sleep(0.000000000000002)
delta = (time.time()) - start # Calcula o tempo de execução final da função
lista_tempo_selection.append(delta) #Salvando os valores de Selection para comparar com os outros!
print(f"Usando a Ordenação por Seleção, o tempo total de execução do programa com 10000 foi de: {delta:.20f}")

''' -----------------------------------------ORDENAÇÕES POR INSERÇÃO---------------------------------------'''

start = float(time.time()) #1 - Inicia a contagem do tempo
z100 = ord_insercao(lista_copia_100) # Chama a função de ordenação por inserção para 100 números
#end = float(time.time()) #1 - Finaliza a contagem do tempo
time.sleep(0.000000000000002)
delta = (time.time()) - start # Calcula o tempo de execução final da função
tempo3 = delta #Salvando o tempo em uma váriavel diferente (Só estou salvando nas ordenações com listas de 100 valores)
lista_tempo_insert.append(delta) #Salvando os valores de Insert para comparar com os outros!
print(f"Usando a Ordenação por Inserção, o tempo total de execução do programa com 100 foi de: {delta:.20f}")

start = float(time.time()) #2 - Inicia a contagem do tempo
z1000 = ord_insercao(lista_copia_1000) # Chama a função de ordenação por inserção para 1000 números
#end = float(time.time()) #2 - Finaliza a contagem do tempo
time.sleep(0.000000000000002)
delta = (time.time()) - start # Calcula o tempo de execução final da função
lista_tempo_insert.append(delta) #Salvando os valores de Insert para comparar com os outros!
print(f"Usando a Ordenação por Inserção, o tempo total de execução do programa com 1000 foi de: {delta:.20f}")

start = float(time.time()) #3 -Inicia a contagem do tempo
z10k = ord_insercao(lista_copia_10k) # Chama a função de ordenação por inserção para 10k números
#end = float(time.time()) #3 - Finaliza a contagem do tempo
time.sleep(0.000000000000002)
delta = (time.time()) - start # Calcula o tempo de execução final da função
lista_tempo_insert.append(delta) #Salvando os valores de Insert para comparar com os outros!
print(f"Usando a Ordenação por Inserção, o tempo total de execução do programa com 10000 foi de: {delta:.20f}")

''' ------------------------------------ORDENAÇÕES PELA FUNÇÃO SORT()---------------------------------------'''

#Utilizando a função Sort(), que é nativa do PYTHON!

start = float(time.time()) #1 - Inicia a contagem do tempo
w100 = lista_copia_100.sort() #Chama a função de ordenação com o Sort() para 100 números
#end = float(time.time()) #1 - Finaliza a contagem do tempo
time.sleep(0.000000000000002)
delta = (time.time()) - start # Calcula o tempo de execução final da função
tempo4 = delta #Salvando o tempo em uma váriavel diferente (Só estou salvando nas ordenações com listas de 100 valores)
lista_tempo_sort.append(delta) #Salvando os valores de Sort() para comparar com os outros!
print(f"Usando a Ordenação com a função Sort() do PYTHON, o tempo total de execução do programa com 100 foi de: {delta:.20f}")

start = float(time.time()) #2 - Inicia a contagem do tempo
w1000 = lista1000.sort() #Chama a função de ordenação com o Sort() para 1000 números
#end = float(time.time()) #2 - Finaliza a contagem do tempo
time.sleep(0.000000000000002)
delta = (time.time()) - start # Calcula o tempo de execução final da função
lista_tempo_sort.append(delta) #Salvando os valores de Sort() para comparar com os outros!
print(f"Usando a Ordenação com a função Sort() do PYTHON, o tempo total de execução do programa com 1000 foi de: {delta:.20f}")

start = float(time.time()) #2 - Inicia a contagem do tempo
w10k = lista_copia_10k.sort() #Chama a função de ordenação com o Sort() para 10k números
#end = float(time.time()) #2 - Finaliza a contagem do tempo
time.sleep(0.000000000000002)
delta = (time.time()) - start # Calcula o tempo de execução final da função
lista_tempo_sort.append(delta) #Salvando os valores de Sort() para comparar com os outros!
print(f"Usando a Ordenação com a função Sort() do PYTHON, o tempo total de execução do programa com 10000 foi de: {delta:.20f}")

print() # Pular uma linha

# Calculando o menor tempo e qual tipo de seleção ele é:

matriz_tempo = [] #Montando...
matriz_tempo.append(lista_tempo_bubble) #... a matriz...
matriz_tempo.append(lista_tempo_selection) #... com todos...
matriz_tempo.append(lista_tempo_insert) #... os valores...
matriz_tempo.append(lista_tempo_sort) #... de tempo...

menor = 100000 # Variável para guardar o menor tempo
menor_ind_i = 0 #Variável para guardar o indice i do menor tempo
menor_ind_j = 0 # Variavel para guardar o indice j do menor tempo

#Menor tempo, em Listas de 100 valores, e qual foi o tipo de Ordenação:

for i in range(len(matriz_tempo)): #Esses laços percorrem a matriz, onde i e j serão usados para recuperar o indice do menor valor
    for j in range(len(matriz_tempo[i])): #Esse laço percorre a lista de indice i dentro da matriz
            if matriz_tempo[i][0] < menor: # Como queremos recuperar os tempos das listas de 100 valores, o indice sempre será i e o indice 0
                menor = matriz_tempo[i][0] # Se as condições forem satisfeitas, guardamos o valor de tempo e...
                menor_ind_i = i #... o indice
if menor_ind_i == 0: #Esses condicionais são usados para identificar qual o tipo de Ordenação será printado no final
    string = "Ordenação em Bolha"
if menor_ind_i == 1:
    string = "Ordenação por Seleção"
if menor_ind_i == 2:
    string = "Ordenação por Inserção"
if menor_ind_i == 3:
    string = "Ordenação pela Função Sort"
print(f"Para listas de 100 Valores, o menor tempo foi de: {menor:.20f} e o tipo de ordenação foi: {string}")

#Zeramos as variaveis iniciais para reutiliza-las

menor = 100000 # Variável para guardar o menor tempo
menor_ind_i = 0 #Variável para guardar o indice i do menor tempo
menor_ind_j = 0 # Variavel para guardar o indice j do menor tempo

#Menor tempo, em Listas de 1000 valores, e qual foi o tipo de Ordenação:

for i in range(len(matriz_tempo)): #Esses laços percorrem a matriz, onde i e j serão usados para recuperar o indice do menor valor
    for j in range(len(matriz_tempo[i])): #Esse laço percorre a lista de indice i dentro da matriz
            if matriz_tempo[i][1] < menor: # Como queremos recuperar os tempos das listas de 1000 valores, o indice sempre será i e o indice 1
                menor = matriz_tempo[i][1] # Se as condições forem satisfeitas, guardamos o valor de tempo e...
                menor_ind_i = i #... o indice
if menor_ind_i == 0: #Esses condicionais são usados para identificar qual o tipo de Ordenação será printado no final
    string = "Ordenação em Bolha"
if menor_ind_i == 1:
    string = "Ordenação por Seleção"
if menor_ind_i == 2:
    string = "Ordenação por Inserção"
if menor_ind_i == 3:
    string = "Ordenação pela Função Sort"
print(f"Para listas de 1000 Valores, o menor tempo foi de: {menor:.20f} e o tipo de ordenação foi: {string}")

#Zeramos as variaveis iniciais para reutiliza-las

menor = 100000 # Variável para guardar o menor tempo
menor_ind_i = 0 #Variável para guardar o indice i do menor tempo
menor_ind_j = 0 # Variavel para guardar o indice j do menor tempo

#Menor tempo, em Listas de 10k de valores, e qual foi o tipo de Ordenação:

for i in range(len(matriz_tempo)): #Esses laços percorrem a matriz, onde i e j serão usados para recuperar o indice do menor valor
    for j in range(len(matriz_tempo[i])): #Esse laço percorre a lista de indice i dentro da matriz
            if matriz_tempo[i][2] < menor: # Como queremos recuperar os tempos das listas de 10k de valores, o indice sempre será i e o indice 2
                menor = matriz_tempo[i][2] # Se as condições forem satisfeitas, guardamos o valor de tempo e...
                menor_ind_i = i #... o indice
if menor_ind_i == 0: #Esses condicionais são usados para identificar qual o tipo de Ordenação será printado no final
    string = "Ordenação em Bolha"
if menor_ind_i == 1:
    string = "Ordenação por Seleção"
if menor_ind_i == 2:
    string = "Ordenação por Inserção"
if menor_ind_i == 3:
    string = "Ordenação pela Função Sort"
print(f"Para listas de 10k de Valores, o menor tempo foi de: {menor:.20f} e o tipo de ordenação foi: {string}")