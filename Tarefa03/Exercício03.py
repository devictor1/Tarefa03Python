# Curso Básico de Python
# Nome do Desenvolvedor: Victor Fregni Gogorza
# Versão1.0
# Exercício de lógica de programação utilizando a linguagem de programação Python

# Faça um programa que pergunte ao usuário o valor do produto e o percentual de
# desconto, e retorne o valor final após o desconto.

valorProduto = float(input("Qual o valor do produto?"))
percentualDesconto = float(input("E qual a porcentagem de desconto nele?"))
desconto = (percentualDesconto/100)*valorProduto
valorFinal = valorProduto - desconto
print("O valor final do seu produto é", round(valorFinal, 2))