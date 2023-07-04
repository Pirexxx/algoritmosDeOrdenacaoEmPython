import PySimpleGUI as sgui
import joaopedro_de_oliveira_pires_funcoes as tst
import random
import time


#Definindo algumas variáveis e funções para uso na Interface Gráfica!

#Montando as Listas de números
lista100 = [random.randint(0,100) for num in range(100)] #Insere numeros aleatórios na lista de 100 valores.
lista_copia_100 = [] #Montando
for valor in lista100: #Uma cópia
    lista_copia_100.append(valor) #Da lista de 100 Valores

lista1000 = [random.randint(0,1000) for num in range(1000)] #Insere numeros aleatórios na lista de 1000 valores.
lista_copia_1000 = []
for valor in lista1000:
    lista_copia_1000.append(valor)

lista10k = [random.randint(0,10000) for num in range(10000)] #Insere numeros aleatórios na lista de 10 mil valores.
lista_copia_10k = []
for valor in lista10k:
    lista_copia_10k.append(valor)

lista_tempo100,lista_tempo1000,lista_tempo10k = [],[],[]

# Bloco de código para a Interface Gráfica 2:^D

#Tema da Interface:

sgui.theme('Blue Purple') 

#Layout
layout = [
    [sgui.Text('Quantidade de Números em Lista')],
    [sgui.Button('100 Números',key='cem'), 
    sgui.Button('1000 Números',key='mil'), 
    sgui.Button('10 mil Números',key='10mil')],
    [sgui.Text('Ordenação em Bolhas')],
    [sgui.Button('Executar',key='Bolhas')],
    [sgui.Text('Ordenação por Seleção')],
    [sgui.Button('Executar',key='Seleção')],
    [sgui.Text('Ordenação por Inserção')],
    [sgui.Button('Executar',key='Inserção')],
    [sgui.Text('Ordenação pela Função Sort')],
    [sgui.Button('Executar',key='Sort')],
    [sgui.Text('',key='texto')],
    [sgui.Button('Sair',key='fechar')]

]
#Janela
janela = sgui.Window('Tempo de Execução com Diferentes tipos de Ordenação de Listas', layout, size = (850,400))
qntd_num = ''
while True:
    eventos, valores = janela.read()
    if eventos == sgui.WINDOW_CLOSED or eventos == 'fechar': #Caso usuário queira fechar a janela
        break
    if eventos == 'cem' or eventos == 'mil' or eventos == '10mil': #Escolha da quantidade de números na lista
        qntd_num = eventos
    

    '''Ordenação em Bolhas'''

    if eventos == 'Bolhas' and qntd_num == 'cem': # Caso 1.1 - Ordenação em Bolha - Lista de 100 números
        start = float(time.time()) #1 - Inicia a contagem do tempo 
        x100 = tst.bubble_sort(lista_copia_100) # Chama a função de ordenação em bolhas para 100 números
        #end = float(time.time()) #1 - Finaliza a contagem do tempo
        time.sleep(0.000000000000002)
        delta = time.time() - start #Calcula o tempo de execução total do código
        tempo1 = delta #Salvando o tempo em uma váriavel diferente (Só estou salvando nas ordenções com listas de 100 valores)
        lista_tempo100.append(delta) #Salvando todos os valores de tempo em uma única lista para comparar depois
        janela['texto'].update(f"Usando a Ordenação por Bolhas, o tempo total de execução do programa com 100 numeros, foi de: {delta:.20f}")

    if eventos == 'Bolhas' and qntd_num == 'mil': # Caso 1.2 - Ordenação em Bolha - Lista de 1000 números
        start = float(time.time()) #2 - Inicia a contagem do tempo
        x1000 = tst.bubble_sort(lista1000) #Chama a função de ordenação em bolhas para 1000 números
        #end = float(time.time()) #2 - Finaliza a contagem do tempo.
        time.sleep(0.000000000000002)
        delta = time.time() - start #Calcula o tempo de execução total do código
        lista_tempo1000.append(delta) #Salvando todos os valores de tempo em uma única lista para comparar depois
        janela['texto'].update(f"Usando a Ordenação por Bolhas, o tempo total de execução do programa com 1000 numeros foi de: {delta:.20f}")

    if eventos == 'Bolhas' and qntd_num == '10mil': # Caso 1.3 - Ordenação em Bolha - Lista de 10 mil números
        start = float(time.time()) #3 - Inicia a contagem do tempo 
        x10k = tst.bubble_sort(lista_copia_10k) # Chama a função de ordenação em bolhas para 10 mil números
        #end = float(time.time()) #3 - Finaliza a contagem do tempo
        time.sleep(0.000000000000002)
        delta = time.time() - start #Calcula o tempo de execução total do código
        lista_tempo10k.append(delta) #Salvando todos os valores de tempo em uma única lista para comparar depois
        janela['texto'].update(f"Usando a Ordenação por Bolhas, o tempo total de execução do programa com 10000 foi de: {delta:.20f}")


    '''Ordenação por Seleção'''

    if eventos == 'Seleção' and qntd_num == 'cem': # Caso 2.1 - Ordenação por Seleção - Lista de 100 números
        start = float(time.time()) #1 - Inicia a contagem do tempo 
        y100 = tst.ord_selecao(lista_copia_100) # Chama a função de ordenação por seleção para 100 números
        #end = float(time.time()) #1 - Finaliza a contagem do tempo
        time.sleep(0.000000000000002)
        delta = time.time() - start #Calcula o tempo de execução total do código
        tempo2 = delta #Salvando o tempo em uma váriavel diferente (Só estou salvando nas ordenações com listas de 100 valores)
        lista_tempo100.append(delta) #Salvando todos os valores de tempo em uma única lista para comparar depois
        janela['texto'].update(f"Usando a Ordenação por Seleção, o tempo total de execução do programa com 100 foi de: {delta:.20f}")

    if eventos == 'Seleção' and qntd_num == 'mil': # Caso 2.2 - Ordenação por Seleção - Lista de 1000 números
        start = float(time.time()) #2 - Inicia a contagem do tempo 
        y1000 = tst.ord_selecao(lista_copia_1000) # Chama a função de ordenação por seleção para 1000 números
        #end = float(time.time()) #2 - Finaliza a contagem do tempo
        time.sleep(0.000000000000002)
        delta = time.time() - start #Calcula o tempo de execução total do código
        lista_tempo1000.append(delta) #Salvando todos os valores de tempo em uma única lista para comparar depois
        janela['texto'].update(f"Usando a Ordenação por Seleção, o tempo total de execução do programa com 1000 foi de: {delta:.20f}")

    if eventos == 'Seleção' and qntd_num == '10mil': # Caso 2.3 - Ordenação por Seleção - Lista de 10 mil números 
        start = float(time.time()) #3 - Inicia a contagem do tempo
        y10k = tst.ord_selecao(lista_copia_10k) # Chama a função de ordenação por seleção para 10 mil números
        #end = float(time.time()) #3 - Finaliza a contagem do tempo
        time.sleep(0.000000000000002)
        delta = time.time() - start #Calcula o tempo de execução total do código
        lista_tempo10k.append(delta) #Salvando todos os valores de tempo em uma única lista para comparar depois
        janela['texto'].update(f"Usando a Ordenação por Seleção, o tempo total de execução do programa com 10000 foi de: {delta:.20f}")


    '''Ordenação por Inserção'''

    if eventos == 'Inserção' and qntd_num == 'cem': # Caso 3.1 - Ordenação por Inserção - Lista de 100 números
        start = float(time.time()) #1 - Inicia a contagem do tempo
        z100 = tst.ord_insercao(lista_copia_100) # Chama a função de ordenação por inserção para 100 números
        #end = float(time.time()) #1 - Finaliza a contagem do tempo
        time.sleep(0.000000000000002)
        delta = time.time() - start #Calcula o tempo de execução total do código
        tempo3 = delta #Salvando o tempo em uma váriavel diferente (Só estou salvando nas ordenações com listas de 100 valores)
        lista_tempo100.append(delta) #Salvando todos os valores de tempo em uma única lista para comparar depois
        janela['texto'].update(f"Usando a Ordenação por Inserção, o tempo total de execução do programa com 100 foi de: {delta:.20f}")

    if eventos == 'Inserção' and qntd_num == 'mil': # Caso 3.2 - Ordenação por Inserção - Lista de 1000 números
        start = float(time.time()) #2 - Inicia a contagem do tempo
        z1000 = tst.ord_insercao(lista_copia_1000) # Chama a função de ordenação por inserção para 1000 números
        #end = float(time.time()) #2 - Finaliza a contagem do tempo
        time.sleep(0.000000000000002)
        delta = time.time() - start #Calcula o tempo de execução total do código
        lista_tempo1000.append(delta) #Salvando todos os valores de tempo em uma única lista para comparar depois
        janela['texto'].update(f"Usando a Ordenação por Inserção, o tempo total de execução do programa com 1000 foi de: {delta:.20f}")

    if eventos == 'Inserção' and qntd_num == '10mil': # Caso 3.3 - Ordenação por Inserção - Lista de 10 mil números
        start = float(time.time()) #3 -Inicia a contagem do tempo
        z10k = tst.ord_insercao(lista_copia_10k) # Chama a função de ordenação por inserção para 10k números
        #end = float(time.time()) #3 - Finaliza a contagem do tempo
        time.sleep(0.000000000000002)
        delta = time.time() - start #Calcula o tempo de execução total do código
        lista_tempo10k.append(delta) #Salvando todos os valores de tempo em uma única lista para comparar depois
        janela['texto'].update(f"Usando a Ordenação por Inserção, o tempo total de execução do programa com 10000 foi de: {delta:.20f}")


    '''Ordenação pela Função SORT() do PYTHON!'''

    if eventos == 'Sort' and qntd_num == 'cem': # Caso 4.1 - Ordenação pela Função Sort - Lista de 100 números
        start = float(time.time()) #1 - Inicia a contagem do tempo
        w100 = lista_copia_100.sort() #Chama a função de ordenação com o Sort() para 100 números
        #end = float(time.time()) #1 - Finaliza a contagem do tempo
        time.sleep(0.000000000000002)
        delta = time.time() - start #Calcula o tempo de execução total do código
        tempo4 = delta #Salvando o tempo em uma váriavel diferente (Só estou salvando nas ordenações com listas de 100 valores)
        lista_tempo100.append(delta) #Salvando todos os valores de tempo em uma única lista para comparar depois
        janela['texto'].update(f"Usando a Ordenação com a função Sort() do PYTHON, o tempo total de execução do programa com 100 foi de: {delta:.20f}")

    if eventos == 'Sort' and qntd_num == 'mil': # Caso 4.2 - Ordenação pela Função Sort - Lista de 1000 números
        start = float(time.time()) #2 - Inicia a contagem do tempo
        w1000 = lista_copia_1000.sort() #Chama a função de ordenação com o Sort() para 1000 números
        #end = float(time.time()) #2 - Finaliza a contagem do tempo
        time.sleep(0.000000000000002)
        delta = time.time() - start #Calcula o tempo de execução total do código
        lista_tempo1000.append(delta) #Salvando todos os valores de tempo em uma única lista para comparar depois
        janela['texto'].update(f"Usando a Ordenação com a função Sort() do PYTHON, o tempo total de execução do programa com 1000 foi de: {delta:.20f}")

    if eventos == 'Sort' and qntd_num == '10mil': # Caso 4.3 - Ordenação pela Função Sort - Lista de 10 mil números
        start = float(time.time()) #2 - Inicia a contagem do tempo
        w10k = lista_copia_10k.sort() #Chama a função de ordenação com o Sort() para 10k números
        #end = float(time.time()) #2 - Finaliza a contagem do tempo
        time.sleep(0.000000000000002)
        delta = time.time() - start #Calcula o tempo de execução total do código
        lista_tempo10k.append(delta) #Salvando todos os valores de tempo em uma única lista para comparar depois
        janela['texto'].update(f"Usando a Ordenação com a função Sort() do PYTHON, o tempo total de execução do programa com 10000 foi de: {delta:.20f}")


    if qntd_num == '': # Caso 5 - Nenhuma lista é inserida... apenas é executado uma ordenação!
        janela['texto'].update('Insira um valor válido ; - ;')
