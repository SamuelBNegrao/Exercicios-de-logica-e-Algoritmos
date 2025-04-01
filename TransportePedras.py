'''Transporte de pedras: Tomando N pedras onde cada uma tem peso 1kg maior que a anterior (pedra1=1kg, pedra2=2kg, pedra3=3kg, ..., pedraN=Nkg),
determine a forma de transportá-las em um veículo com capacidade máxima de C (kg) por vez com o mínimo de deslocamentos.
A solução para este problema deve ser implementada com a estratégia gulosa.
Algoritmo: 
1- Solicitar dados do usuário
2- Verificar se o caminhão é capaz de carregar a maior pedra. Se for muito pesado, o programa pede pedras mais leves
3- Criar uma lista com todas as pedras em ordem crescente 
4- SOmar o peso de todas as pedras, caso esse peso for menor que a capacidade de carga do caminhão, encerrar programa
5- Caso contrário, pegar a pedra mais pesada e a mais leve, se possível pegar mais mais uma leve e colocar no caminhão
6- Percorrer a lista até que todas as pedras sejam transportadas e somar cada interação, resultando no número total de transportes 
'''
muito_pesado = False
lista_Pedras = []
qtd_deslocamentos, soma, i  = 0, 0, 1
kg_caminhao = int(input("Digite quantos Kg o caminhão aguenta carregar: "))
qtd_Pedras = int(input("Insira a quantidade de pedras que deseja transportar: "))

#Verifica se o caminhão é capaz de transportar as pedras 
if qtd_Pedras > kg_caminhao:
    print("O caminhão não suporta essa quantidade de peso, diminua o peso das pedras!!!")
    muito_pesado = True
    while muito_pesado ==  True:
        qtd_Pedras = int(input("Insira pedras com pesos menores dessa vez: "))
        if qtd_Pedras <= kg_caminhao:
            muito_pesado = False

#Cria a lista com todas as pedras
while i <= qtd_Pedras:
    lista_Pedras.append(i)
    i += 1
#Soma o peso de cada uma das pedras em uma variável
for num in lista_Pedras:
    soma += num
if soma <= kg_caminhao:
    qtd_deslocamentos += 1
    print("Legal! Você consegue transportar todas as pedras em apenas uma viagem!")
#Faz a contagem de peso de cada pedra e verifica se é possível o transporte
else:
    leve, pesada, soma_pedras = 0, len(lista_Pedras) - 1, 0
while leve <= pesada:
    carga_atual = lista_Pedras[pesada]
    pesada -= 1
    if leve <= pesada and carga_atual + lista_Pedras[leve] <= kg_caminhao:
        carga_atual += lista_Pedras[leve]
        leve += 1
    if leve <= pesada and carga_atual + lista_Pedras[leve] <= kg_caminhao:
        carga_atual += lista_Pedras[leve]
        leve += 1 

    qtd_deslocamentos += 1 

print(f'Serão necessárias {qtd_deslocamentos} viagens para transportar todas as pedras.')