#Projeto HEALTH TRACK. Inserir Peso, altura e calculo IMC.

peso = float(input('Informe seu peso aqui, por favor:'))
altura = float(input('Agora, nos diga qual sua altura:'))
imc = float(peso) / (altura * altura)

if imc <= 16.00:
    print('Baixo peso grau III')

elif (imc >= 16.00) and (imc <= 16.00):
    print('Baixo peso grau II')
elif (imc >= 17.00) and (imc <= 18.49):
    print('Baixo peso grau I')
elif (imc >= 18.50) and (imc <= 24.99):
    print('Peso ideal')
elif (imc >= 25.00) and (imc <= 29.99):
    print('Sobrepeso')
elif (imc >= 30.00) and (imc <= 34.99):
    print('Obesidade grau I')
elif (imc >= 35.00) and (imc <= 39.99):
    print('Obesidade grau II')
elif imc >= 40.00:
    print('Obesidade grau III')