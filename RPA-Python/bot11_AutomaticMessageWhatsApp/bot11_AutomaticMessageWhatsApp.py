import pywhatkit

# O número deve conter +55 DDD 99999 - 9999
number_list = ['+5516999999999']

# Insira sua mensagem
message = "Olá, boa noite! Está é uma mensagem enviada pelo PyWhatKit :)"

# A ordem dos parametros são: número, mensagem e por fim o horário, exemplo: 19(horas), 15(minutos).
for numero in number_list:
    pywhatkit.sendwhatmsg(numero, message, 19,15) # A ordem dos parametros são: número, mensagem e por fim