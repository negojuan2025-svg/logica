def calcular_reajuste():
    try:
        # Lê o salário atual do funcionário
        salario_atual = float(input("Digite o salário atual do funcionário (R$): "))
        
        # Verifica se o valor é válido
        if salario_atual <= 0:
            print("Erro: O salário deve ser um valor maior que zero.")
            return

        # Determina o percentual de aumento baseado nas faixas salariais
        if salario_atual <= 1000.00:
            percentual = 20
        elif salario_atual <= 1700.00:
            percentual = 15
        elif salario_atual <= 2300.00:
            percentual = 10
        else: # Acima de R$ 2.300,00
            percentual = 5
            
        # Calcula o valor do aumento e o novo salário
        valor_aumento = salario_atual * (percentual / 100)
        novo_salario = salario_atual + valor_aumento
        
        # Exibe os resultados formatados na tela
        print("\n--- Resumo do Reajuste ---")
        print(f"Salário digitado: R$ {salario_atual:.2f}")
        print(f"Aumento         : {percentual}%")
        print(f"Valor do aumento: R$ {valor_aumento:.2f}")
        print(f"Novo salário    : R$ {novo_salario:.2f}")

    except ValueError:
        print("Erro: Por favor, digite um valor numérico válido para o salário.")

# Executa a função principal
if __name__ == "__main__":
    calcular_reajuste()