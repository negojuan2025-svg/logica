def exibir_menu():
    # Exibe as opções na tela para o usuário
    print("1 - Opção 1")
    print("2 - Opção 2")
    print("3 - Opção 3")
    print("4 - Sair")
    
    try:
        # Lê a opção escolhida pelo usuário
        opcao = int(input("Digite uma opção: "))
        
        # Verifica qual foi a opção digitada e exibe a mensagem correspondente
        if opcao == 1:
            print("Você selecionou a opção 1")
        elif opcao == 2:
            print("Você selecionou a opção 2")
        elif opcao == 3:
            print("Você selecionou a opção 3")
        elif opcao == 4:
            print("Você selecionou sair")
        else:
            # Captura qualquer número que não seja 1, 2, 3 ou 4
            print("Opção inválida!!!")
            
    except ValueError:
        # Captura o erro caso o usuário digite texto ou símbolos ao invés de um número
        print("Opção inválida!!!")
        
    # Esta linha é executada independentemente da opção escolhida, 
    # pois está fora do bloco if/elif/else e do try/except
    print("Fim do programa!")

# Executa a função principal
if __name__ == "__main__":
    exibir_menu()