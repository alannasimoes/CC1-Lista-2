def MN_raiz_quadrada(a, erro=1e-10):
    print(f'Questão 1 - Raíz quadrada de {a}')
    an = a/2
    iteracao = 0
    while abs(a - an**2) > erro:
        an = (an + a / an) / 2
        iteracao+=1
        print(f'Iteração {iteracao}: {an}')
    return an, iteracao

MN_raiz_quadrada(3)

def MN_raiz_cubica(a, erro=1e-10):
    print(f'\n Questão 1 - Raíz cúbica de {a}')
    an = a/3
    iteracao = 0
    while abs(a - an**3) > erro:
        an = an - (an - a/an**2)/3
        iteracao+=1
        print(f'Iteração {iteracao}: {an}')
    return an, iteracao

MN_raiz_cubica(100)