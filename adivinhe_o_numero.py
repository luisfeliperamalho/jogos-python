print("********************************")
print("Bem vindo no jogo de Adivinhação")
print("********************************")

numero_secreto = 87

chute_str = input("Escolhe um numero: ")

print("Você digitou o número", chute_str)

chute = int(chute_str)

#condicao if else
if numero_secreto != chute:
    print("Você errou")
else:
    print("Você acertou")

print("Fim do jogo!")