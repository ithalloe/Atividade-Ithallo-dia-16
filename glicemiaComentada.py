# coding=utf-8
#Aqui é criado uma função e suas variaveis
def diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial):
#Aqui foi criado uma estrutura de condição para retornar os valores diabetes, pre diabetes e normal
if glicemia_em_jejum >= 126 or glicemia_pos_prandial >= 200:
return "Diabetes"
elif 100 <= glicemia_em_jejum < 126 or 140 <= glicemia_pos_prandial < 200:
return "Pré-diabetes"
else:
return "Normal"
#Aqui são dados dois inputs recebendo as informações que vao definir o valor de glicemia em jejum e glicemia pos prandial
glicemia_em_jejum = float(input("Digite o valor da glicemia em jejum (mg/dL): "))
glicemia_pos_prandial = float(input("Digite o valor da glicemia pós-prandial (mg/dL): "))
resultado = diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial)
#Essa parte é onde o usuario ve o resultado de seu diagnostico
print(f"O diagnóstico é: {resultado}")