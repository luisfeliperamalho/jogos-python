print("********************************")
print("Bem vindo no jogo de Adivinhação")
print("********************************")

#condicao if e else

# numero_secreto = 65;

# chute_str = input("Escolhe um numero: ");

# print("Você digitou o número", chute_str);

# chute = int(chute_str);

# acertou = chute == numero_secreto;
# maior = chute > numero_secreto;
# menor = chute < numero_secreto;

# #condicao if else
# if(acertou):
#     print("Você acertou");
# else:
#     if(maior):
#         print("Você errou! O seu chute foi maior do que o número secreto");
#     elif (menor) :
#         print("Você errou! O seu chute foi menor do que o número secreto");

# print("Fim do jogo!");

###############################################################################################################
#condicao while

#enquanto ainda há tentativas

numero_secreto = 65;
total_de_tentativas = 3;
rodada = 1;

while(rodada <= total_de_tentativas) :
    print("Tentativa ", rodada, "de ", total_de_tentativas);
    chute_str = input("Escolhe um numero: ");

    print("Você digitou o número", chute_str);

    chute = int(chute_str);

    acertou = chute == numero_secreto;
    maior = chute > numero_secreto;
    menor = chute < numero_secreto;

    #condicao if else
    if(acertou):
        print("Você acertou");
    else:
        if(maior):
            print("Você errou! O seu chute foi maior do que o número secreto");
        elif (menor) :
            print("Você errou! O seu chute foi menor do que o número secreto");

    rodada = rodada + 1;

    print("Fim do jogo!");