import smtplib


fromaddr = '.......'  
toaddrs  = '.......'   

username = 'username'  
password = 'pass'

server = smtplib.SMTP('smtp.gmail.com', 587)

SUBJECT = "Subject"   
TEXT = "Message body"
message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

server.starttls()
server.login(username, password)  
server.sendmail(fromaddr, toaddrs, message)  
server.quit()