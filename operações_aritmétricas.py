def executar_calculadora():
    try:
        # Lê os dois números
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        # Exibe o menu de opções
        print("\nEscolha a operação:")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Potência")
        print("6 - Raiz quadrada")
        print("7 - Número par")
        print("8 - Número ímpar")
        
        opcao = int(input("\nDigite a opção desejada (1-8): "))
        
        # Estrutura condicional para executar a operação escolhida
        if opcao == 1:
            resultado = num1 + num2
            print(f"Resultado da Adição: {resultado}")
            
        elif opcao == 2:
            resultado = num1 - num2
            print(f"Resultado da Subtração: {resultado}")
            
        elif opcao == 3:
            resultado = num1 * num2
            print(f"Resultado da Multiplicação: {resultado}")
            
        elif opcao == 4:
            if num2 == 0:
                print("Erro: Não é possível dividir um número por zero.")
            else:
                resultado = num1 / num2
                print(f"Resultado da Divisão: {resultado}")
                
        elif opcao == 5:
            # num1 elevado a num2
            resultado = num1 ** num2
            print(f"Resultado da Potência ({num1} elevado a {num2}): {resultado}")
            
        elif opcao == 6:
            # Verifica a raiz quadrada para os dois números
            # Não podemos calcular raiz real de números negativos
            if num1 >= 0:
                print(f"A raiz quadrada de {num1} é {num1 ** 0.5:.2f}")
            else:
                print(f"Erro: Não há raiz quadrada real para {num1}.")
                
            if num2 >= 0:
                print(f"A raiz quadrada de {num2} é {num2 ** 0.5:.2f}")
            else:
                print(f"Erro: Não há raiz quadrada real para {num2}.")
                
        elif opcao == 7:
            # Verifica se o resto da divisão por 2 é igual a zero
            print(f"O número {num1} é Par? {'Sim' if num1 % 2 == 0 else 'Não'}")
            print(f"O número {num2} é Par? {'Sim' if num2 % 2 == 0 else 'Não'}")
            
        elif opcao == 8:
            # Verifica se o resto da divisão por 2 é diferente de zero
            print(f"O número {num1} é Ímpar? {'Sim' if num1 % 2 != 0 else 'Não'}")
            print(f"O número {num2} é Ímpar? {'Sim' if num2 % 2 != 0 else 'Não'}")
            
        else:
            print("Opção inválida!")

    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite apenas números válidos.")

# Executa a função principal
if __name__ == "__main__":
    executar_calculadora()