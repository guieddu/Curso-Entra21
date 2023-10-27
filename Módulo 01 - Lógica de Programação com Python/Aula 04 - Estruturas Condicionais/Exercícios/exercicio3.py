"""
Escreva um programa que receba um número, se esse número for ímpar,
 mostre na tela o quadrado do número digitado. No final do
 programa mostre na tela a mensagem: “Programa finalizado…”.
"""
numero = int(input("Digite um número:"))

if numero % 2 != 0:
    quadrado = numero ** 2
    print(f"O número é ímpar,e o quadrado dele é: {quadrado}")
else:
    print("O número é par")

print("Programa finalizado")