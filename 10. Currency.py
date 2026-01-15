# Write code below 💖

PESOS_TO_USD = 0.00027
SOLES_TO_USD = 0.3
REAIS_TO_USD = 0.19

try:
    pesos = float(input('What do you have left in pesos? '))
    soles = float(input('What do you have left in soles? '))
    reais = float(input('What do you have left in reais? '))

    dollars = pesos * PESOS_TO_USD + soles * SOLES_TO_USD + reais * REAIS_TO_USD
    print(f"Total in US dollars: ${dollars:.1f}")

except ValueError:
    print("错误：请输入有效的数字")