from matplotlib import pyplot as plt

#-Exemplo 1--Grafico em Linha------------------------------------------------------
# years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
# gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# # cria um gráfico de linha, anos no eixo x, gdp no eixo y
# plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

# # adiciona título
# plt.title('GDP Nominal')

# # adiciona um selo no eixo y
# plt.ylabel('Bilhões de R$')
# plt.show()

#-Exemplo 2--Grafico em Barra------------------------------------------------------
# movies = ['LOTR - Trilogy', 'Star Wars', 'Robocop', 'Gladiator', 'Predator', 'Rambo']
# num_oscars = [11, 6, 1, 3, 1, 1]

# # barras possuem o tamanho padrão de 0.8, então adicionaremos 0.1 as
# # coordenadas a esquerda para que cada barra seja centralizada
# xs = [i + 0.1 for i, _ in enumerate(movies)]

# # as barras do grafico com as coordenadas x a esquerda [xs], alturas [num_oscars]
# plt.bar(xs, num_oscars)

# plt.ylabel('# de Premiações')
# plt.title('Meus Filmes Favoritos')

# # nomeia o eixo x com nomes de filmes na barra central
# # 0.09 é somado ao i, para centralizar junto com a barra
# plt.xticks([i + 0.09 for i, _ in enumerate(movies)], movies)
# plt.show()

#-Exemplo 3--Grafico em Barra------------------------------------------------------
# from collections import Counter

# grades = [83,95,91,87,70,0,85,82,100,67,73,77,0]
# decile = lambda grade: grade // 10 * 10
# histogram = Counter(decile(grade) for grade in grades)

# # da para cada barra sua altura correta
# # da para cada barra a largura de 8
# plt.bar([x for x in histogram.keys()], histogram.values(), 8)

# # eixo x de -5 ate 105
# # eixo y de 0 ate 5
# plt.axis([-5, 105, 0, 5])

# # rotulos do eixo x em 0, 10, ..., 100
# plt.xticks([10 * i for i in range(11)])
# plt.xlabel('Decil')
# plt.ylabel('# de Alunos')
# plt.title('Distribuição das Notas do Teste 1')
# plt.show()

#-Exemplo 4--Grafico em Barra------------------------------------------------------
# from collections import Counter

# mentions = [500, 505]
# years = [2013, 2014]

# plt.bar([2013, 2014], mentions, 0.8)
# plt.xticks(years)
# plt.ylabel('# de vezes que ouvimos alguem dizer datascience')

# # se não fizer isso, matplotlib nomeará o eixo x de 0, 1
# # e então adiciona a +2.013e3 para fora do canto (ficando paia)
# plt.ticklabel_format(useOffset=False)

# # enganar o eixo y mostra apenas a parte aicma de 500
# # plt.axis([2012.5, 2014.5, 499, 506])
# # plt.title('Olhe o grande aumento')
# plt.axis([2012.5,2014.5,0,550])
# plt.title('Não tão grande assim')
# plt.show()

#-Exemplo 5--Grafico em Linha------------------------------------------------------
variance = [1,2,4,8,16,32,64,128,256]
bias_squared = [256,128,64,32,16,8,4,2,1]
total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]

# podemos fazer multiplas chamadas paraplt.plot
# para mostrar multiplas series no mesmo grafico
plt.plot(xs, variance, 'g-', label='variance')          # linha verde solida
plt.plot(xs, bias_squared, c='r', ls='-.', label='bias^2')        # linha com ponto tracejado vermelho
plt.plot(xs, total_error, 'b:', label='total error')    # linha com pontilhado azul

# como atribuimos rotulos(label) para cada um
# podemos inserir uma legenda
# loc=9 significa 'top center'
plt.legend(loc=9)
plt.xlabel('complexidade do modelo')
plt.title('Compromisso entre Polarização e Variância')
plt.show()
