# Questão 09:

dias = int(input('Informe a quantidade de dias:'))
horas = int(input('Informe a quantidade as horas:'))
minu = int(input('Informe a quantidade de minutos:'))
sec = int(input('Informe a quantidade de segundos:'))

total = (dias * 86400) + (horas * 3600) + (minu * 60) + sec

print ('O total em segundos é:', total)
