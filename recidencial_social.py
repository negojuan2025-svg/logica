def calcular_conta():
    try:
        # Lê o consumo de água informado pelo usuário
        consumo = float(input("Digite o consumo de água da residência (em m³): "))
        
        # Verifica se o consumo é válido (não negativo)
        if consumo < 0:
            print("Erro: O consumo não pode ser um valor negativo.")
            return

        # Calcula o valor baseado nas faixas informadas
        if consumo <= 10:
            valor_conta = 7.59  # Valor fixo
        elif consumo <= 20:
            valor_conta = consumo * 1.31
        elif consumo <= 30:
            valor_conta = consumo * 4.64
        elif consumo <= 50:
            valor_conta = consumo * 6.62
        else: # Acima de 50m³
            valor_conta = consumo * 7.31
            
        # Exibe o resultado formatado com duas casas decimais
        print(f"O valor da conta de água é: R$ {valor_conta:.2f}")

    except ValueError:
        print("Erro: Por favor, digite um número válido para o consumo.")

# Executa a função principal
if __name__ == "__main__":
    calcular_conta()