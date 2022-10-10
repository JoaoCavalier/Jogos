import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,51)
    total_tentativas = 0
    pontos = 1000

    print("Qual o Nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Díficil")

    nivel = int(input("Defina o Nível: "))

    if(nivel == 1):
        total_tentativas = 11
    elif(nivel == 2):
        total_tentativas = 8
    else:
        total_tentativas = 5

    #rodada = 1
    # while(rodada <= total_tentativas):

    for rodada in range(1, total_tentativas + 1):
        #print("Tentativa {} de {}".format(rodada, total_tentativas))
        print(f'Tentativa {rodada} de {total_tentativas}')
        chute = int(input("Digite um número entre 1 e 50: "))
        print("você digitou", chute)

        if(chute < 1 or chute > 50 ):
            print("Você deve digitar um número entre 1 e 50!")
            continue

        Acertou =  chute == numero_secreto
        Maior   = chute > numero_secreto
        Menor   = chute < numero_secreto

        if(Acertou):
            print(f"Você Acertou e fez {pontos} pontos!!")
            break
        else:
            if(Maior):
                print("Você errou! Chutou um numero maior que o numero secreto")
                if (rodada == total_tentativas):
                    print(f"O número secreto era {numero_secreto}. Você fez {pontos}")

            elif(Menor):
                print("Você errou! Chutou um numero menor que o numero secreto")
                if (rodada == total_tentativas):
                    print(f"O número secreto era {numero_secreto}. Você fez {pontos}")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

        #rodada = rodada + 1 ( while )

        # "R$ {:7.1f}".format(1000.12) format + float
        # "R$ {:07.2f}".format(4.11)   format + float

    print("Fim do jogo!!")

if(__name__ == "__main__"):
    jogar()