nome = input("Identifique-se! Qual é o seu nome? ")
idade = int(input("E qual a sua idade? "))
nomevo = input("Nome da vó é bom falar também hehe: ")

idade_futura = idade + 5

resposta = input(f"Daqui a 5 anos você terá {idade_futura} anos. Sabia que essa é considerada uma idade comum para ter filho? ")

if resposta == "Sim":
 print ("Então se prepare kkkkkk")
 if resposta == "Não":
  print ("Dá pra aproveitar bastante se é que me entende hehe")
print(f"Olá {nome}, bom saber que você tem {idade} anos.")
print(f"A {nomevo} não deve ser tão novinha assim rsrs.")