# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

print("\nSelecione o numero da operacao desejada:")

print("\n1 - Soma")
print("2 - Subtracao")
print("3 - Multiplicacao")
print("4 - Divisao")

opcao = int(input("\nDigite sua opcao (1/2/3/4): "))
if ( opcao < 1 or opcao > 4):
	print("opcao escolhida %s e invalida" %(opcao))
else:
	numero1 = int(input("\nDigite o primeiro numero: "))
	numero2 = int(input("\nDigite o segundo numero: "))
	resultado = 0
	operacao = ""
	if ( opcao == 1 ):
		resultado = numero1 + numero2
		operacao = "+"
	elif( opcao == 2 ):
		resultado = numero1 - numero2
		operacao = "-"
	elif( opcao == 3 ):
		resultado = numero1 * numero2
		operacao = "*"
	else:
		resultado = numero1 / numero2
		operacao = "/"
	print ("\n\n%s %s %s = %s\n\n" %(numero1,operacao,numero2,resultado))
