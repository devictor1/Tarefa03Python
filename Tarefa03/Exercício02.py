# Curso Básico de Python
# Nome do Desenvolvedor: Victor Fregni Gogorza
# Versão1.0
# Exercício de lógica de programação utilizando a linguagem de programação Python

# Crie um programa que solicite ao usuário sua altura e peso, e calcule seu índice de massa corporal (IMC).

peso = float(input("Insira o seu peso"))
altura = float(input("Insira agora a sua altura"))
imc = peso/(altura*altura)
print("O seu índice de massa corporal é", round(imc, 2))