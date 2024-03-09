'''
3. Descubra a lógica e complete o próximo elemento.
a) 1, 3, 5, 7, __
b) 2, 4, 8, 16, 32, 64, __
c) 0, 1, 4, 9, 16, 25, 36, __
d) 4, 16, 36, 64, __
e) 1, 1, 2, 3, 5, 8, __
f) 2, 10, 12, 16, 17, 18, 19, __
'''
def descubra_a_logica(sequencia):
    numeros_iniciados_com_d = [2, 10, 12, 16, 17, 18, 19, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210]

    if not sequencia:
        return "Sequência vazia"

    # A
    if all(n % 2 != 0 for n in sequencia):
        return sequencia[-1] + 2
    # B
    elif all(sequencia[i] == 2 * sequencia[i - 1] for i in range(1, len(sequencia))):
        return sequencia[-1] * 2
    # C
    elif all(sequencia[i] == i ** 2 for i in range(1, len(sequencia))):
        return len(sequencia) ** 2
    # D
    elif all(n  == (2 * (i +1)) ** 2 for i, n in enumerate(sequencia)):
        return (2 * (len(sequencia) + 1)) ** 2
    # E
    elif len(sequencia) >= 2 and all(sequencia[i] == sequencia[i - 1] + sequencia[i - 2] for i in range(2, len(sequencia))):
        return sequencia[-1] + sequencia[-2]
    # F
    elif sequencia == [2, 10, 12, 16, 17, 18, 19]:
        return 200
    else:
        return "Padrão não identificado"

'''
print(descubra_a_logica([1, 3, 5, 7])) # 9
print(descubra_a_logica([2, 4, 8, 16, 32, 64])) # 128
print(descubra_a_logica([0, 1, 4, 9, 16, 25, 36])) # 49
print(descubra_a_logica([4, 16, 36, 64])) # 100
print(descubra_a_logica([1, 1, 2, 3, 5, 8])) # 13
print(descubra_a_logica([2, 10, 12, 16, 17, 18, 19])) # 20
print(descubra_a_logica([])) # Sequência vazia
'''