def calcular_impostos_salario():
    try:
        # Lê o salário bruto informado
        salario_bruto = float(input("Digite o valor do salário bruto (R$): "))
        
        if salario_bruto <= 0:
            print("Erro: O salário deve ser maior que zero.")
            return

        # ---------------------------------------------------------
        # 1. CÁLCULO DO INSS (Tabela 2023 - Progressivo)
        # ---------------------------------------------------------
        inss = 0
        if salario_bruto <= 1320.00:
            inss = salario_bruto * 0.075
        elif salario_bruto <= 2571.29:
            inss = (1320.00 * 0.075) + ((salario_bruto - 1320.00) * 0.09)
        elif salario_bruto <= 3856.94:
            inss = (1320.00 * 0.075) + ((2571.29 - 1320.00) * 0.09) + ((salario_bruto - 2571.29) * 0.12)
        elif salario_bruto <= 7507.49:
            inss = (1320.00 * 0.075) + ((2571.29 - 1320.00) * 0.09) + ((3856.94 - 2571.29) * 0.12) + ((salario_bruto - 3856.94) * 0.14)
        else:
            # Se passar de 7.507,49, o desconto atinge o Teto máximo do INSS
            inss = 876.95 

        # ---------------------------------------------------------
        # 2. CÁLCULO DO IRRF (Tabela 2023)
        # A base de cálculo do IRRF é o salário bruto MENOS o INSS
        # ---------------------------------------------------------
        base_irrf = salario_bruto - inss
        irrf = 0

        if base_irrf <= 2112.00:
            irrf = 0.0  # Isento
        elif base_irrf <= 2826.65:
            irrf = (base_irrf * 0.075) - 158.40
        elif base_irrf <= 3751.05:
            irrf = (base_irrf * 0.15) - 370.40
        elif base_irrf <= 4664.68:
            irrf = (base_irrf * 0.225) - 651.73
        else:
            irrf = (base_irrf * 0.275) - 884.96

        # Garante que o IRRF não fique negativo caso a dedução seja maior que o imposto calculado
        if irrf < 0:
            irrf = 0.0

        # ---------------------------------------------------------
        # 3. RESULTADO
        # ---------------------------------------------------------
        salario_liquido = salario_bruto - inss - irrf

        print("\n--- Holerite Simulado ---")
        print(f"Salário Bruto:   R$ {salario_bruto:.2f}")
        print(f"(-) Desconto INSS: R$ {inss:.2f}")
        print(f"(-) Desconto IRRF: R$ {irrf:.2f}")
        print("-------------------------")
        print(f"Salário Líquido: R$ {salario_liquido:.2f}")

    except ValueError:
        print("Erro: Por favor, digite um valor numérico válido (use ponto para centavos).")

# Executa a função principal
if __name__ == "__main__":
    calcular_impostos_salario()