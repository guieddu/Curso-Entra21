"""
Faça um programa que leia o salário de um trabalhador e o valor
da prestação de um empréstimo. Se a prestação for maior que 20%
do salário imprima: “empréstimo não concedido”, caso contrário
imprima: “empréstimo concedido”.
"""

salario = int(input("Digite o salário do trabalhador:"))
emprestimo = int(input("Digite o valor do empréstimo do trabalhador:"))

if emprestimo > salario * 0.2:
    print("Empréstimo não concedido")
else:
    print("Empréstimo concedido")