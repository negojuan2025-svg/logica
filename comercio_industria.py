def calcular_conta_comercial():
    try:
        # Lê o consumo de água informado pelo usuário
        consumo = float(input("Digite o consumo de água do prédio (em m³): "))
        
        # Verifica se o consumo é válido (não negativo)
        if consumo < 0:
            print("Erro: O consumo não pode ser um valor negativo.")
            return

        # Calcula o valor baseado nas faixas comerciais/industriais
        if consumo <= 10:
            valor_conta = 44.95  # Valor fixo
        elif consumo <= 20:
            valor_conta = consumo * 8.75
        elif consumo <= 50:
            valor_conta = consumo * 16.76
        else: # Acima de 50m³
            valor_conta = consumo * 17.46
            
        # Exibe o resultado formatado com duas casas decimais
        print(f"O valor da conta de água é: R$ {valor_conta:.2f}")

    except ValueError:
        print("Erro: Por favor, digite um número válido para o consumo.")

# Executa a função principal
if __name__ == "__main__":
    calcular_conta_comercial()