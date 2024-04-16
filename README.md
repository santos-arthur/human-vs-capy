# Human-vs-Capy 

## Descrição 📑
 Human-vs-Capy é um jogo feito em Python para aula de Lógica e Técnica de Programação da Turma de Engenharia de Software da Uniasselvi (EGSO011)


## Desafios 🧮
- 🚫 **Não utilizar bibliotecas voltadas para o desenvolvimento de jogos.**
- 🚫 **Não utilizar conceitos de Programação Orientada a Objetos.**

## Como jogar? 🎮
 1. Clone o repositório em questão com o comando: `git clone https://github.com/santos-arthur/human-vs-capy.git`
 
 2. Navegue até os arquivos do jogo com o comando: `cd human-vs-capy`
 
 3. Instale as dependências com o comando: `pip install -r requirements.txt`
 
 4. Executar o jogo com o comando `python ./main.py`
 
 5. Para uma melhor experiência, o jogo foi pensado para ser jogado com o console com 48 caracteres de largura e aproximadamente 30 caracteres de altura.

    **A tela de configurações dispõe de um assistente para esse ajuste.**

## Mecânicas ⚙️
- ⚔️ O jogo foi pensado para ser um RPG de combate por turnos.

- 🔼 O jogador joga contra a máquina em **10 níveis** incrementais.

- 🎲 Os inimigos, bem como sua quantidade, são gerados de maneira pseudoaleatória, com base nos **pontos**, no **nível** e na **dificuldade** selecionada pelo jogador.

- 💼 Todos os inimigos derrotados deixam cair **itens** quando morrem que podem ser **equipados** ou **consumidos** pelo jogador.

- 🔫 Existe um controle de limite de **armas** possuídas pelo jogador.

- ⏱️ Consumir um item gasta uma **ação** do jogador.

- 🛡️ O jogador não terá mais de uma **armadura** por vez.

- ⬆️ Passar de nível concede um incremento de **vida máxima** e devolve todas as **ações** para o jogador.

- 💾 O método como o jogo foi desenvolvido e pensado, implicava na existência de vários 'saves' do jogo. Então, foi criada uma funcionalidade que permite que o jogador **saia do jogo** e **continue sua aventura** a qualquer momento. **É permitida apenas uma aventura por vez.**

## Maiores Dificuldades 🏋️
- 📦 Durante o desenvolvimento do jogo, como não podíamos ter objetos, tive que arrumar uma maneira, meio complexa, com dicionários, para passar as entidades de um módulo para o outro.

- 🔄 Não utilizar bibliotecas prontas nos levou a recriarmos várias soluções, desde as básicas como limpar o console ou centralizar texto, até mesmo soluções mais complexas como menus de duas dimensões circulares.

- 🎹 Como optamos por fazer um 'jogo' sem ser baseado apenas em entrada de texto, tivemos que usar uma biblioteca que 'escuta' o teclado do jogador praticamente para todas as ações do jogo. Confesso que não gostei da solução final, porém foi a mais simples e prática que encontrei, tentando evitar os itens solicitados pelo professor.

- 🎵 Tentei implementar uma trilha sonora no game, porém o controle assíncrono de playlist, pular, voltar ou pausar, as músicas deu muito mais trabalho do que todo o resto do jogo e optei por não seguir com a ideia.

- 🔄 Sendo meu primeiro projeto complexo com Python, optei por reescrevê-lo praticamente inteiro quando terminei, pois não gostei das soluções originais. Várias vezes precisei refatorar as mesmas funções ou trechos até encontrar algo que conciliasse o recomendado pelas diretrizes da linguagem e o que eu pudesse entender de maneira rápida e prática.

## Pontos Positivos 🎉
- 🧠 O jogo possuir algumas limitações, principalmente de arquitetura, me fez pensar 'fora da caixa' para diversas soluções. Valeu muito o aprendizado e o desafio.

- 👍 Gostei de diversas soluções e praticidades que o Python se propõe a entregar para o desenvolvedor.

- 💻 Acredito que o 'core' do game, módulos de jogador, jogo, inimigos, menu e utils, foram o melhor que eu conseguiria produzir com o meu conhecimento atual da linguagem.

- 😄 O desenvolvimento do jogo, embora cansativo pela sua complexidade, foi no geral bem divertido, provendo risadas sinceras durante a prototipação e desenvolvimento de certas features.