import random


def gene_cb():
    """Gera um gene válido para o problema das caixas binárias.
    
    Return:
      Um valor zero ou um.
    """
    lista = [0,1]
    gene = random.choice(lista)
    return gene


def gene_cnb(valor_max_caixa):
    """Gera um gene válido para o problema das caixas não-binárias
    
    Args:
      valor_max_caixa: Valor máximo que a caixa pode assumir
      
    Returns:
      Um valor de 0 a 'valor_max_caixa' (incluso)
    """
    gene = random.randint(0, valor_max_caixa)
    return gene
    

def individuo_cb(n):
    """Gera um indivíduo para o problema das caixas binárias.
    
    Args:
      n: número de genes do indivíduo.
    
    Return:
      Uma lista com n genes. Cada gene é um valor zero ou um.
    """
    individuo = []
    for i in range(n):
        gene = gene_cb()
        individuo.append(gene)
    return individuo


def individuo_cnb(numero_genes, valor_max_caixa):
    """Gera um indivíduo válido para o problemas das caixas não binárias
    
    Args:
      numero_genes: número de genes na lista que representa o indivíduo
      valor_max_caixa: Valor máximo que a caixa pode assumir
      
    Returns:
      Uma lista que representa um individuo válido para o problema das CNB
    """
    individuo = []
    for _ in range(numero_genes):
        gene = gene_cnb(valor_max_caixa)
        individuo.append(gene)
    return individuo
    
    
def populacao_cb(tamanho, n):
    """Cria uma população no problema das caixas binárias.
    
    Args:
      tamanho: tamanho da população
      n: número de genes de um indivíduo.
    
    Returns:
      Uma lista onde cada item é um indivídio. Um indivíduo é uma lista com n genes.
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_cb(n))
    return populacao


def populacao_cnb(tamanho_populacao, numero_genes, valor_max_caixa):
    """Cria uma população de indivíduos para o problema das caixaas não-binárias
    
    Args:
      tamanho_populacao: número de indivíduos da população
      numero_genes: número de genes do indivíduo
      valor_max_caixa: valor máximo que a caixa pode assumir
      
    Returns:
      Uma lista onde cada item representa um indivíduo
    """
    populacao = []
    for _ in range(tamanho_populacao):
        individuo = individuo_cnb(numero_genes, valor_max_caixa)
        populacao.append(individuo)
    return populacao


def selecao_roleta_max(populacao, fitness):
    """Seleciona indivíduos de uma população usando o método da roleta.
    
    Nota: apenas funciona para problemas de maximização.
    
    Args:
      populacao: lista com todos os indivíduos da população
      fitness: lista com o valor da funcao objetivo dos individuos da população
    
    Returns:
      População dos indivíduos selecionados.
    """
    populacao_selecionada = random.choices(populacao, weights=fitness, k=len(populacao))
    return populacao_selecionada


def cruzamento_ponto_simples(pai, mae):
    """Operador de cruzamento de ponto simples.
    
    Args:
      pai: uma lista representando um individuo
      mae: uma lista representando um individuo
      
    Returns:
      Duas listas, sendo que cada uma representa um filho dos pais que foram os argumentos.
    """
    ponto_de_corte = random.randint(1, len(pai) - 1)
    
    filho1 = pai[:ponto_de_corte] + mae[ponto_de_corte:]
    filho2 = mae[:ponto_de_corte] + pai[ponto_de_corte:]
    
    return filho1, filho2


def mutacao_cb(individuo):
    """Realiza a mutação de um gene no problema das caixas binárias.
    
    Args: 
      individuo: uma lista representando um indivíduo no problema das caixas binárias
      
    Return:
      Um indivíduo com um gene mutado.
    """
    gene_a_ser_mutado = random.randint(0, len(individuo) - 1)
    individuo[gene_a_ser_mutado] = gene_cb()
    return individuo


def mutacao_cnb(individuo, valor_max_caixa):
    """Realiza a mutação do indivíduo
    
    Args:
      individuo: individuo que deve sofrer a mutação
      valor_max_caixa: valor máximo que a caixa pode assumir
      
    Returns:
      Indivíduo que sofreu a mutação
    """
    gene_a_ser_mutado = random.randint(0, len(individuo) - 1)
    individuo[gene_a_ser_mutado] = gene_cnb(valor_max_caixa)
    return individuo


def funcao_objetivo_cb(individuo):
    """Computa a função objetivo no problema das caixas binárias.
    
    Args:
      individuo: lista contendo os genes das caixas binárias.
    
    Return:
      Um valor representando a soma dos genes do indivíduo.
    """
    return sum(individuo) + 1


def funcao_objetivo_cnb(individuo):
    """Calcula o fitness do indivíduo para o problema das caixas não-binárias
    
    Args:
      individuo: lista que representa um indivíduo dentro do problema das CNB
      
    Returns:
      Um valor que representa o fitness do indivíduo
    """
    fitness = sum(individuo)
    return fitness


def funcao_objetivo_pop_cb(populacao):
    """Calcula a funcao objetivo para todos os membros de uma população
    
    Args:
      populacao: lista com todos os indivíduos da população
    
    Return:
      Lista de valores representando a fitness de cada indivíduo de uma população.
    """
    fitness = []
    for individuo in populacao:
        fobj = funcao_objetivo_cb(individuo)
        fitness.append(fobj)
    return fitness


def funcao_objetivo_pop_cnb(populacao):
    """Calcula o fitness da população completa
    
    Args:
      populacao: lista com todos os indivíduos da população
      
    Returns:
      Uma lista com o fitness de cada indivíduo em ordem
    """
    fitness_pop = []
    for individuo in populacao:
        fitness_ind = funcao_objetivo_cnb(individuo)
        fitness_pop.append(fitness_ind)
    return fitness_pop