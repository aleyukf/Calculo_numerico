import ponto_fixo as pf

# g(x) = e^(-x)
def g(x):
    return (math.exp(-x))


x0 = 0.5  # Aproximação inicial
sol = pf.ponto_fixo(g, x0,2**(-30))

print(f"Ponto fixo encontrado com método interativo: " + pf.float_to_bin(sol))

