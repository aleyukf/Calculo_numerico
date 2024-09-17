# Alessandra Yukari Fujii RA:11202130820
# Faça implementação da função que calcula o valor de expoente com erro absoluto menor que 2^(-30).

# Utilizando esta função resolve a equação
# x=exp(-x)
# utilizando o método do ponto fixo.

# Retorne o resultado utilizando a base binária.

import math

def int_to_bin(num):
    if num > 1:
        return int_to_bin(int(num / 2)) + str(int(num % 2))
    else:
        return str(int(num))

def float_to_bin(num):
    #separa a parte inteira da decimal. Ex 4.33 = 4 e 0.33
    inteiro = int(num)
    decimal = num - inteiro

    # Converte a parte inteira para binario
    inteiro_bin = int_to_bin(inteiro)

    # Converte a parte decimal para binario
    # Começa com uma String vazia, a cada interação do while faz decimal = (decimal*2), se o resultado for maior que 1, adiciona 1 na string do binario, se não adiona 0, o loop continua até decimal = 0
    #Ex: 0.625 
    #Loop 1 - 0.625*2 = 1.25 -> então adiciona 1 na string e subtrai 1 do resultado
    #Loop 2 - 0.25*2 = 0.5 -> então adiciona 0 na string
    #Loop 3 - 0.5*2 = 1 -> então adiciona 1 na string e subtrai 1 do resultado
    #Como agora decimal = 0, o loop acaba e a string retornada é 101
    decimal_bin = ""
    i = 0
    #Enquanto decimal maior que 0 e numero de iteracoes for menor que 100 para o caso do número não convergir a 0
    while decimal > 0 and i < 100: 
        i = i + 1
        decimal = decimal * 2
        if decimal >= 1:
            decimal_bin = decimal_bin + ("1")
            decimal = decimal - 1.0
        else:
            decimal_bin = decimal_bin + ("0")

    # Combina as duas parte
    return inteiro_bin + '.' + decimal_bin

# g(x) = e^(-x)
def g(x):
    return (math.exp(-x))

#Calcula o ponto fixo da função g, de forma interativa, dado um x0 até o erro for menor que a tolerancia
def ponto_fixo(g, x0, tol):
    x_anterior = x0
    x = g(x_anterior)
    #Enquanto o erro de aproximação for maior que a tolerancia, continua a iterar
    while abs(x - x_anterior) > tol:
        x_anterior = x
        x = g(x_anterior)
    return x 

if __name__ == "__main__":    
    x0 = float(input("Entre com o valor inicial: "))
    tol = 2**(-30)
    sol = ponto_fixo(g, x0, tol)
    print(f"Ponto fixo = " + float_to_bin(sol))


