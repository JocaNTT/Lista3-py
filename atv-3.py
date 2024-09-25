def converter_temperatura(celsius, tipo):
    if tipo == 'F':
        return (9/5) * celsius + 32
    elif tipo == 'K':
        return celsius + 273.15

def main():
    while True:
        celsius = float(input("Digite a temperatura em graus Celsius (ou um valor negativo para sair): "))
        
        if celsius < 0:
            print("Obrigado!")
            break

        tipo = input("Digite F para converter para Fahrenheit ou K para converter para Kelvin: ")
        
        if tipo == 'F':
            resultado = converter_temperatura(celsius, 'F')
            print(f"{celsius}°C é equivalente a {resultado:.2f}°F.")
        elif tipo == 'K':
            resultado = converter_temperatura(celsius, 'K')
            print(f"{celsius}°C é equivalente a {resultado:.2f} K.")
        else:
            print("Opção inválida. Tente novamente.")

main()