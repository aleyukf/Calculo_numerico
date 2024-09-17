# Calculo_numerico

Programa utilizado para calcular o ponto fixo da função $x = e ^{-x}$ com erro absoluto ($\epsilon$) menor que $2^{-30}$. Com resultado final convertido para a base binária.

## Método do ponto fixo

$x^{n+1} = g(x^n)$ , n $>=$ 1

Até que

$\mid {x^{n+1} - x^{n}} \mid <\epsilon$


onde n é a iteração