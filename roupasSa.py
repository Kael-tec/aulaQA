nome = input("Qual o seu nome?")
mes = "Janeiro"
valor_compra = 500
desconto = 10
cupom = "PAULAÉ10"

print("Olá, " + nome + " em " + mes +" voce realizou uma compra no valor de "+ str(valor_compra) + " e ganhou um desconto de "+ str(desconto) +"% em sua proxima compra. Use o cupom. " + cupom )

valor_compra = 500
desconto = 10

porcentagem_desconto = (valor_compra*desconto)/100
print(f"E sua compra após o desconto e de R${valor_compra - porcentagem_desconto}")
print(f"O valor original da compra é R${valor_compra}. Com um desconto de {desconto}%, o preço final é R${valor_compra * (1 - desconto / 100):.2f}.")
