#aqui é a parte da criação da função e suas variaveis
def calcular_imc(peso, altura):
#aqui define oque é imc, sendo peso dividido por altura ao quadrado
imc = peso / (altura ** 2)
return imc
#aqui é a criação de uma outra função com finalidade de classificar o resultado do imc
def classificar_imc(imc):
#aqui foi criado uma estrutura de condição para definir o imc
if imc < 18.5:
return "Abaixo do peso"
elif 18.5 <= imc < 24.9:
return "Peso normal"
elif 25 <= imc < 29.9:
return "Sobrepeso"
elif 30 <= imc < 34.9:
return "Obesidade grau 1"
elif 35 <= imc < 39.9:
return "Obesidade grau 2"
else:
return "Obesidade grau 3"
#nessa parte é uma outra função, que de acordo com o resultado obtido em classificação imc vai sujerir uma atividade fisica
def sugestao_atividade_fisica(classificacao_imc):
#Aqui é outra estrutura para retornar um resultado que é definido  de acordo com o resutado do imc
if classificacao_imc == "Abaixo do peso":
return "Sugere-se atividades de fortalecimento muscular, como musculação, e uma dieta rica em
proteínas e calorias."
elif classificacao_imc == "Peso normal":
return "Sugere-se a manutenção com atividades aeróbicas regulares, como caminhada, corrida leve e
natação, junto a um treino de força moderado."
elif classificacao_imc == "Sobrepeso":
return "Sugere-se atividades aeróbicas moderadas, como caminhada rápida, ciclismo e natação, além
de exercícios de resistência."
elif classificacao_imc == "Obesidade grau 1":
return "Sugere-se atividades de baixo impacto, como caminhadas, natação e hidroginástica, junto a um
programa de reeducação alimentar."
elif classificacao_imc == "Obesidade grau 2":
return "Sugere-se exercícios de baixo impacto com supervisão, como hidroginástica e pilates, e
acompanhamento nutricional."
else:
return "Sugere-se atividades físicas supervisionadas por profissionais de saúde, como hidroginástica,
fisioterapia, e consultas regulares com um nutricionista."
#aqui é onde o usuario digita seu peso e sua altura
peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura (em metros): "))
imc = calcular_imc(peso, altura)
classificacao_imc = classificar_imc(imc)
sugestao = sugestao_atividade_fisica(classificacao_imc)
#nessa parte é onde os resultados são printados para o usuario
print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao_imc}")
print(f"Sugestão de atividade física: {sugestao}")