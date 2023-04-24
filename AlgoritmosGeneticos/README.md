<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=00008B&height=120&section=header"/>

[![Typing SVG](https://readme-typing-svg.herokuapp.com/?color=4B0082&size=35&center=true&vCenter=true&width=1000&lines=Bem-vindo(a)+à+pasta+de+Algoritmos+Genéticos!;Só+para+lembrar;meu+nome+é+Vitória+Yumi+Uetuki+Nicoleti;E+serei+sua+glia+nessa+fasntástica+formação;de+novas+sinapses.;Fique+agora+com+AlgoritmosGeneticos+:%29+!;print(AlgoritmosGeneticos))](https://git.io/typing-svg)

<p style='text-align: justify'> Bem-vindo(a), novamente, à pasta de Algoritmos Genéticos 🧬! 😄 
    
Espero muito podermos nos aventurarmos por meio desses experimentos e formarmos muitas novas conexões/sinapses nessa trajetória!! Caso caiu aqui de paraquedas, sem passar pela parte principal de todo esse repositório, <a href="https://github.com/viyuetuki/aula_redes">clique aqui</a>, que será redirecionado para lá e poderá começar a abrir seus horizontes para o conhecimento que aqui te espera.

Vamos começar? 🤩 Prepare-se para programar...</p>


# Experimentos de otimização e algoritmos genéticos 🧬

<p style='text-align: justify'> Como já mencionado, nesta pasta, estão armazenados os arquivos dos experimentos de algoritmos genéticos, que se baseiam em otimização. As problemáticas foram desenvolvidas pelo Professor Doutor Daniel R. Cassar e o código, além de partes terem sido desenvolvidas em conjunto com ele durante as aulas, outras são de minha autoria, como completações, comentários, conclusões, descrições e experimentos do tipo GA (fique tranquilo(a) que isso será apresentado em breve!).</p>

## Conceitos e fundamentos 📜

<p style='text-align: justify'> Assim como que, para se construir uma boa edificação, que não seja derrubada por qualquer ventania e outros fatores, é essencial que uma boa base e fundação seja feita, é imprescindível, quando tratamos de aprender algo novo, que uma base sólida de saberes seja construída por nós. Assim, para que nossas sinapses fiquem firmes e fortes, façam parte da nossa memória de longa duração e para que não as perdamos com certa facilidade, além de que possamos compreender tudo o que vem a seguir, precisamos reforçar bem os conceitos iniciais.

Para isso, o que acha, então, de começarmos apredendo tópicos que vamos utilizar em nossos códigos? 

</p>

## 🗃 Arquivos

<p style='text-align: justify'> Para nos situarmos aqui dentro, cabe ressaltar que cada arquivo presente nesta pasta consiste em:</p>
    
---------------------
<b> Experimentos</b>:

<p style='text-align: justify'> ✅ <a href="https://github.com/viyuetuki/aula_redes/blob/main/AlgoritmosGeneticos/experimento%20A.01%20-%20busca%20aleatoria.ipynb">experimento A.01 - busca aleatoria.ipynb</a> - Este arquivo é referente ao primeiro experimento realizado em sala, visando entender o conceito de otimização pelo problema das caixas binárias, por meio de busca aleatória. Nele, o algoritmo foi desenvolvido em conjunto com o professor e feito com apenas 4 caixas para poder ter conhecimento da solução e começar a criar domínio sobre o tópico.

Funções que implementamos em <a href="https://github.com/viyuetuki/aula_redes/blob/main/AlgoritmosGeneticos/funcoes.py">funcoes.py</a>:</p>
```
gene_cb
indivíduo_cb
funcao_objetivo_cb
```

<p style='text-align: justify'> ✅ <a href="https://github.com/viyuetuki/aula_redes/blob/main/AlgoritmosGeneticos/experimento%20A.02%20-%20busca%20em%20grade.ipynb">experimento A.2 - busca em grade.ipynb</a> - Este arquivo é referente ao segundo experimento realizado em sala, visando entender o conceito de otimização, em semelhança ao anterior, pelo problema das caixas binárias, por meio de busca em grade. Nele, o algoritmo também foi desenvolvido em conjunto com o professor.

Aqui, não implementamos nenhuma função nova. Mas utilizamos, do arquivo <a href="https://github.com/viyuetuki/aula_redes/blob/main/AlgoritmosGeneticos/funcoes.py">funcoes.py</a>, a função:</p>
```
funcao_objetivo_cb
```
<p style='text-align: justify'> E fizemos uso de loop for e da biblioteca itertools.</p>

<p style='text-align: justify'> ✅ <a href="https://github.com/viyuetuki/aula_redes/blob/main/AlgoritmosGeneticos/experimento%20A.03%20-%20algoritmo%20genetico.ipynb">experimento A.3 - algoritmo genetico.ipynb</a> - Este arquivo é referente ao primeiro algoritmo genético estruturado em sala, a fim de se resolver o problema das caixas binárias. O quesito de seleção, crossing-over e mutação também foram acrescidos e apresentados nesse experimento. Nesse caso, o algoritmo foi desenvolvido em conjunto com o professor, e comentado e concluído por mim 😊.

Funções que implementamos em <a href="https://github.com/viyuetuki/aula_redes/blob/main/AlgoritmosGeneticos/funcoes.py">funcoes.py</a>:</p>
```
populacao_cb
funcao_objetivo_pop_cb
selecao_roleta_max
cruzamento_ponto_simples
mutacao_cb
```

<p style='text-align: justify'> ✅ <a href="https://github.com/viyuetuki/aula_redes/blob/main/AlgoritmosGeneticos/experimento%20A.04%20-%20caixas%20nao-binarias.ipynb">experimento A.4 - caixas nao-binarias.ipynb</a> - Este arquivo é referente ao algoritmo genético que visa resolver o problema das caixas não-binárias. Contou com seleção, crossing-over e mutação também, possibilitando ainda mais verificar a questão de variabilidade genética. Aqui as funções locais foram apresentadas e o conceito de constantes de busca e do problema também. Neste caso, o algoritmo foi desenvolvido em conjunto na sala de aula e baseado no que o professor fez.</p>

Funções que implementamos em <a href="https://github.com/viyuetuki/aula_redes/blob/main/AlgoritmosGeneticos/funcoes.py">funcoes.py</a>:</p>
```
populacao_cnb
funcao_objetivo_cnb
funcao_objetivo_pop_cnb
selecao_roleta_max
cruzamento_ponto_simples
mutacao_cnb
```

<p style='text-align: justify'> ✅ <a href="https://github.com/viyuetuki/aula_redes/blob/main/AlgoritmosGeneticos/experimento%20A.05%20-%20descobrindo%20a%20senha.ipynb">experimento A.5 - descobrindo a senha.ipynb</a> - Este arquivo é referente ao algoritmo genéticos que tem como objetivo resolver o problema de descobrir uma senha dada uma fornecida. Englobou seleção, crossing-over e mutação. Além disso, como trata com caracteres, faz uso de uma função ord() que os transforma em respectivos números ordinais. O código foi desenvolvido juntamente ao professor, mas a senha dada e conteúdo escrito foram feitos por mim.

Funções que implementamos em <a href="https://github.com/viyuetuki/aula_redes/blob/main/AlgoritmosGeneticos/funcoes.py">funcoes.py</a>:</p>
```
populacao_inicial_senha
funcao_objetivo_senha
funcao_objetivo_pop_senha
selecao_torneio_min
cruzamento_ponto_simples
mutacao_senha
```

<p style='text-align: justify'> ✅ <a href="https://github.com/viyuetuki/aula_redes/blob/main/AlgoritmosGeneticos/experimento%20A.06%20-%20o%20caixeiro%20viajante.ipynb">experimento A.06 - o caixeiro viajante.ipynb</a> - Este arquivo é referente à resolução do problema do caixeiro viajante, visto pela primeira vez na disciplina de Lógica Computacional como um problema NP difícil, ou seja, que não há um algoritmo totalmente eficaz para resolver, ao menos que todas as possibilidades fossem testadas. Aqui, foram apresentadas duas vias de resolução para comparação, portanto: busca por algoritmos genéticos; busca exaustiva testando todas as permutações.

Funções que implementamos em <a href="https://github.com/viyuetuki/aula_redes/blob/main/AlgoritmosGeneticos/funcoes.py">funcoes.py</a>:</p>
```
cria_cidades
populacao_inicial_cv
funcao_objetivo_cv
funcao_objetivo_pop_cv
cruzamento_ordenado
mutacao_de_troca
```
<p style='text-align: justify'> Outra função utilizada que foi importada nesse notebook, além da random:</p>
```
permutations da biblioteca itertools
```

<p style='text-align: justify'> ✅ <a href="https://github.com/viyuetuki/aula_redes/blob/main/AlgoritmosGeneticos/experimento%20A.07%20-%20aplicando%20restricoes.ipynb">experimento A.07 - aplicando restricoes.ipynb</a> - Este arquivo é referente à resolução do problema da mochila (que também vimos em Lógica Computacional), em que além encontrarmos uma mochila com itens somando maior valor, devemos considerar a restrição de que ela não pode exceder 15 unidades massa, para não rasgar.

Funções que implementamos em <a href="https://github.com/viyuetuki/aula_redes/blob/main/AlgoritmosGeneticos/funcoes.py">funcoes.py</a>:</p>
```
computa_mochila
funcao_objetivo_mochila
funcao_objetivo_pop_mochila
```

<p style='text-align: justify'> ✅ <a href="https://github.com/viyuetuki/aula_redes/blob/main/AlgoritmosGeneticos/experimento%20A.08%20-%20usando%20o%20modulo%20DEAP.ipynb">experimento A.08 - usando o modulo DEAP.ipynb</a> - Este arquivo contém experimento de busca aleatória resolvido pelo módulo DEAP e a função eaSimple.</p>

<p style='text-align: justify'> ✅ <a href="https://github.com/viyuetuki/aula_redes/blob/main/AlgoritmosGeneticos/experimento%20A.09%20-%20usando%20o%20modulo%20DEAP%20sem%20o%20eaSimple.ipynb">experimento A.09 - usando o modulo DEAP sem o eaSimple.ipynb</a> - Este arquivo contém experimento das caixas binárias resolvido pelo módulo DEAP e sem a função eaSimple.</p>

<p style='text-align: justify'> ✅ <a href="https://github.com/viyuetuki/aula_redes/blob/main/AlgoritmosGeneticos/experimento%20A.10%20-%20caixas%20nao-binarias%20com%20DEAP.ipynb">experimento A.10 - caixas nao-binarias com DEAP.ipynb</a> - Este arquivo contém experimento das caixas não-binárias resolvido pelo módulo DEAP e com a função eaSimple.</p>

<p style='text-align: justify'> ✅ <a href="https://github.com/viyuetuki/aula_redes/blob/main/AlgoritmosGeneticos/experimento%20A.11%20-%20descobrindo%20a%20senha%20com%20DEAP.ipynb">experimento A.11 - descobrindo a senha com DEAP.ipynb</a> - Este arquivo contém experimento de descobrir a senha resolvido pelo módulo DEAP e com a função eaSimple.</p>

<p style='text-align: justify'> ✅ <a href="https://github.com/viyuetuki/aula_redes/blob/main/AlgoritmosGeneticos/experimento%20GA.01%20-%20senha%20de%20tamanho%20variavel.ipynb">experimento GA.01 - senha de tamanho variavel</a> - Este arquivo contempla a resolução do experimento da senha de tamanho variável, em que ele não é dado no momento da geração dela. Esse, inteiramente, foi sendo desenvolvido por mim, contando tanto com funções reaproveitadas quanto novas.</p>

Funções que implementamos em <a href="https://github.com/viyuetuki/aula_redes/blob/main/AlgoritmosGeneticos/funcoes.py">funcoes.py</a>:</p>
```
individuo_senha_var
populacao_inicial_senha_var
cruzamento_ponto_simples_senha_var
mutacao_tam_senha_var
funcao_objetivo_senha_var
funcao_objetivo_pop_senha_var
```
    
---------------------
<b> Arquivos .py</b>:

<p style='text-align: justify'> 📂 <a href="https://github.com/viyuetuki/aula_redes/blob/main/AlgoritmosGeneticos/classes.py">classes.py</a> - Este arquivo não foi utilizado, mas tinha a função de armazenar as classes utilizadas nos experimentos.</p>

<p style='text-align: justify'> 📂 <a href="https://github.com/viyuetuki/aula_redes/blob/main/AlgoritmosGeneticos/constantes.py">constantes.py</a> - Este arquivo não foi utilizado, mas tinha a função de armazenar as constantes utilizadas nos experimentos.</p>

<p style='text-align: justify'> 📁 <a href="https://github.com/viyuetuki/aula_redes/blob/main/AlgoritmosGeneticos/funcoes.py">funcoes.py</a> - Neste arquivo, serão armazenadas todas as funções sendo utilizadas ao longo do tempo nos experimentos/projetos. Com este arquivo, a reutilização de funções nos mais diversos arquivos da pasta será possibilitada, assim como a organização será evidenciada.</p>

---------------------
<b> Aprendizados para se relembrar e alguns extras</b>:

<p style='text-align: justify'> 🗂 <a href="https://github.com/viyuetuki/aula_redes/blob/main/AlgoritmosGeneticos/Algumas%20coisas%20que%20valem%20a%20pena%20aprender%20ou%20relembrar.ipynb">Algumas coisas que valem a pena aprender ou relembrar.ipynb</a> - Este arquivo contém informações interessantes para serem aprendidas ao longo do curso sempre que desejado.</p>
    
<details><summary><h3>Tópicos relembrados</h3></summary>
    <ul>
     <b> O módulo random</b>
        <li> <b> Tenho uma lista e quero sortear um item</b></li>
        <li> <b> Tenho uma lista e quero sortear n itens com reposição</b></li>
        <li> <b> Tenho uma lista e quero sortear um item, mas a chance de sortear cada item não é igual</b></li>
        <li> <b> Tenho uma lista e quero sortear n itens com reposição, mas a chance de sortear cada item não é igual</b></li>
        <li> <b> Tenho uma lista e quero sortear n itens sem reposição</b></li>
        <li> <b> Quero sortear um número inteiro dentro do intervalo [a,b]</b></li>
        <li> <b> Quero sortear um número real dentro do intervalo[0,1[</b></li>
        <li> <b> Quero sortear um número real dentro do intervalo [a,b]</b></li>
        <li> <b> Quero sortear um número real a partir de uma distribuição normal (Gaussiana)</b></li>
        <li> <b> Quero embaralhar uma lista de objetos</b></li>
    <b> O módulo itertools</b>
        <li> <b> Quero fazer o produto cartesiano entre duas ou mais listas</b></li>
        <li> <b> Quero fazer a permutação dos elementos de uma lista</b></li>
    <b> A função zip</b>
    <b> O objeto deque</b>
    <b> Convertendo uma letra ou um símbolo em um número</b>
    <b> Funções parciais</b>
    </ul></details>
    
---------------------
<b> Explicação</b>:
    
<p style='text-align: justify'> 📁 <a href="https://github.com/viyuetuki/aula_redes/blob/main/AlgoritmosGeneticos/README.md">README.md</a> - É o arquivo do readme, com extensão markdown, desta repositório referente a Algoritmos Gnéticos, que nada mais é do que exatamente o que você está lendo agora.</p>

<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=00008B&height=120&section=footer"/>