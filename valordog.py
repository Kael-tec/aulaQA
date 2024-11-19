def calcularIdadePet ():
    nome_Pet = str(input("Qual o nome do seu Pet: "))
    idade_Pet = int(input("Qual a idade do seu cachorro: "))
    porte_Pet = int(input("Qual o tamanho dele caso seja grande porte digite 1, caso seja médio porte digite 2, e pequeno porte digite 3: "))
    quantiaBanho = int(input("E quantas vezes nos últimos 12 meses ele tomou banho? ")) 
    
    if porte_Pet == 1: print(input(f"Olá, a idade humana do {nome_Pet} é {idade_Pet * 7} e nos últimos 12 meses o lucro com este animal foi de R${quantiaBanho*(75-20)}."))
    elif porte_Pet == 2: print(input(f"Olá, a idade humana do {nome_Pet} é {idade_Pet * 7} e nos últimos 12 meses o lucro com este animal foi de R${quantiaBanho*(60-15)}. "))
    elif porte_Pet == 3: print(input(f"Olá, a idade humana do {nome_Pet} é {idade_Pet * 7} e nos últimos 12 meses o lucro com este animal foi de R${quantiaBanho*(50-5)}."))

calcularIdadePet()