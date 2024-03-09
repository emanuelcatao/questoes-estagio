'''
2. Escreva uma função que recebe um número inteiro n e retorna se n pertence à sequência de Fibonacci.
'''
def is_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b 
    return "Pertence à sequencia" if b == n else "Não pertence à sequencia"

''' 
print(is_fibonacci(13)) # Pertence à sequencia
print(is_fibonacci(14)) # Não pertence à sequencia
print(is_fibonacci(21)) # Pertence à sequencia
print(is_fibonacci(34)) # Pertence à sequencia
print(is_fibonacci(109)) # Não pertence à sequencia
'''