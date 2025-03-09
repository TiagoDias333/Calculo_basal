from time import sleep
peso = float(input("Digite seu peso:[kg] "))
altura = int(input("Digite sua altura:[cm] "))
idade = int(input("Digite sua idade: "))
basal = (10*peso)+(6.25*altura)-(5.0*idade)
print("CALCULANDO......")
sleep(1)
print(f'Seu metabolismo basal está em \33[93m{basal}\33[m calorias.')
