import forca
import adivinhacao

def escolhe_jogos():
    print("*********************************")
    print("*****  Escolha o seu Jogo!  *****")
    print("*********************************")

    print("(1) Forca! - (2) Adivinhação!")

    jogo = int(input("Qual Jogo?: "))

    if(jogo == 1):
        print("Você escolheu Forca!!")
        forca.jogar()

    elif(jogo == 2):
        print("Você escolheu Adivinhação!!")
        adivinhacao.jogar()

if (__name__ == "__main__"):
    escolhe_jogos()