# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
# https://stackoverflow.com/questions/21572175/convert-csv-file-to-list-of-dictionaries/21572244
with open("chicago.csv", "r") as file_read:
    data_list = [{k: v for k, v in row.items()}
                 for row in csv.DictReader(file_read)]
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

for i in range(0, 20):
    print(data_list[i])

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")


for i in range(0, 20):
    print(data_list[i])

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem


def column_to_list(data, index):
    """
        Faz uma lista a partir de uma conluna usando como parametro
        Parametros:
         -Data: Lista de dicionarios
         -Index: A posição da coluna
        Retorna:
        -column_list: Lista de colunas
    """
    column_list = []
    listaDeColunas = list(data[0].keys())
    for element in data:
        column_list.append(element[listaDeColunas[index]])
    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])
# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)
            ) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)
           ) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(
    data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função parTODO isso.

female = 0
male = 0
unknown = 0

for row in data_list:
    if(row['Gender'] == 'Male'):
        male += 1
    elif(row['Gender'] == 'Female'):
        female += 1
    else:
        unknown += 1
# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função parTODO isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)


def groupBy(data, index):
    """
        Função que agrupa uma coluna do dicionario e conta suas ocorrencias
        em um dicionario tendo:
        Parametros:
         -Data: Um dicionario daonde ele deve agrupar.
         -Index: A posição da key que ele deve agrupar por.
        Retorna:
         -group: Dicionario com campo:count
    """
    lista = column_to_list(data, index)
    group = {}
    elements = list(set(lista))
    for element in elements:
        group[element] = 0
    for item in lista:
        group[item] += 1
    return group


def count_gender(data_list):
    """
        Conta os generos do dicionario
        Parametros:
         -data_list: lista de dados daonde ele deve contar
        Retorna:
         -Lista: [Masculino, Feminino]
    """
    group = groupBy(data_list, -2)
    male = group['Male']
    female = group['Female']
    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)
            ) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)
           ) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[
    1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.


def most_popular_gender(data):
    """
        Conta o Genero mais popular do dicionario
        Parametros:
         -data: Dicionario aonde deve contar
        Retorna:
         -answer: String contendo o genero mais popular
    """
    genders = groupBy(data, -2)
    answer = max(genders, key=genders.get)
    if(genders[answer] == (len(data)/2)):
        answer = 'Igual'
    if(answer == 'Male'):
        answer = 'Masculino'
    elif(answer == 'Female'):
        answer = 'Feminino'
    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)
            ) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(
    data_list) == "Masculino", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
# Se tudo está rodando como esperado, verifique este gráfico!
user_type_list = column_to_list(data_list, -3)
types = ["Subscriber", "Customer", "Dependent"]
groups = groupBy(data_list, -3)
quantity = [groups['Subscriber'], groups['Customer'], groups['Dependent']]
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipo')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipo de Usuário')
plt.show(block=True)
print("\nTAREFA 7: Verifique o gráfico!")


input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Porque temos generos vazios :( qtde de generos vazios: {}".format(
    groupBy(data_list, -2)[''])
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas parTODO isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)
print(trip_duration_list[:20])


def myMin(numbers):
    """
        Equivalente ao min()
        Parametros:
         -numbers: Lista do que deve pegar o minimo
        Retorna:
         -mini: o minimo da lista
    """
    mini = float(numbers[0])
    for i in numbers:
        i = float(i)
        if i < mini:
            mini = i
    return mini


def myMax(numbers):
    """
        Equivalente ao max()
        Parametros:
         -numbers: Lista do que deve pegar o maximo
        Retorna:
         -biggest: o maximo da lista
    """
    biggest = float(numbers[0])
    for i in numbers:
        i = float(i)
        if i > biggest:
            biggest = i
    return biggest


def mySum(numbers):
    """
        Equivalente ao sum()
        Parametros:
         -numbers: Lista do que deve somar
        Retorna:
         -theSum: A soma da lista
    """
    theSum = 0
    for number in numbers:
        number = int(number)
        theSum += number
    return theSum


def myLen(theList):
    """
        Equivalente ao len()
        Parametros:
         -theList: Lista do que deve contar
        Retorna:
         -lenght: tamanho da lista
    """
    lenght = 0
    for _ in theList:
        lenght += 1
    return lenght


def mean(numbers):
    """
        Tira a média da lista
        Parametros:
         -numbers: Lista do que deve pegar a média
        Retorna:
         -mean: a média da lista 
    """
    return mySum(numbers)/myLen(numbers)


def median(theList):
    """
        Tira a mediana da lista
        Parametros:
         -numbers: Lista do que deve pegar a mediana
        Retorna:
         -median: a mediana da lista 
    """
    numbers = list()
    for i in theList:
        numbers.append(int(i))
    numbers.sort()
    if(myLen(numbers) % 2 == 0):
        return (numbers[myLen(numbers) // 2] + numbers[(myLen(numbers)//2) + 1]) / 2
    else:
        return numbers[(myLen(numbers) // 2) + 1]


min_trip = myMin(trip_duration_list)
max_trip = myMax(trip_duration_list)
mean_trip = mean(trip_duration_list)
median_trip = median(trip_duration_list)


print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")


print("Min: ", min_trip, "Max: ", max_trip,
      "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
start_stations = set(groupBy(data_list, 3))

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(
    start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documenteou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:


def new_function(param1: int, param2: str) -> list:
    """
    Função de exemplo com anotações.
    Argumentos:
        param1: O primeiro parâmetro.
        param2: O segundo parâmetro.
    Retorna:
        Uma lista de valores x.

    """


input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

# Eu meio que já tinha feito isso com o groupBy


def count_items(column_list):
    """
        Conta itens repetidos em uma lista.
        Parametros:
         -column_list: Uma lista daonde ele deve contar
        Retorna:
         -item_types: Tipo dos itens
         -counts: Quantidade de repetições
    """

    item_types = list(set(column_list))
    counts = []
    for _ in item_types:
        counts.append(0)

    for index, value in enumerate(item_types):
        for column in column_list:
            if(column == value):
                counts[index] += 1
    return item_types, counts


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 11: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"
    # -----------------------------------------------------
