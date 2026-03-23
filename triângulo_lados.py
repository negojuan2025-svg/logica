def classificar_triangulo():
    try:
        # Lê os três lados informados pelo usuário
        lado1 = float(input("Digite o valor do primeiro lado: "))
        lado2 = float(input("Digite o valor do segundo lado: "))
        lado3 = float(input("Digite o valor do terceiro lado: "))
        
        # Verifica se os valores são maiores que zero (lados negativos não existem na geometria)
        if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
            print("Erro: Os lados do triângulo devem ser maiores que zero.")
            return

        # Verifica a condição de existência de um triângulo
        # A soma de dois lados deve ser sempre maior que o terceiro lado
        if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
            print("\nOs valores informados PODEM formar um triângulo!")
            
            # Classifica o triângulo
            if lado1 == lado2 == lado3:
                print("Classificação: Triângulo Equilátero (três lados iguais)")
            elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
                print("Classificação: Triângulo Isósceles (dois lados iguais)")
            else:
                print("Classificação: Triângulo Escaleno (três lados diferentes)")
                
        else:
            print("\nOs valores informados NÃO podem formar um triângulo.")

    except ValueError:
        print("Erro: Por favor, digite valores numéricos válidos.")

# Executa a função principal
if __name__ == "__main__":
    classificar_triangulo()