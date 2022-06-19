from pywhatkit import sendwhatmsg
from keyboard import press_and_release
from time import sleep
from datetime import datetime

contatos = ['+5585989333222']

print(datetime.now().hour)
print(datetime.now().minute)

while len(contatos) >= 1:
    sendwhatmsg(contatos[0], 'E ai LGBTQIA+', 
    datetime.now().hour, datetime.now().minute+1, tab_close= True)
    del contatos[0]
    sleep(15)

press_and_release('Ctrl + w')