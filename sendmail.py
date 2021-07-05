# -*- coding: utf-8 -*-
#!/usr/bin/python

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart()
message = " Teste de e-mail "

password = "******"                  # Sender Password Here
msg['From'] = "from_exemple@mail.com"  # Sender Here
msg['To'] = "to_exemple@mail.com"   # Recipient Here
msg['Subject'] = "[MAIL NOTIFICATION]"  # Subject Here

msg.attach(MIMEText(message, 'plain'))
server = smtplib.SMTP('161.97.82.236: 587')  # SMTP Server Here
server.starttls()
server.login(msg['From'], password)
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()
