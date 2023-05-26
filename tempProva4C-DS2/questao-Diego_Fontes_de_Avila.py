'''
Calcula a longitude de um navio pirata ao longo dos dias de uma viagem seguindo a linha do equador,
dados a longitude inicial(graus), a longitude final(graus) e a velocidade(Km/h)
'''
def posNavio (longInit, longFin, velocidadeKmH):
    from math import ceil
    
    grauToKm = 111 # Cada grau de latitude equivale a 111Km
    longCurr = longInit # Longitude começa na inicial
    totalDias = ceil((longFin-longInit) * grauToKm / (velocidadeKmH  * 24)) # Calcula o número total de dias
    distDiaria = velocidadeKmH * 24 / grauToKm # Calcula a distância percorrida por dia

    for dia in range(totalDias):
        longCurr += distDiaria # Soma a distancia percorrida no dia
        if longCurr > longFin: longCurr = longFin # Define o fim da viagem
        print(f"No final do dia {dia + 1}, a posição do navio é {longCurr:.2f} graus de longitude.")

posNavio(0, 24*51, 111)