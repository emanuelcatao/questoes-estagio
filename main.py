from questao1 import questao1
from questao2 import is_fibonacci
from questao3 import descubra_a_logica
from questao4 import descobrir_lampadas
from questao5 import inverte_string_interativo, inverte_string_sem_facilidades, inverte_string_slicing

print("Resposta da questão 1:")
questao1()

print()
print("Resposta da questão 2:")
entrada = int(input("Digite um número inteiro: "))
print(is_fibonacci(entrada))

print()
print("Resposta da questão 3:")
entrada = input("De qual item você quer descobrir a lógica? (a, b, c, d, e, f):")
if entrada.lower() == 'a':
    entrada = [1, 3, 5, 7]
elif entrada.lower() == 'b':
    entrada = [2, 4, 8, 16, 32, 64]
elif entrada.lower() == 'c':
    entrada = [0, 1, 4, 9, 16, 25, 36]
elif entrada.lower() == 'd':
    entrada = [4, 16, 36, 64]
elif entrada.lower() == 'e':
    entrada = [1, 1, 2, 3, 5, 8]
elif entrada.lower() == 'f':
    entrada = [2, 10, 12, 16, 17, 18, 19]
else:
    print("Entrada inválida")
    exit()
print(descubra_a_logica(entrada))

print()
print("Resposta da questão 4:")
descobrir_lampadas()

print()
print("Resposta da questão 5:")
entrada = input("Digite uma string: ")
print(inverte_string_slicing(entrada))