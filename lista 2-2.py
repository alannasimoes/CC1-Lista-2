import numpy as np

# Função f(x)
def f(x):
    return np.exp(-x**2) - 2*x**2

# Derivada f'(x)
def dfd(x):
    return -2*x*np.exp(-x**2) - 4*x

# Método de Newton
def metodo_newton(x0, erro=1e-8, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfdx = dfd(x)
        print(f'Iteração {i+1}: {x}')
        if abs(fx) < erro:
            print(f"\n")
            return x
        
        if dfdx == 0:  # Evitar divisão por zero
            raise ValueError("Derivada zero")
        
        x_n = x - fx / dfdx # Fórmula Método de Newton
        
        if abs(x_n - x) < erro:
            return x_n
        
        x = x_n
    
    print("Número máximo de iterações atingido.")
    return x

# Testar para diferentes valores iniciais
x0 = -2 # Ponto inicial próximo de α1 < 0
raiz = metodo_newton(x0)

print(f"A raiz encontrada é: {raiz}")
