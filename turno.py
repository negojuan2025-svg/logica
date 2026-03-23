def saudacao_turno():
    # Exibe a instrução e lê o turno informado pelo usuário
    print("Em que turno você estuda?")
    turno = input("Digite M-Matutino, V-Vespertino ou N-Noturno: ")
    
    # Verifica a letra digitada e exibe a mensagem correspondente
    # A validação é estrita (case-sensitive), aceitando apenas maiúsculas
    if turno == 'M':
        print("Bom Dia!")
    elif turno == 'V':
        print("Boa Tarde!")
    elif turno == 'N':
        print("Boa Noite!")
    else:
        # Captura qualquer coisa que não seja exatamente 'M', 'V' ou 'N'
        print("Valor Inválido!")

# Executa a função principal
if __name__ == "__main__":
    saudacao_turno()