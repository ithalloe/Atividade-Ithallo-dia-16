# coding=utf-8
#Nessa primeira parte foi criada a função e suas variaveis.
def calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso):
#Aqui a foi dado um valor para taxa juros diaria, no qual é a porcentagem por dia da taxa juros anual
taxa_juros_diaria = taxa_juros_anual / 365 / 100
#Aqui foi dado um valor para juros, no qual é a multiplicação do valor inicial, taxa de juros diaria e os dias de atraso.
juros = valor_principal * taxa_juros_diaria * dias_atraso
#Aqui foi definido o valor da variavel valor total, que se da pela soma do valor inicial e juros
valor_total = valor_principal + juros
return valor_total, juros
#Nessa parte foram dados os valores para as variaveis valor principal,taxa juros anual e dias atraso.
valor_principal = 1000.00
taxa_juros_anual = 5.0
dias_atraso = 30
valor_total, juros = calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso)
#Essa parte Printa o valor a ser pago, e os valores dos juros.
print(f"Valor total a ser pago: R${valor_total:.2f}")
print(f"Valor dos juros: R${juros:.2f}")