import random


###############################################################################
#                                   Suporte                                   #
##############################################################################+


def distancia_entre_dois_pontos(a, b):
    """Computa a distância Euclidiana entre dois pontos em R^2.
    
    Args:
      a: lista contendo as coordenadas x e y de um ponto.
      b: lista contendo as coordenadas x e y de um ponto.
      
    Returns:
      Distância entre as coordenadas dos pontos `a` e `b`.
    """

    x1 = a[0]
    x2 = b[0]
    y1 = a[1]
    y2 = b[1]

    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)

    return dist


def cria_cidades(n):
    """Cria um dicionário aleatório de cidades com suas posições (x,y).
    
    Args:
      n: inteiro positivo
        Número de cidades que serão visitadas pelo caixeiro.
        
    Returns:
      Dicionário contendo o nome das cidades como chaves e a coordenada no plano
      cartesiano das cidades como valores.
    """

    cidades = {}

    for i in range(n):
        cidades[f"Cidade {i}"] = (random.random(), random.random())
        # cria cidades chamadas de i
        # random.random() sorteia uma float aleatória entre 0 e 1 para as coordenadas

    return cidades


def computa_mochila(individuo, objetos, ordem_dos_nomes):
    """Computa o valor total e peso total de uma mochila.
    
    Args:
      individuo:
        Lista binária contendo a informação de quais objetos serão selecionados.
        
      objetos:
        Dicionário onde as chaves são os nomes dos objetos e os valores são
        dicionários com a informação do peso e valor.
        
      ordem_dos_nomes:
        Lista contendo a ordem dos nomes dos objetos.
        
    Returns:
      valor_total: valor total dos itens da mochila em unidades de dinheiros.
      peso_total: peso total dos itens da mochila em unidades de massa.
    """
    
    valor_total = 0
    peso_total = 0
    
    for pegou_o_item_ou_nao, nome_do_item in zip(individuo, ordem_dos_nomes):
    # associou 1 (pega) e 0 (não pega) de individuos com os correspondentes nomes dos itens
        if pegou_o_item_ou_nao == 1:
            valor_do_item = objetos[nome_do_item]["valor"]
            peso_do_item = objetos[nome_do_item]["peso"]
            
            valor_total = valor_total + valor_do_item
            peso_total = peso_total + peso_do_item

    return valor_total, peso_total


###############################################################################
#                                    Genes                                    #
###############################################################################


def gene_cb():
    """Gera um gene válido para o problema das caixas binárias.
    
    Returns:
      Um valor zero ou um.
    """
    lista = [0,1] # Cria uma com os elementos 0 e 1
    gene = random.choice(lista) # Sorteia, aleatoriamente, um dos elementos 
                                # dessa lista e armazena como varável gene
        
    return gene # Retorna o gene


def gene_cnb(valor_max_caixa):
    """Gera um gene válido para o problema das caixas não-binárias.
    
    Args:
      valor_max_caixa: Valor máximo que a caixa pode assumir
      
    Returns:
      Um valor de 0 a 'valor_max_caixa' (incluso)
    """
    gene = random.randint(0, valor_max_caixa)
    return gene


def gene_letra(letras):
    """Sorteia uma letra.
    
    Args:
      letras: letras possíveis de serem sorteadas.
      
    Returns: 
      Retorna uma letra dentro das possíveis de serem sorteadas.
    """
    
    letra = random.choice(letras) # sorteia uma letra aleatória dentre as disponíveis
    
    return letra


###############################################################################
#                                  Indivíduos                                 #
###############################################################################


def individuo_cb(n):
    """Gera um indivíduo para o problema das caixas binárias.
    
    Args:
      n: número de genes do indivíduo.
    
    Returns:
      Uma lista com n genes. Cada gene é um valor zero ou um.
    """
    individuo = [] # Cria uma lista que vai representar o indivíduo
    for i in range(n): # Itera até atingir a quantidade de genes do indivíduo
        gene = gene_cb() # Cria um gene
        individuo.append(gene) # Adiciona o gene ao indivíduo
        
    return individuo # Retorna o indivíduo formado


def individuo_cnb(numero_genes, valor_max_caixa):
    """Gera um indivíduo válido para o problemas das caixas não binárias.
    
    Args:
      numero_genes: número de genes na lista que representa o indivíduo.
      valor_max_caixa: Valor máximo que a caixa pode assumir.
      
    Returns:
      Uma lista que representa um indivíduo válido para o problema das CNB.
    """
    individuo = []
    for _ in range(numero_genes): # _ permite iterar sem precisar criar outra variável,
                                  # já que aqui não será usado 
        gene = gene_cnb(valor_max_caixa)
        individuo.append(gene)
        
    return individuo


def individuo_senha(tamanho_senha, letras):
    """Cria um candidato para o problema da senha.
    
    Args:
      tamanho_senha: inteiro representando o tamanho da senha.
      letras: letras possíveis de serem sorteadas.
      
    Returns:
      Lista com n letras.
    """
    candidato = []
    
    for n in range(tamanho_senha):
        candidato.append(gene_letra(letras))
        
    return candidato


def individuo_cv(cidades):
    """Sorteia um caminho possível no problema do caixeiro viajante.
    
    Args:
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
        
    Returns:
      Retorna uma lista de nomes de cidades formando um caminho onde visitamos
      cada cidade apenas uma vez.
    """
    nomes = list(cidades.keys())
    random.shuffle(nomes) # ordena a lista de nomes
    
    return nomes


def individuo_senha_var(tamanhos_senha, letras):
    """Cria um candidato para o problema da senha de tamanho variável.
    
    Args:
      tamanhos_senha: lista do intervalo de números possíveis de tamanhos da senha.
      letras: letras possíveis de serem sorteadas.
      
    Returns:
      cadidado: lista com n letras, que pode variar de tamanho a cada rodada.
    """
    candidato = []
    tam_senha = random.choice(tamanhos_senha) # sorteia um tamanho possível de
                                              # forma aleatória
    
    for _ in range(tam_senha):
        candidato.append(gene_letra(letras))
        
    return candidato


###############################################################################
#                                  População                                  #
###############################################################################

    
def populacao_cb(tamanho, n):
    """Cria uma população no problema das caixas binárias.
    
    Args:
      tamanho: tamanho da população
      n: número de genes de um indivíduo.
    
    Returns:
      Uma lista onde cada item é um indivídio. Um indivíduo é uma lista com n genes.
    """
    
    populacao = [] # Cria uma lista que conterá a população de indivíduos
    for _ in range(tamanho): # Itera para o tamanho da população (número de 
                             # indíviduos que contemplará)
        populacao.append(individuo_cb(n)) # Adiciona o indivíduo, com a quantidade
                                          # de genes estibulada, na populaçao
            
    return populacao # Retorna a população formada


def populacao_cnb(tamanho_populacao, numero_genes, valor_max_caixa):
    """Cria uma população de indivíduos para o problema das caixaas não-binárias.
    
    Args:
      tamanho_populacao: número de indivíduos da população
      numero_genes: número de genes do indivíduo
      valor_max_caixa: valor máximo que a caixa pode assumir
      
    Returns:
      Uma lista onde cada item representa um indivíduo.
    """
    populacao = [] 
    for _ in range(tamanho_populacao):
        individuo = individuo_cnb(numero_genes, valor_max_caixa)
        populacao.append(individuo)
        
    return populacao


def populacao_inicial_senha(tamanho, tamanho_senha, letras):
    """Cria população inicial no problema da senha.
    
    Args:
      tamanho: tamanho da população.
      tamanho_senha: inteiro representando o tamanho da senha.
      letras: letras possíveis de serem sorteadas.
      
    Returns:
      Lista com todos os indivíduos da população no problema da senha.
    """
    populacao = []
    for n in range(tamanho):
        populacao.append(individuo_senha(tamanho_senha, letras))
        
    return populacao


def populacao_inicial_cv(tamanho, cidades):
    """Cria população inicial no problema do caixeiro viajante.
    
    Args:
      tamanho:
        Tamanho da população.
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
        
    Returns:
      Lista com todos os indivíduos da população no problema do caixeiro
      viajante.
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_cv(cidades))
        
    return populacao


def populacao_inicial_senha_var(tamanho_pop, tamanhos_senha, letras):
    """Cria população inicial no problema da senha de tamanho variável.
    
    Args:
      tamanho_pop: tamanho da população (quantidade de indivíduos dela).
      tamanhos_senha: lista do intervalo de números possíveis de tamanhos da senha.
      letras: letras possíveis de serem sorteadas.
      
    Returns:
      populacao: lista com todos os indivíduos da população no problema da senha
      de tamanho variável.
    """
    populacao = []
    for _ in range(tamanho_pop):
        populacao.append(individuo_senha_var(tamanhos_senha, letras))
        
    return populacao


###############################################################################
#                                   Seleção                                   #
###############################################################################


def selecao_roleta_max(populacao, fitness):
    """Seleciona indivíduos de uma população usando o método da roleta.
    
    Nota: apenas funciona para problemas de maximização.
    
    Args:
      populacao: lista com todos os indivíduos da população.
      fitness: lista com o valor da funcao objetivo dos indivíduos da população.
    
    Returns:
      População dos indivíduos selecionados.
    """
    populacao_selecionada = random.choices(populacao, weights=fitness, k=len(populacao))
    # escolhe indivíduos de forma que leva o fitness em consideração
    
    return populacao_selecionada


def selecao_torneio_min(populacao, fitness, tamanho_torneio=3):
    """Faz a seleção de uma população usando torneio.
    
    Nota: da forma que está implementada, só funciona em problemas de
    minimização.
    
    Args:
      populacao: população do problema.
      fitness: lista com os valores de fitness dos indivíduos da população.
      tamanho_torneio: quantidade de invidiuos que batalham entre si.
      
    Returns:
      Indivíduos selecionados. Lista com os individuos selecionados com mesmo
      tamanho do argumento `populacao`.
    """
    selecionados = []

    # criamos essa variável para associar cada individuo com seu valor de fitness
    par_populacao_fitness = list(zip(populacao, fitness))

    # vamos fazer len(populacao) torneios! Que comecem os jogos!
    for _ in range(len(populacao)):
        combatentes = random.sample(par_populacao_fitness, tamanho_torneio)

        # é assim que se escreve infinito em python
        minimo_fitness = float("inf")

        for par_individuo_fitness in combatentes:
            individuo = par_individuo_fitness[0]
            fit = par_individuo_fitness[1]

            # queremos o individuo de menor fitness
            if fit < minimo_fitness:
                selecionado = individuo
                minimo_fitness = fit

        selecionados.append(selecionado)

    return selecionados


###############################################################################
#                                  Cruzamento                                 #
###############################################################################


def cruzamento_ponto_simples(pai, mae):
    """Operador de cruzamento de ponto simples.
    
    Args:
      pai: uma lista representando um indivíduo.
      mae: uma lista representando um indivíduo.
      
    Returns:
      Duas listas, sendo que cada uma representa um filho dos pais que foram os argumentos.
    """
    ponto_de_corte = random.randint(1, len(pai) - 1) # Sorteia, de forma aleatoria,
                                                     # um local possível para ser 
                                                     # o ponto de corte, e armaneza-o
    
    # Definindo o filho1 e filho2 como parte do pai e da mãe, de acordo com o
    # ponto de corte estabelecido.
    filho1 = pai[:ponto_de_corte] + mae[ponto_de_corte:]
    filho2 = mae[:ponto_de_corte] + pai[ponto_de_corte:]
    
    return filho1, filho2 # Retorna filho1 e filho2


def cruzamento_ordenado(pai, mae):
    """Operador de cruzamento ordenado.
    Neste cruzamento, os filhos mantém os mesmos genes que seus pais tinham,
    porém em uma outra ordem. Trata-se de um tipo de cruzamento útil para
    problemas onde a ordem dos genes é importante e não podemos alterar os genes
    em si. É um cruzamento que pode ser usado no problema do caixeiro viajante.
    Ver pág. 37 do livro do Wirsansky.
    
    Args:
      pai: uma lista representando um indivíduo.
      mae : uma lista representando um indivíduo.
      
    Returns:
      Duas listas, sendo que cada uma representa um filho dos pais que foram os
      argumentos. Estas listas mantém os genes originais dos pais, porém altera
      a ordem deles.
    """
    corte1 = random.randint(0, len(pai) - 2)
    corte2 = random.randint(corte1 + 1 , len(pai) - 1)
    
    filho1 = pai[corte1:corte2]
    for gene in mae:
        if gene not in filho1:
            filho1.append(gene)
            
    filho2 = mae[corte1:corte2]
    for gene in pai:
        if gene not in filho2:
            filho2.append(gene)
            
    return filho1, filho2


def cruzamento_ponto_simples_senha_var(pai, mae):
    """Operador de cruzamento de ponto simples para pai e mãe podendo ter tamanhos
    diferentes.
    
    Args:
      pai: uma lista representando um indivíduo.
      mae: uma lista representando um indivíduo.
      
    Returns:
      Duas listas, sendo que cada uma representa um filho dos pais que foram os argumentos.
    """
    tam_pais = []
    tam_pai = len(pai)
    tam_pais.append(tam_pai)
    tam_mae = len(mae)
    tam_pais.append(tam_mae)
    tam_menor_progenitor = min(tam_pais) # encontra o tamanho do menor progenitor
    ponto_de_corte = random.randint(1, tam_menor_progenitor - 1) # Sorteia, de forma aleatoria,
                                                                 # um local possível para ser 
                                                                 # o ponto de corte, e armaneza-o
    
    # Definindo o filho1 e filho2 como parte do pai e da mãe, de acordo com o
    # ponto de corte estabelecido.
    filho1 = pai[:ponto_de_corte] + mae[ponto_de_corte:]
    filho2 = mae[:ponto_de_corte] + pai[ponto_de_corte:]
    
    return filho1, filho2 # Retorna filho1 e filho2


###############################################################################
#                                   Mutação                                   #
###############################################################################


def mutacao_cb(individuo):
    """Realiza a mutação de um gene no problema das caixas binárias.
    
    Args: 
      individuo: uma lista representando um indivíduo no problema das caixas binárias.
      
    Return:
      Um indivíduo com um gene mutado.
    """
    gene_a_ser_mutado = random.randint(0, len(individuo) - 1) # Sorteia o gene
                                                              # a ser mutado
    individuo[gene_a_ser_mutado] = gene_cb() # Substitui-o por um novo gene criado
    
    return individuo # Retorna o indivíduo mutado


def mutacao_cnb(individuo, valor_max_caixa):
    """Realiza a mutação do indivíduo.
    
    Args:
      individuo: indivíduo que deve sofrer a mutação.
      valor_max_caixa: valor máximo que a caixa pode assumir.
      
    Returns:
      Indivíduo que sofreu a mutação.
    """
    gene_a_ser_mutado = random.randint(0, len(individuo) - 1)
    individuo[gene_a_ser_mutado] = gene_cnb(valor_max_caixa)
    
    return individuo


def mutacao_senha(individuo, letras):
    """Realiza a mutação de um gene no problema da senha.
    
    Args:
      individuo: uma lista representado um indivíduo no problema da senha.
      letras: letras possíveis de serem sorteadas.
      
    Returns:
      Um indivíduo (senha) com um gene mutado.
    """
    gene = random.randint(0, len(individuo) - 1)
    individuo[gene] = gene_letra(letras)
    
    return individuo


def mutacao_de_troca(individuo):
    """Troca o valor de dois genes.
    
    Args:
      individuo: uma lista representado um indivíduo.
      
    Returns:
      O indivíduo recebido como argumento, porém com dois dos seus genes
      trocados de posição.
    """
    
    indices = list(range(len(individuo)))
    lista_sorteada = random.sample(indices, k=2)
    indice1 = lista_sorteada[0]
    indice2 = lista_sorteada[1]
    
    individuo[indice1], individuo[indice2] = individuo[indice2], individuo[indice1]
    
    return individuo


def mutacao_tam_senha_var(individuo, tamanhos_senha, letras):
    """Altera o tamanho da senha no problema da senha de tamanho variável.
    
    Args:
      individuo: uma lista representado um indivíduo no problema da senha de tamanho variável.
      tamanhos_senha: lista do intervalo de números possíveis de tamanhos da senha.
      letras: letras possíveis de serem sorteadas.
      
    Returns:
      Um indivíduo (senha) com tamanho alterado.
    """
    tam_novo_senha = random.choice(tamanhos_senha)
    
    if tam_novo_senha < len(individuo):
        individuo = individuo[:(tam_novo_senha - 1)] # indivíduo novo será o original,
                                                     # desde o início até o de index
                                                     # de comprimento-1
    elif tam_novo_senha > len(individuo):
        for _ in range(tam_novo_senha - len(individuo)): # para cada unidade que o 
                                                         # tamanho novo é maior
            individuo.append(gene_letra(letras))
    
    # caso tam_novo_senha == len(individuo), nada acontecerá e é retornado, portanto,
    # o mesmo indivíduo
    
    return individuo

###############################################################################
#                         Função objetivo - indivíduos                        #
###############################################################################


def funcao_objetivo_cb(individuo):
    """Computa a função objetivo no problema das caixas binárias.
    
    Args:
      individuo: lista contendo os genes das caixas binárias.
    
    Return:
      Um valor representando a soma dos genes do indivíduo.
    """
    return sum(individuo) + 1 # Retorna a soma dos genes de um indivíduo

    # Nota: adiciona-se 1, para que, quando usada a seleção por roleta máxima,
    # o indivíduo de genes todos 0 ainda possa ter alguma chance.


def funcao_objetivo_cnb(individuo):
    """Calcula o fitness do indivíduo para o problema das caixas não-binárias.
    
    Args:
      individuo: lista que representa um indivíduo dentro do problema das CNB.
      
    Returns:
      Um valor que representa o fitness do indivíduo.
    """
    fitness = sum(individuo)
    
    return fitness


def funcao_objetivo_senha(individuo, senha_verdadeira):
    """Computa a funcao objetivo de um indivíduo no problema da senha
    
    Args:
      indivíduo: lista contendo as letras da senha
      senha_verdadeira: a senha que você está tentando descobrir
      
    Returns:
      A "distância" entre a senha proposta e a senha verdadeira. Essa distância 
      é medida letra por letra. Quanto mais distante uma letra for da que 
      deveria ser, maior é essa distância.
    """
    
    diferenca = 0
    
    for letra_candidato, letra_oficial in zip(individuo, senha_verdadeira):
        diferenca = diferenca + abs(ord(letra_candidato) - ord(letra_oficial))
        
    return diferenca


def funcao_objetivo_cv(individuo, cidades):
    """Computa a funcao objetivo de um individuo no problema do caixeiro viajante.
    
    Args:
      individiuo:
        Lista contendo a ordem das cidades que serão visitadas
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
        
    Returns:
      A distância percorrida pelo caixeiro seguindo o caminho contido no
      `individuo`. Lembrando que após percorrer todas as cidades em ordem, o
      caixeiro retorna para a cidade original de onde começou sua viagem.
    """

    distancia = 0

    for posicao in range(len(individuo) - 1):
        
        partida = cidades[individuo[posicao]]
        chegada = cidades[individuo[posicao + 1]]
        
        percurso = distancia_entre_dois_pontos(partida, chegada)
        distancia = distancia + percurso
        
    # Calculando o caminho de volta para a cidade inicial
    partida = cidades[individuo[-1]]
    chegada = cidades[individuo[0]]
    
    percurso = distancia_entre_dois_pontos(partida, chegada)
    distancia = distancia + percurso

    return distancia


def funcao_objetivo_mochila(individuo, objetos, limite, ordem_dos_nomes):
    """Computa a funcao objetivo de um candidato no problema da mochila.
    
    Args:
      individiuo:
        Lista binária contendo a informação de quais objetos serão selecionados.
      objetos:
        Dicionário onde as chaves são os nomes dos objetos e os valores são
        dicionários com a informação do peso e valor.
      limite:
        Número indicando o limite de peso que a mochila aguenta.
      ordem_dos_nomes:
        Lista contendo a ordem dos nomes dos objetos.
        
    Returns:
      Valor total dos itens inseridos na mochila considerando a penalidade para
      quando o peso excede o limite.
    """

    valor_mochila, peso_mochila = computa_mochila(individuo, objetos, ordem_dos_nomes)
    
    if peso_mochila > limite:
        valor_mochila = 0.01
        
    return valor_mochila


def funcao_objetivo_senha_var(individuo, senha_verdadeira, penalidade):
    """Computa a funcao objetivo de um indivíduo no problema da senha de tamanho
    variável e a penaliza, caso erre o tamanho.
    
    Args:
      individuo: lista contendo as letras da senha.
      senha_verdadeira: a senha que você está tentando descobrir.
      penalidade: valor da penalidade aplicada a cada unidade de tamanho do individuo
      distante do da senha_verdadeira.
      
    Returns:
      A "distância" entre a senha proposta e a senha verdadeira. Essa distância 
      é medida letra por letra. Quanto mais distante uma letra for da que 
      deveria ser, maior é essa distância.
    """
    
    diferenca = 0
    
    for letra_candidato, letra_oficial in zip(individuo, senha_verdadeira): # zip respeita o de menor tamanho
        diferenca = diferenca + abs(ord(letra_candidato) - ord(letra_oficial))
        
    dif_tam = abs(len(individuo) - len(senha_verdadeira)) # calcula o módulo da
                                                          # diferença de tamanho
    if dif_tam != 0: # caso haja diferença de tamanho
        diferenca = diferenca + (dif_tam * penalidade) # aplica-se a penalidade 
                                                       # no que se retornará de 
                                                       # função objetivo (obs:
                                                       # soma-se por ser problema
                                                       # de minimização)
        
    return diferenca


###############################################################################
#                         Função objetivo - população                         #
###############################################################################


def funcao_objetivo_pop_cb(populacao):
    """Calcula a funcao objetivo para todos os membros de uma população.
    
    Args:
      populacao: lista com todos os indivíduos da população.
    
    Returns:
      Lista de valores representando a fitness de cada indivíduo de uma população.
    """
    fitness = [] # Cria uma lista para armazenar as fitness
    for individuo in populacao: # Itera para cada indivíduo dentro da população
        fobj = funcao_objetivo_cb(individuo) # Calcula e armazena a função 
                                             # objetivo (soma dos genes) para um 
                                             # indivíduo
        fitness.append(fobj) # Adiciona a função objetivo calculada na lista de
                             # fitnesss
            
    return fitness # Retorna a lista de fitness


def funcao_objetivo_pop_cnb(populacao):
    """Calcula o fitness da população completa.
    
    Args:
      populacao: lista com todos os indivíduos da população.
      
    Returns:
      Uma lista com o fitness de cada indivíduo em ordem.
    """
    fitness_pop = []
    for individuo in populacao:
        fitness_ind = funcao_objetivo_cnb(individuo)
        fitness_pop.append(fitness_ind)
        
    return fitness_pop


def funcao_objetivo_pop_senha(populacao, senha_verdadeira):
    """Computa a funcao objetivo de uma populaçao no problema da senha.
    
    Args:
      populacao: lista com todos os individuos da população.
      senha_verdadeira: a senha que você está tentando descobrir.
      
    Returns:
      Lista contendo os valores da métrica de distância entre senhas.
    """
    resultado = []

    for individuo in populacao:
        resultado.append(funcao_objetivo_senha(individuo, senha_verdadeira))

    return resultado


def funcao_objetivo_pop_cv(populacao, cidades):
    """Computa a funcao objetivo de uma população no problema do caixeiro viajante.
    
    Args:
      populacao:
        Lista com todos os inviduos da população.
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
        
    Returns:
      Lista contendo a distância percorrida pelo caixeiro para todos os
      indivíduos da população.
    """

    resultado = []
    for individuo in populacao:
        resultado.append(funcao_objetivo_cv(individuo, cidades))

    return resultado


def funcao_objetivo_pop_mochila(populacao, objetos, limite, ordem_dos_nomes):
    """Computa a função objetivo de uma populacao no problema da mochila.
    
    Args:
      populacao:
        Lista com todos os individuos da população
      objetos:
        Dicionário onde as chaves são os nomes dos objetos e os valores são
        dicionários com a informação do peso e valor.
      limite:
        Número indicando o limite de peso que a mochila aguenta.
      ordem_dos_nomes:
        Lista contendo a ordem dos nomes dos objetos.
        
    Returns:
      Lista contendo o valor dos itens da mochila de cada indivíduo.
    """

    resultado = []
    for individuo in populacao:
        resultado.append(
            funcao_objetivo_mochila(
                individuo, objetos, limite, ordem_dos_nomes
            )
        )

    return resultado


def funcao_objetivo_pop_senha_var(populacao, senha_verdadeira, penalidade):
    """Computa a funcao objetivo de uma populaçao no problema da senha.
    
    Args:
      populacao: lista com todos os individuos da população
      senha_verdadeira: a senha que você está tentando descobrir
      penalidade: valor da penalidade aplicada a cada unidade de tamanho do individuo
      distante do da senha_verdadeira.
      
    Returns:
      Lista contendo os valores da métrica de distância entre senhas.
    """
    resultado = []

    for individuo in populacao:
        resultado.append(funcao_objetivo_senha_var(individuo, senha_verdadeira, penalidade))

    return resultado