import random

def gerar_numeros_aleatorios(inicio, fim):
    return random.randint(inicio, fim)

def main():
    lista_numeros = []

    for _ in range(5):
        inicio = int(input("Digite o valor inicial: "))
        fim = int(input("Digite o valor final: "))
        
        numero_aleatorio = gerar_numeros_aleatorios(inicio, fim)
        lista_numeros.append(numero_aleatorio)
        print(f"\nNúmero aleatório gerado: {numero_aleatorio}\n")

    print(f"\nLista com todos os números gerados:", lista_numeros)

main()