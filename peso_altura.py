def calcular_imc():
    try:
        # Lê o peso e a altura informados pelo usuário
        peso = float(input("Digite o seu peso (em kg): "))
        altura = float(input("Digite a sua altura (em metros, ex: 1.75): "))
        
        # Verifica se os valores são válidos
        if peso <= 0 or altura <= 0:
            print("Erro: Peso e altura devem ser maiores que zero.")
            return

        # Calcula o IMC (peso dividido pela altura ao quadrado)
        imc = peso / (altura ** 2)
        
        # Determina a classificação com base na tabela
        if imc < 16:
            classificacao = "Magreza grave"
        elif imc < 17:
            classificacao = "Magreza moderada"
        elif imc < 18.5:
            classificacao = "Magreza leve"
        elif imc < 25:
            classificacao = "Saudável"
        elif imc < 30:
            classificacao = "Sobrepeso"
        elif imc < 35:
            classificacao = "Obesidade Grau I"
        elif imc < 40:
            classificacao = "Obesidade Grau II (severa)"
        else: # Maior ou igual a 40
            classificacao = "Obesidade Grau III (mórbida)"
            
        # Exibe o IMC formatado com duas casas decimais e a sua classificação
        print(f"\nSeu IMC é: {imc:.2f}")
        print(f"Classificação: {classificacao}")

    except ValueError:
        print("Erro: Por favor, digite valores numéricos válidos (use ponto para casas decimais).")

# Executa a função principal
if __name__ == "__main__":
    calcular_imc()