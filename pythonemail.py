import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

# Open the plain text file whose name is in textfile for reading.
with open('firrs.txt') as fp:
    # Create a text/plain message
    msg = EmailMessage()
    msg.set_content(fp.read())
me ='shaileshkandel123@gmail.com'
you ='shaileshkandel123@gmail.com'
msg['subject'] = 'The contents of firrs.txt'
msg['From'] = me
msg['To'] = you
# Send the message via our own SMTP server.
print(msg)
s = smtplib.SMTP('smtp.gmail.com',587)
s.ehlo()
s.starttls()
s.login(me,'password')
#s.sendmail(me,you,msg)
s.send_message(msg)
s.quit()

