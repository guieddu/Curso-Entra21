altura = float(input("Informe sua altura em metros: "))
peso = float(input("Informe seu peso em kg: "))
IMC = peso/(altura**2)

print(f"Seu indice de massa corporal é {IMC:.2f}")

if IMC < 18.5:
    print("Abaixo do peso")
elif IMC > 18.5 and IMC < 24.9:
    print("Peso normal")
elif IMC > 25 and IMC < 29.9:
    print("Sobrepeso")
elif IMC > 30 and IMC < 34.9:
    print("Obesidade grau 1")
elif IMC > 35 and IMC < 39.9:
    print("Obesidade grau 2")
else:
    IMC >= 40
    print("Obesidade grau 3")

