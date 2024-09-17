estados = []
alfabeto = []
func_transicao = {}
estado_inicial = ""
estados_finais = []
continuar = "s"

print("__________Automato Finito Deterministico__________")
print("\n")

print("Informe o conjunto de estados: ", end="")
estados = input().split()

print("Informe o alfabeto de entrada: ", end="")
alfabeto = input().split()

print("Informe o estado inicial: ", end="")
estado_inicial = input()

print("Informe o conjunto de estados finais: ", end="")
estados_finais = input().split()

print("Defina as funçoes de transcição: ")
for estado in estados:
    for simbolo in alfabeto:
        print(f"\t {simbolo}")
        print(f"{estado}\t---->\t", end="")
        proximo_estado = input()
        
        if proximo_estado == ".":
            func_transicao[(estado, simbolo)] = None
        else: 
            func_transicao[(estado, simbolo)] = proximo_estado

print("\n")

while continuar == "s":
    print("Informe a palavra: ", end="")
    entrada = input()

    estado_atual = estado_inicial

    for simbolo in entrada:
        print(f"Estado atual: {estado_atual}")
        print(f"Entrada atual: {simbolo}")

        print(f"Proximo estado: {func_transicao[(estado_atual, simbolo)]}")

        estado_atual = func_transicao[(estado_atual, simbolo)]

        if estado_atual == None:
            print("O automato nao reconheceu a linguagem")
            break

    print("\n")

    if estado_atual in estados_finais:
        print("Reconheceu")
    else:
        print("Não reconheceu")
    
    print("\n")
    
    print("Deseja continuar? (s/n): ", end="")
    continuar = input("")
    print("\n")