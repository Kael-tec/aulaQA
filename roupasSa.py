nome = "Paula Martins"
mes = "Janeiro"
valor_compra = 500
desconto = 10
cupom = "PAULAÉ10"

print("Olá, " + nome + " em " + mes +" voce realizou uma compra no valor de "+ str(valor_compra) + " e ganhou um desconto de "+ str(desconto) +" em sua proxima compra. Use o cupom " + cupom )

valor_compra = 500
desconto = 10 

porcentagem_desconto = (valor_compra*desconto)/100
print(f"Sua compra após o desconto E de R${valor_compra - porcentagem_desconto}")