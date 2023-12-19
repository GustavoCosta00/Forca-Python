# JOGO DA FORCA

"""
1º SORTEAR UMA PALAVRA DE UMA LISTA;
2º MOSTRAR NA TELA A QTD DE LETRAS DE PALAVRA SELECIONADA;
3º PEDIR AO USUÁRIO PARA DIGITAR UMA PALAVRA ( FAZER VERIFICAÇÃO DE CARACTER );
4º TROCAR O DÍGITO PELA PALAVRA SELECIONADA PELO USUÁRIO, CASO NÃO SEJA VÁLIDA APARECE UM 'X' NO NÚMERO DE TENTATIVAS;
4.1º CASO O USUÁRIO ERRE 5 LETRAS ELE PERDE;
5º SE O USUÁRIO GANHAR OU PERDER ELE RECEBERÁ UMA NOTIFICAÇÃO SE DESEJA CONTINUAR OU NÃO;
"""

import random
import re

tentativas = 5


def sorteando_palavra():
    list_palavras = ['abelha','elefante','cobra','cachorro','gato','urso','cavalo','pernilongo']
    selecionar_palavra = random.choice(list_palavras)
    print("Dica: A palavra é {}".format(selecionar_palavra))
    return selecionar_palavra

guardando_palavra = sorteando_palavra()


def quebrando_palavra(palavra_oculta):
    for letra in palavra_oculta:
        print(letra, end=" ")


def letra_usuario():
    letra = str(input("Digite uma letra:  "))
    if(letra == ""):
        letra_usuario()
    elif re.match(r"^[a-z]+$", letra):
        print("A entrada é válida!")
    else:
        letra_usuario()
    return letra

    
def iniciando_jogo():
    global tentativas
    global guardando_palavra
    

    palavra_oculta = ["_" for _ in guardando_palavra]
    
    while tentativas > 0 and "_" in palavra_oculta:
        quebrando_palavra(palavra_oculta)
        print("\nNúmero de tentativas:", tentativas)

        letra = letra_usuario()

        if letra in guardando_palavra:
            for i in range(len(guardando_palavra)):
                if guardando_palavra[i] == letra:
                    palavra_oculta[i] = letra
        else:
            tentativas -= 1

    if "_" not in palavra_oculta:
        print("Parabéns! Você venceu!")
    else:
        print("Você perdeu >:(")



iniciando_jogo()