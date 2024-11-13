nome = input("Qual o seu nome?")
mes = input("Qual foi o mes da compra?")
valor_compra = 500
desconto = 10
cupom = "PAULAÉ10"

print("Olá, " + nome + ", em " + mes +" voce realizou uma compra no valor de "+ str(valor_compra) + " e ganhou um desconto de "+ str(desconto) +"% em sua proxima compra. Use o cupom. " + cupom )

valor_compra = 500
desconto = 10

porcentagem_desconto = (valor_compra*desconto)/100
print(f"O valor original da compra é R${valor_compra}. Com um desconto de {desconto}%, o preço final é R${valor_compra * (1 - desconto / 100):.2f}.")
print(f"espero que goste do seu desconto e do valor de R${valor_compra - porcentagem_desconto}" "da sua compra, Boa tarde.")