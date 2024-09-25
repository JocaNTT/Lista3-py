# Dicionário com as cotações de algumas moedas (cotação simulada, atualize conforme necessário)
cotacoes = {
    '1': {'nome': 'Dólar (USD)', 'cotacao': 5.48},
    '2': {'nome': 'Euro (EUR)', 'cotacao': 6.01},
    '3': {'nome': 'Libra (GBP)', 'cotacao': 7.30},
    '4': {'nome': 'Quetzal Guatemalteco (GTQ)', 'cotacao': 0.71},
    '5': {'nome': 'Peso Cubano (CUC)', 'cotacao': 0.23}
}

def exibir_menu():
    print(f"\nEscolha uma moeda para conversão:\n")
    for codigo, info in cotacoes.items():
        print(f"{codigo} - {info['nome']} (R$ {info['cotacao']:.2f})")

def converter_moeda(valor_reais, cotacao):
    return valor_reais / cotacao

def main():
    while True:
        exibir_menu()
        
        escolha = input(f"\nDigite o número da moeda que deseja converter (ou 'sair' para encerrar): ")
        
        if escolha.lower() == 'sair':
            print(f"\nOperação encerrada.\n")
            break

        if escolha in cotacoes:
            valor_reais = float(input(f"\nDigite o valor em reais (R$): "))
            moeda_escolhida = cotacoes[escolha]['nome']
            cotacao = cotacoes[escolha]['cotacao']
            
            valor_convertido = converter_moeda(valor_reais, cotacao)
            print(f"\nR$ {valor_reais:.2f} equivalem a {valor_convertido:.2f} {moeda_escolhida}.\n")
        else:
            print(f"\nEscolha inválida. Tente novamente.")

main()