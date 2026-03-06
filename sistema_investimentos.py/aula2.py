print ("CHECKOUT PARA INVESTIMENTO!")
participar = input ("Gostaria de realizar um investimento de acordo com a sua renda mensal?: ").lower()
if participar == "sim":
    print ("Ótimo, vamos realizar o seu cadastro!")
elif participar == "talvez":
    print ("Em caso de duvidas contatar a central de investimentos.")
    exit() 
else:
    print ("Ok, se futuramente houver interresse estaremos de portas abertas! :)")
    exit()

print ("Você está sendo redirecionado(a) para a central de cadastros!")
nome = input ("Central de Cadastros: Olá, por favor insira seu nome Completo: ")
print ("Perfeito!")
apelido = input ("Central de Cadastros: Me diga como gostaria de  ser chamado(a) durante o atendimento: ")
print (f"Perfeito!, {apelido}, daremos continuidade...")
idade = input (f"Central de Cadastros: Por favor {apelido} insira sua idade: ")
print (f"Perfeito, {apelido} quase lá")
empresa = input (f"Central de Cadastros: {apelido}, em qual empresa você trabalha atualmente ou já trabalhou?: ")
print (f"Ótimo {apelido}, falta pouco...")
renda = float(input(f"Central de Cadastros: Agora, {apelido}, Qual é a sua renda mensal?: "))
if renda >= 2000:
    print (f"Perfeito {apelido}, agora posso te redirecionar para a equipe de investimentos Premium! É um prazer investir com você!<3 ")
    exit()
elif renda >= 1500:
    print (f"Perfeito {apelido}, agora posso te redirecionar para a equipe de investimentos Standart! É um prazer investir com você!<3 ")
    exit()
else:
    print (f"Perfeito {apelido}, agora posso te redirecionar para a equipe de investimentos Basics! É um prazer investir com você!<3 ")
    exit()