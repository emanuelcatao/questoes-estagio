def inverte_string_slicing(string):
    return string[::-1]

def inverte_string_interativo(string):
    string_invertida = ""
    for letra in string:
        string_invertida = letra + string_invertida
    return string_invertida

def inverte_string_sem_facilidades(string):
    string_invertida = ""
    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]
    return string_invertida

'''
print(inverte_string_slicing("teste")) # etset
print(inverte_string_interativo("teste")) # etset
print(inverte_string_sem_facilidades("teste")) # etset
'''
