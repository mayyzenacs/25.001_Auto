

def calc(option, value, percent= 25.001):
        if option == 1: 
            valor_final = float(value)
            percent = float(percent)
            de_por = percent * valor_final / 100
            var = de_por + valor_final
            print(f"{var:.2f}")
        else:
            print("20")


# codigo antigo abaixo

"""
#o preço que queremos + 25,000%

def price(valor, porcentagem=25.001):
    valor_final = float(valor)
    porcentagem = float(porcentagem)
    de_por = porcentagem * valor_final / 100
    return de_por + valor_final

def checador(valorx, entrada):
    if valorx != entrada:
        return print(f"=> {valorx + 0.01:.2f}")
    else:
        pass

entrada = input("Valor ").replace(",",".")
resultado = price(entrada)
checador(resultado, entrada)
print(f"=> {resultado:.2f}")
"""
        