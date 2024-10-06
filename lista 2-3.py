import numpy as np

# Função f(alpha)
def f(alpha, l1, l2, gamma):
    return (l2 * np.cos(np.pi - gamma - alpha) / np.sin(np.pi - gamma - alpha)) - (l1 * np.cos(alpha) / np.sin(alpha))

# Derivada de f(alpha)
def f_prime(alpha, l1, l2, gamma):
    term1 = (-l2 / np.sin(np.pi - gamma - alpha)**2)
    term2 = (-l1 / np.sin(alpha)**2)
    return term1 + term2

# Método de Newton
def newton_method(alpha0, l1, l2, gamma, erro=1e-8, max_iter=100):
    alpha = alpha0
    for i in range(max_iter):
        fa = f(alpha, l1, l2, gamma)
        fpa = f_prime(alpha, l1, l2, gamma)
         
        if abs(fa) < erro:
            print("\n")
            return alpha
        
        if fpa == 0:  # Evitar divisão por zero
            raise ValueError("Derivada zero")
        
        alpha_novo = alpha - fa / fpa
        print(f'Iteração {i+1}: {alpha_novo}')
        
        if abs(alpha_novo - alpha) < erro:
            return alpha_novo
        
        alpha = alpha_novo
    
    print("Número máximo de iterações atingido.")
    return alpha

# Parâmetros
l2 = 10
l1 = 8
gamma = 3 * np.pi / 5

# Chutar um valor inicial para α
alpha0 = 0.1  # Ponto inicial

# Executar o método de Newton
alpha = newton_method(alpha0, l1, l2, gamma)

print(f"O valor de α encontrado é: {alpha}")
