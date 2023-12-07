from datetime import datetime

dia_nascimento = input("Qual o dia do seu nascimento? ")

while (
    len(dia_nascimento) > 2
    or not dia_nascimento.isdigit()
    or int(dia_nascimento) > 31
    or int(dia_nascimento) <= 0
):
    print(
        "O dia do nascimento não contém no máximo 2 numerais ou a data está incorreta, tente novamente."
    )
    dia_nascimento = input("Qual o dia do seu nascimento? ")

mes_nascimento = input("Qual o mês do seu nascimento? ")

while (
    len(mes_nascimento) > 2
    or not mes_nascimento.isdigit
    or int(mes_nascimento) > 12
    or int(mes_nascimento) <= 0
):
    print(
        "O mês de nascimento não contém no máximo 2 numerais ou a data está incorreta, tente novamente."
    )
    mes_nascimento = input("Qual o mês do seu nascimento? ")

ano_nascimento = input("Qual o ano do seu nascimento? ")

while len(ano_nascimento) != 4 or not ano_nascimento.isdigit():
    print(
        "O ano do nascimento precisa conter exatamente 4 numerais, a data está incorreta tente novamente."
    )
    ano_nascimento = input("Qual o ano do seu nascimento? ")

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
    faltam_dias = datetime(
        year=int(datetime.now().strftime("%Y")) + 1,
        month=nascimento.month,
        day=nascimento.day,
    )
    faltam_dias = faltam_dias - datetime.now()
else:
    faltam_dias = datetime(
        year=int(datetime.now().strftime("%Y")),
        month=nascimento.month,
        day=nascimento.day,
    )
    faltam_dias = faltam_dias - datetime.now()

if not fezniver():
    idade_user -= 1

if faltam_dias.days == 0:
    print(
        f"Você tem {idade_user} anos e falta {faltam_dias.days + 1} dia para seu aniversário!"
    )
else:
    print(
        f"Você tem {idade_user} anos e faltam {faltam_dias.days + 1} dias para seu aniversário!"
    )
print(f"Sua data de nascimento é: {nascimento.strftime('%d/%m/%Y')}")
print(f"A data de hoje é: {datetime.now().strftime('%d/%m/%Y')}")
