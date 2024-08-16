# coding=utf-8
#Aqui foi criado uma função
def calcular_area_comodos():
#Aqui foi inicializado total area com o valor 0
total_area = 0
while True:
#Aqui foi dado dois input para o usuario digitar a largura e o comprimento
largura = float(input("Digite a largura do cômodo (em metros): "))
comprimento = float(input("Digite o comprimento do cômodo (em metros): "))
#Aqui foi dado o valor para area comodo, que é o resultado da multiplicação da largura e comprimento
area_comodo = largura * comprimento

#Aqui é parte que mostra ao usuario a area
print(f"A área deste cômodo é: {area_comodo:.2f} metros quadrados.")


total_area += area_comodo
#aqui é dado um novo input, é a parte que define se o codigo ira continuar rodando ou vai parar
mais_comodos = input("Deseja adicionar mais cômodos? (s/n): ").strip().lower()
if mais_comodos != 's':
break

return total_area
area_total = calcular_area_comodos()

#Aqui mostra ao usuario a area total de todos os comodos que ele colocou
print(f"A área total da casa é: {area_total:.2f} metros quadrados.")