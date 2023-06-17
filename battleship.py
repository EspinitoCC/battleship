import random

jogador = []
computador = []
computador_escondido = []

for j in range (5):
    jogador.append(["-"] * 10)

for c in range(5):
    computador.append(["-"] * 10)

for e in range(5):
    computador_escondido.append(["-"] * 10)

def tabuleiro(jogador):
    l = 0
    for linha in jogador:
        print(linha)
        l += 1

#Aqui e onde o jogador vai posicionar os seus navios
def navios_jogador():
    print("Posicione seus cinco barcos no tabuleiro!")

    for i in range (5):

        # Esses dois whiles são usados caso o jogador escreva um valor que não está dentrop das linhas e colunas
        linha_jogador = int(input("Selecione a linha."))

        while linha_jogador not in (0, 1, 2, 3, 4):
            print("Erro, tente novamente!")
            linha_jogador = int(input("Selecione a linha."))

        coluna_jogador = int(input("Selecione a coluna."))

        while coluna_jogador not in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
            print("Erro, tente novamente!")
            coluna_jogador = int(input("Selecione a coluna."))

        jogador[linha_jogador][coluna_jogador] = "N"
        return int(linha_jogador), int(coluna_jogador)

#Nessa função o jogador vai decidir onde do tabuleiro ele vai atirar
def tiro_jogador():

    linha_tiro_jogador = int(input("Escolha a linha que ira atirar."))

    while linha_tiro_jogador not in (0, 1, 2, 3, 4):
        print("Erro, tente novamente!")
        linha_tiro_jogador = int(input("Escolha a linha que ira atirar."))

    coluna_tiro_jogador = int(input("Escolha a coluna que ira atirar."))

    while coluna_tiro_jogador not in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
        print("Erro, tente novamente!")
        coluna_tiro_jogador = int(input("Escolha a coluna que ira atirar."))

    return int(linha_tiro_jogador), int(coluna_tiro_jogador)

#Aqui e onde o computador vai posicionar seus navios com o import random
def navios_computador():

    for x in range (5):

        linha_computador = int(random.randint(0,4))
        coluna_computador = int(random.randint(0,9))

        while computador[linha_computador][coluna_computador] == "N":
            linha_computador = int(random.randint(0, 4))
            coluna_computador = int(random.randint(0, 9))

        computador[linha_computador][coluna_computador] = "N"
        return int(linha_computador), int(coluna_computador)

#Aqui o computador vai decidir uma linha e uma coluna aleatoria para atirar, caso ele tente atirar na mesma ele tem a chance de atirar em outro lugar diferente do jogador
def tiro_computador():

    linha_tiro_computador = int(random.randint(0,4))
    coluna_tiro_computador = int(random.randint(0,9))
    while jogador[linha_tiro_computador][coluna_tiro_computador] == "N" or jogador[linha_tiro_computador][coluna_tiro_computador] == "N":
        linha_tiro_computador = int(random.randint(0, 4))
        coluna_tiro_computador = int(random.randint(0, 9))
    return linha_tiro_computador, coluna_tiro_computador

#Aqui finalmente começa o jogo, mostrando tabuleiro do jogador e criando as variaveis de quantos navios o computador e o jogador tem no momento, além de uma pontuação.

tabuleiro(jogador)
navios = 5
while navios != 0:
    linha_jogador, coluna_jogador = navios_jogador()
    navios_computador()
    tabuleiro(jogador)
    navios -= 1

print("                             INICIAR")
print("Seu objetivo é acertar todos os navios do seu inimigo (computador)!")
na_jogador = 5
na_computador = 5

pontuacao_jogador = 0
pontuacao_computador = 0

while True:
    print("                       JOGADOR")
    tabuleiro(jogador)
    print("                      COMPUTADOR")
    tabuleiro(computador_escondido)
    print("                  PLACAR")
    print(f"Seus pontos:{pontuacao_jogador} Pontos do computador:{pontuacao_computador}")
    print(f"Seus navios:{na_jogador} Navios do computador:{na_computador}")
    linha_tiro_jogador, coluna_tiro_jogador = tiro_jogador()

    if computador_escondido[linha_tiro_jogador][coluna_tiro_jogador] == "O":
        print("Esse lugar ja foi acertado!")

    elif computador_escondido[linha_tiro_jogador][coluna_tiro_jogador] == "X":
        print("Esse navio ja foi derrubado!")

    elif computador[linha_tiro_jogador][coluna_tiro_jogador] == "N":
        print("Você acertou um navio!")
        computador_escondido[linha_tiro_jogador][coluna_tiro_jogador] = "X"
        na_computador -= 1
        pontuacao_jogador += 1

    else:
        print("Você errou!")
        computador_escondido[linha_tiro_jogador][coluna_tiro_jogador] ="O"

    if pontuacao_jogador == 5:
        print("Você ganhou!")
        break

    print("Vez do computador.")
    linha_tiro_computador, coluna_tiro_computador = tiro_computador()
    if jogador[linha_tiro_computador][coluna_tiro_computador] == "N":
        print(f"O computador atirnou na linha {linha_tiro_computador} e a coluna {coluna_tiro_computador}")
        print("O computador acertou seu navio!")
        jogador[linha_tiro_computador][coluna_tiro_computador] = "X"
        pontuacao_computador += 1
        na_computador -= 1
    else:
        print(f"O computador atirou na linha {linha_tiro_computador} e a coluna {coluna_tiro_computador}")
        print("O computador errou seus navios!")
        jogador[linha_tiro_computador][coluna_tiro_computador] = "O"
    if pontuacao_computador == 1:
        print("Você perdeu!")
