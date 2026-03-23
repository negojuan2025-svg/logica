def calcular_boletim():
    try:
        # Lê as quatro notas bimestrais
        nota1 = float(input("Digite a 1ª nota: "))
        nota2 = float(input("Digite a 2ª nota: "))
        nota3 = float(input("Digite a 3ª nota: "))
        nota4 = float(input("Digite a 4ª nota: "))
        
        # Validação simples para garantir que as notas não sejam negativas
        if nota1 < 0 or nota2 < 0 or nota3 < 0 or nota4 < 0:
            print("Erro: As notas não podem ser negativas.")
            return

        # Calcula a média aritmética
        media = (nota1 + nota2 + nota3 + nota4) / 4
        
        # Determina o conceito com base na média
        # Como o Python lê de cima para baixo, começamos da maior nota para a menor
        if media >= 9.0:
            conceito = "A"
        elif media >= 7.5:
            conceito = "B"
        elif media >= 6.0:
            conceito = "C"
        elif media >= 4.0:
            conceito = "D"
        else: # Média menor que 4.0
            conceito = "E"
            
        # Verifica a situação de aprovação com base no conceito
        if conceito in ["A", "B", "C"]:
            situacao = "APROVADO"
        else: # Se for D ou E
            situacao = "REPROVADO"
            
        # Exibe o boletim completo formatado
        print("\n--- Boletim Final ---")
        print(f"Notas Bimestrais: {nota1:.1f} | {nota2:.1f} | {nota3:.1f} | {nota4:.1f}")
        print(f"Média Final     : {media:.2f}")
        print(f"Conceito        : {conceito}")
        print(f"Situação        : {situacao}")
        print("---------------------")

    except ValueError:
        print("Erro: Por favor, digite apenas números válidos para as notas.")

# Executa a função principal
if __name__ == "__main__":
    calcular_boletim()
