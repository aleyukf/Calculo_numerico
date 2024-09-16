import math

def float_to_bin(num):
    #separa a parte inteiro e a decimal. Ex 4.33 = 4 e 0.33
    inteiro = int(num)
    decimal = num - inteiro

    # Converte a parte inteira para binario
    inteiro_bin = bin(inteiro)

    # Converte a parte decimal para binario
    # Começa com uma String vazia, a cada interação do while faz decimal = (decimal*2), se o resultado for maior que 1, adiciona 1 na string do binario, se não adiona 0, o loop continua até decimal = 0
    #Ex: 0.625 
    #Loop 1 - 0.625*2 = 1.25 -> então adiciona 1 na string e subtrai 1 do resultado
    #Loop 2 - 0.25*2 = 0.5 -> então adiciona 0 na string
    #Loop 3 - 0.5*2 = 1 -> então adiciona 1 na string e subtrai 1 do resultado
    #Como agora decimal = 0, o loop acaba e a string retornada é 101
    print(decimal)

    decimal_bin = ""
    while decimal > 0:
        decimal = decimal * 2
        print(decimal) # dixar essa linha se quiser o método passo a passo
        if decimal >= 1:
            decimal_bin = decimal_bin + ("1")
            decimal = decimal - 1.0
        else:
            decimal_bin = decimal_bin + ("0")

    # Combina as duas parte
    return inteiro_bin + '.' + decimal_bin


# g(x) = e^(-x)
def g(x):
    return math.exp(-x)

# Calcula o ponto fixo da função g, de forma recursiva, dado um x0 até o erro for menor que a tol
def ponto_fixo2(g, x0, tol):
    x = g(x0)
    if abs(x - x0) > tol:
        return ponto_fixo2(g, x, tol)
    else:
        return x

#Calcula o ponto fixo da função g, de forma interativa, dado um x0 até o erro for menor que a tol
def ponto_fixo(g, x0, tol):
    x_anterior = x0
    x = g(x_anterior)
    #Enquanto o erro de aproximação for maior que a tolerancia, continua a inteirar
    while abs(x - x_anterior) > tol:
        x_anterior = x
        x = g(x_anterior)
    return x 

if __name__ == "__main__":    
    x0 = 0.5  # Aproximação inicial
    sol = ponto_fixo(g, x0,2**(-30))
    sol2 = ponto_fixo2(g, x0,2**(-30))

    print(f"Ponto fixo encontrado com método interativo: " + float_to_bin(sol))
    print(f"Ponto fixo encontrado com método recursivo: " + float_to_bin(sol2))import math

def float_to_bin(num):
    #separa a parte inteiro e a decimal. Ex 4.33 = 4 e 0.33
    inteiro = int(num)
    decimal = num - inteiro

    # Converte a parte inteira para binario
    inteiro_bin = bin(inteiro)

    # Converte a parte decimal para binario
    # Começa com uma String vazia, a cada interação do while faz decimal = (decimal*2), se o resultado for maior que 1, adiciona 1 na string do binario, se não adiona 0, o loop continua até decimal = 0
    #Ex: 0.625 
    #Loop 1 - 0.625*2 = 1.25 -> então adiciona 1 na string e subtrai 1 do resultado
    #Loop 2 - 0.25*2 = 0.5 -> então adiciona 0 na string
    #Loop 3 - 0.5*2 = 1 -> então adiciona 1 na string e subtrai 1 do resultado
    #Como agora decimal = 0, o loop acaba e a string retornada é 101
    print(decimal)

    decimal_bin = ""
    while decimal > 0:
        decimal = decimal * 2
        print(decimal) # dixar essa linha se quiser o método passo a passo
        if decimal >= 1:
            decimal_bin = decimal_bin + ("1")
            decimal = decimal - 1.0
        else:
            decimal_bin = decimal_bin + ("0")

    # Combina as duas parte
    return inteiro_bin + '.' + decimal_bin


# g(x) = e^(-x)
def g(x):
    return math.exp(-x)

# Calcula o ponto fixo da função g, de forma recursiva, dado um x0 até o erro for menor que a tol
def ponto_fixo2(g, x0, tol):
    x = g(x0)
    if abs(x - x0) > tol:
        return ponto_fixo2(g, x, tol)
    else:
        return x

#Calcula o ponto fixo da função g, de forma interativa, dado um x0 até o erro for menor que a tol
def ponto_fixo(g, x0, tol):
    x_anterior = x0
    x = g(x_anterior)
    #Enquanto o erro de aproximação for maior que a tolerancia, continua a inteirar
    while abs(x - x_anterior) > tol:
        x_anterior = x
        x = g(x_anterior)
    return x 

if __name__ == "__main__":    
    x0 = 0.5  # Aproximação inicial
    sol = ponto_fixo(g, x0,2**(-30))
    sol2 = ponto_fixo2(g, x0,2**(-30))

    print(f"Ponto fixo encontrado com método interativo: " + float_to_bin(sol))
    print(f"Ponto fixo encontrado com método recursivo: " + float_to_bin(sol2))
