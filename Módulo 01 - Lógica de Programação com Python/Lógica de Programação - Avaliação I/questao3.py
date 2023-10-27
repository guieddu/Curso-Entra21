ano = int(input("Digite o ano: "))

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
             print("O ano é bissexto (tem 366 dias)")
        else:
            print("O ano não é bissexto (tem 365 dias)")
    else:
        print("O ano é bissexto (tem 366 dias)")
else:
    print("O ano não é bissexto (tem 365 dias)")
