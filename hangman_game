import random


def verifica_acerto(palavra_temp, letra_temp, resposta_temp):
    posicao = 0
    acertos_temp: int = 0
    for l in palavra_temp:
        if letra_temp.lower() == l.lower():
            resposta_temp[posicao] = letra_temp
            print('Você acertou!', resposta_temp)
        if resposta_temp[posicao] == palavra_temp[posicao]:
            acertos_temp += 1
        posicao += 1
    return acertos_temp


# Inicializando variaveis
randomic = ['guitarra', 'navio', 'australia', 'chapeu', 'capoeira']
palavra = randomic[random.randrange(0, len(randomic))].lower()
win = False
loose = False
erros = 0
acertou = 0

# Menu inicial
print('Bem vindo ao jogo da forca!')
x = int(input('Escolha a opção desejada\n\t1) Escolher uma palavra\n\t2) Usar palavra pré definida\n\t'))
if x == 1:
    while x != 'Y':
        palavra = input('Digite a palavra desejada:\t')
        x = input('A palavra desejada é {0}? (Y/N)\t'.format(palavra))
    print('Palavra definida, vamos começar!')
    print('\n' * 130)
    print('Bem vindo ao Jogo da Forca!')
    print('Sua palavra tem', len(palavra), 'Letras!')
    print('Você terá {} tentativas'.format(len(palavra) * 2))
if x == 2:
    print('\n' * 130)
    print('Bem vindo ao Jogo da Forca!')
    print('Sua palavra tem', len(palavra), 'Letras!')
    print('Você terá {} tentativas'.format(len(palavra) * 2))

# Definindo a resposta
resposta = []
for y in range(0, len(palavra)):
    resposta.append('_')

# Respondendo
while not win and not loose:
    letra = input('Digite uma letra a sua escolha (Utilizar letras minusculas)\n\t')
    if letra in palavra:
        acertou = verifica_acerto(palavra, letra, resposta)
    else:
        erros += 1
        print('Você errou!')
        print('Total de tentativas: {}'.format(len(palavra) * 2 - erros))

    # Vitoria ou derrota
    if erros == len(palavra) * 2:
        loose = True
        print('Você perdeu, a palavra era {}!'.format(palavra))
    elif acertou == len(palavra):
        win = True
        print('Parabens, você venceu, a palavra era {}!'.format(palavra))
