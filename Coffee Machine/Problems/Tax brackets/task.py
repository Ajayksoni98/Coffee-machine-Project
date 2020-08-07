income = int(input())

def result(y,percent):
    print(f"The tax for {income} is {percent}%. That is {round(y)} dollars!")



if 0 <= income <= 15527:
    calculated_tax = 0
    percent = 0
    result(calculated_tax,percent)
elif 15528 <= income <= 42707:
    calculated_tax = income * 0.15
    percent = 15
    result(calculated_tax,percent)
elif 42708 <= income <= 132406:
    calculated_tax = income * 0.25
    percent = 25
    result(calculated_tax,percent)
else:
    calculated_tax = income * 0.28
    percent = 28
    result(calculated_tax,percent)


