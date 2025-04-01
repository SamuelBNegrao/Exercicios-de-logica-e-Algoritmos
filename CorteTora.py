'''Considere uma tora de madeira de comprimento L (m), a qual desejamos cortá-la N vezes em posições determinadas pela lista [p1,p2,p3,...,pN].
Cada corte custa R reais por metro de tora a ser cortada, por exemplo se R=5 e L=10, o valor será R$ 50,00 independente do ponto de corte.
Determine o valor total mínimo para os N cortes.
Algoritmo: 
1- Solicitar dados do usuário
2- Cria uma lista com cada tamanho de corte
3- Percorrer a lista pegando o maior valor e subtraílo do comprimento total da tora 
4- Caso o comprimento da tora ainda for maior que  o próximo corte, realizar o corte
5- Caso contrário, terminar o programa
'''

#Recolhe os dados do usuário
comprimento = int(input("DIgite o comprimento da tora: "))
Ncortes = int(input("DIgite a quantidade de cortes que deseja realizar: "))
valor = float(input("Digite o valor do corte por metro: "))
valor_total = 0
lista =[]
# Cria a lista
for i in range(Ncortes):
    corte_metro = int(input(f"Digite o tamanho do corte {i+1}: "))
    lista.append(corte_metro)

# Realiza os cortes na tora e verifica qual é possível de realizar 
for corte in lista:
    if comprimento >= corte:
        valor_total += corte * valor  
        comprimento -= corte  
        print(f"Corte de {corte} metros realizado.")
    else:
        print(f"Corte de {corte} metros não pode ser realizado. Verificando próximo corte...")

# Exibe o valor total dos cortes e o comprimento restante da tora
print(f'Valor total da compra é de R${valor_total:.2f}')
print(f'Sobraram {comprimento}m da tora')