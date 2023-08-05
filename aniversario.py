from datetime import datetime

def checagem_int(data):
    try:
        data = int(data)
        return True
    except ValueError:
        return False

dia_nascimento = (input("Qual o dia do seu nascimento? "))

while len(dia_nascimento) != 2 or not checagem_int(dia_nascimento):
     print("O dia do nascimento pode conter apenas 2 numerais, tente novamente.")
     dia_nascimento = (input("Qual o dia do seu nascimento? "))

mes_nascimento = (input("Qual o mês do seu nascimento? "))

while len(mes_nascimento) != 2 or not checagem_int(mes_nascimento):
     print("O mês de nascimento pode conter apenas 2 numerais, tente novamente.")
     mes_nascimento = (input("Qual o mês do seu nascimento? "))

ano_nascimento = (input("Qual o ano do seu nascimento? "))

while len(ano_nascimento) != 4 or not checagem_int(ano_nascimento):
     print("O ano do nascimento pode conter apenas 4 numerais, tente novamente.")
     ano_nascimento = (input("Qual o ano do seu nascimento? "))

dia_nascimento = int(dia_nascimento)
mes_nascimento = int(mes_nascimento)
ano_nascimento = int(ano_nascimento)

nascimento = datetime(ano_nascimento, mes_nascimento, dia_nascimento)

idade_user = datetime.now().year - nascimento.year

def fezniver():
    if mes_nascimento > datetime.now().month:
         return False
    elif mes_nascimento == datetime.now().month and dia_nascimento > datetime.now().day:
         return False
    return True

if fezniver():
    faltam_dias = datetime(year=int(datetime.now().strftime("%Y"))+1, month=nascimento.month, day=nascimento.day)
    faltam_dias = faltam_dias - datetime.now()
else:
    faltam_dias = datetime(year=int(datetime.now().strftime("%Y")), month=nascimento.month, day=nascimento.day)
    faltam_dias = faltam_dias - datetime.now()

if mes_nascimento > datetime.now().month:
    idade_user -= 1
elif mes_nascimento == datetime.now().month and dia_nascimento > datetime.now().day:
        idade_user -= 1

print(f"Você tem {idade_user} anos e faltam {faltam_dias.days} dias para seu aniversário!")
print(f"Sua data de nascimento é: {nascimento.strftime('%d/%m/%Y')}")
print(f"A data de hoje é: {datetime.now().strftime('%d/%m/%Y')}")