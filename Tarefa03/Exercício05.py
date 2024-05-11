# Curso Básico de Python
# Nome do Desenvolvedor: Victor Fregni Gogorza
# Versão1.0
# Exercício de lógica de programação utilizando a linguagem de programação Python

# Crie um programa que pergunte ao usuário a quantidade de dias, horas,
# minutos e segundos, e calcule o total em segundos.

dias = int(input("Insira ao lado a quantidade de dias"))
horas = int(input("Agora, insira a quantidade de horas"))
minutos = int(input("Agora, escreva a quantidade de minutos"))
segundos = int(input("Por último, a quantidade de segundos"))

diasSegundos = dias * 24 * 60 * 60
horasSegundos = horas * 60 * 60
minutosSegundos = minutos * 60
segundosTotais = diasSegundos + horasSegundos + minutosSegundos + segundos

print(dias, "dias,", horas, "horas,", minutos, "minutos, e",
      segundos, "segundos correspondem a", segundosTotais, "segundos")