'''
Lógica que envolve a resolução:
1 - Ligar o interruptor 1 e deixar ligado por um bom tempo. Isso faz com que a 
lampada associada se aqueça.
2 - Desligar o interruptor 1 e ligar o interruptor 2.
3 - Deixar o interruptor 3 desligado.
4 - Ir para a sala onde estão as lâmpadas.
5 - A lampada acesa é controlada pelo interruptor 2, a apagada e quente pelo interruptor 1
e a apagada e fria pelo interruptor 3.
'''
def descobrir_lampadas():
    lampadas = {"Lâmpada 1": "quente", "Lâmpada 2": "acesa", "Lâmpada 3": "fria"}

    for lampada, estado in lampadas.items():
        if estado == "quente":
            print(f"A {lampada} é controlada pelo Interruptor 1.")
        elif estado == "fria":
            print(f"A {lampada} é controlada pelo Interruptor 3.")
        else:
            print(f"A {lampada} é controlada pelo Interruptor 2.")
        