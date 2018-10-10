import random

def dados(num_dados=1, jogadas=2, faces=6):
    
    resultados = dict()
    
    for i in range(jogadas):
        resultados["jogada{}".format(i+1)] = dict()
        for j in range(num_dados):
            resultados["jogada{}".format(i+1)]["dado{}".format(j+1)] = random.randint(1, faces)
    
    return resultados