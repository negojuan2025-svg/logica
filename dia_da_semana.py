def mostrar_dia_semana():
    try:
        # Lê o número informado pelo usuário
        numero = int(input("Digite um número de 1 a 7: "))
        
        # Verifica qual dia corresponde ao número
        if numero == 1:
            print("Domingo")
        elif numero == 2:
            print("Segunda")
        elif numero == 3:
            print("Terça")
        elif numero == 4:
            print("Quarta")
        elif numero == 5:
            print("Quinta")
        elif numero == 6:
            print("Sexta")
        elif numero == 7:
            print("Sábado")
        else:
            # Captura qualquer número fora do intervalo 1-7
            print("Opção inválida!")

    except ValueError:
        # Captura o erro caso o usuário digite letras ou símbolos ao invés de um número
        print("Opção inválida!")

# Executa a função principal
if __name__ == "__main__":
    mostrar_dia_semana()