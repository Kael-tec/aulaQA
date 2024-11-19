def verificar_time(matricula):
    
# Verifica se a matrícula é par ou ímpar\ O símbolo `%` é o operador de módulo. Ele retorna o *resto* da divisão entre dois números.
    if matricula % 2 == 0:
        print("VOCÊ ESTÁ NO TIME AZUL")
    else:
        print("VOCÊ ESTÁ NO TIME AMARELO")

# Exemplo de uso:
numero_matricula = int(input("Digite o número de matrícula: "))
verificar_time(numero_matricula)