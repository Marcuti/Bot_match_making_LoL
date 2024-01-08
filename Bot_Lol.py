import pyautogui
from time import sleep
from pyautogui import *
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText




def click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()
    
def check_screen():
    #check up da tela para encontrar a imagem
    try:
        img = pyautogui.locateOnScreen(r"C:\\Users\\marcu\\Desktop\\Bot_Lol\\img\\aceitar.png", confidence=0.7)
        if img:
            aceitarx, aceitary = pyautogui.center(img)
            pyautogui.click(aceitarx, aceitary)
            return True
    except Exception:
        pass
    return False

    #envio de e-mail após a confirmação do click
def send_email(receiver_email):
    if len(receiver_email) == 0:
        return

    SENDER_EMAIL = "" #seu e-mail
    PASSWORD = "" #sua senha
    MESSAGE = "Sua fila no league of legends foi aceita!"

    msg = MIMEMultipart()
         
    msg['From'] = SENDER_EMAIL
    msg['To'] = receiver_email
    msg['Subject'] = "League Of Legends - Partida Encontrada"
     
    msg.attach(MIMEText(MESSAGE, 'plain'))
 
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.ehlo()  
            server.starttls(context=context)
            server.ehlo()  
            server.login(SENDER_EMAIL, PASSWORD)
            server.sendmail(msg['From'], msg['To'], msg.as_string())
    except:
        print('Não foi possível enviar email de notificaçao para "' + receiver_email + '"')

    #requerimento de e-mail e loop do check screen
def main():
    receiver_email = input('Seu email (opcional): ').strip()
    queue_counter = 0

    print('Estou de olho na fila...', end="\n\n")
    
    while True:
        if check_screen():
            queue_counter += 1
            print(f'Filas aceitas: {queue_counter}')
            
            send_email(receiver_email)         
            sleep(6)
           


main()     