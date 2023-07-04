import random

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

valores_100 = 100 # Quantidade de valores a serem gerados!
valores_1000 = 1000 # Quantidade de valores a serem gerados!
valores_10k = 10000 # Quantidade de valores a serem gerados!

#Montando as Listas de números
lista100 = [random.randint(0,valores_100) for num in range(valores_100)] #Insere numeros aleatórios na lista de 100 valores.
lista_copia_100 = [] # Montando
for valor in lista100: # Uma cópia
    lista_copia_100.append(valor) # Da lista de 100 Valores

lista1000 = [random.randint(0,valores_1000) for num in range(valores_1000)] #Insere numeros aleatórios na lista de 1000 valores.
lista_copia_1000 = [] # Montando
for valor in lista1000: # Uma cópia
    lista_copia_1000.append(valor) # Da lista de 1000 Valores

lista10k = [random.randint(0,valores_10k) for num in range(valores_10k)] #Insere numeros aleatórios na lista de 10 mil valores.
lista_copia_10k = [] # Montando
for valor in lista10k: # Uma cópia
    lista_copia_10k.append(valor) #Da lista de 10k Valores
