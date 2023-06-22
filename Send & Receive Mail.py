# 1. send email by python using smtp
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
from getpass import getpass
import ssl
from easygui import *

# (1) send plain email
sender_email = input("Sender's Email: ")
password = getpass("Password: ")
receiver_email = input("Receiver's Email: ")
sender = input("Sender's Name: ")
receiver = input("Receiver's Name: ")
subject = input("Subject: ")
# content = input(f"Content: Dear {receiver}: \n\n") or
content = input("Content:")
exit()

context = ssl.create_default_context()  # 加载系统允许的证书，在登录时进行hostname、证书验证
smtp_obj = smtplib.SMTP_SSL("smtp.qq.com", 465, context=context)

# smtp_obj = smtplib.SMTP_SSL("smtp.gmail.com", 465) or
# smtp_obj = smtplib.SMTP_SSL("smtp.qq.com", 465) or
# smtp_obj = smtplib.SMTP_SSL("smtp.163.com", 465) or
# smtp_obj = smtplib.SMTP_SSL("smtp.126.com", 465)     #使用SMTP端口号均为465

smtp_obj.login(sender_email, password)

msg = MIMEText(content, "plain", "utf-8")
msg["From"] = formataddr((sender, sender_email))
msg["To"] = formataddr((receiver, receiver_email))
msg["Subject"] = Header(subject, "utf-8")

smtp_obj.sendmail(sender_email, [receiver_email], msg.as_string())  # receiver_email can be more than 1
smtp_obj.quit()
msgbox("Email has been sent successfully!")

# ----------------------------------------------------------------------------------------------------------------------

# 2. send email by python using email.message
from email.message import EmailMessage

# (1) send plain email
context = ssl.create_default_context()

sender_email = input("Sender's Email: ")
receiver_email = input("Receiver's Email: ")
sender = input("Sender's Name: ")
receiver = input("Receiver's Name: ")
subject = input("Subject: ")

msg = EmailMessage()
msg["From"] = formataddr((sender, sender_email))
msg["To"] = formataddr((receiver, receiver_email))
msg["Subject"] = Header(subject, "utf-8")
# content = input("Content: ") or
content = input("Content:")
exit()
msg.set_content(content)

with smtplib.SMTP_SSL("smtp.qq.com", 465, context=context) as smtp_obj:
    smtp_obj.login(sender_email, password)
    smtp_obj.send_message(msg)

msgbox("Email has been sent successfully!")

# (2) send attached files -- in between msg.set_content and "with" sentence
filename = "image.xxx"
with open("filename", "rb") as f:
    filedata = f.read()

msg.add_attachment(filedata, maintype="image", subtype="xxx", filename=filename)

# (3) send html email -- in between msg.set_content and "with" sentence
msg.add_alternative("""\
the html content
""", subtype="html")

# (4) send to different receivers
contacts = ["""The list of receivers"""]
with smtplib.SMTP_SSL("smtp.qq.com", 465, context=context) as smtp_obj:
    smtp_obj.login(sender_email, password)
    for contact in contacts:
        msg["From"] = formataddr((sender, sender_email))
        msg["To"] = formataddr((receiver, receiver_email))
        msg["Subject"] = Header(subject, "utf-8")
        content = input(f"Content: Dear {contact}: \n\n")
        #         or content = textbox("Content:")
        #            exit()
        msg.set_content(content)
        smtp_obj.send_message(msg)

# # (5) send to local debugging server (type "python -m smtpd -c DebuggingServer -n localhost:1025" in terminal)
# with smtplib.SMTP("localhost", 1025) as smtp_obj:
#     sender_email = input("Sender's Email: ")
#     receiver_email = input("Receiver's Email: ")
#     sender = input("Sender's Name: ")
#     receiver = input("Receiver's Name: ")

#     subject = input("Subject: ")
#     content = textbox("Content:")
#     exit()
#     msg = f"Subject: {subject}\n\n{content}"

#     smtp_obj.sendmail(sender/sender_email, receiver/receiver_email, msg)

# ----------------------------------------------------------------------------------------------------------------------

# 3. receive email by python using IMAP4
import imaplib
import email
from getpass import getpass

server = imaplib.IMAP4_SSL("imap.qq.com", 993)  # or
# server = imaplib.IMAP4_SSL("imap.126.com", 993) or
# server = imaplib.IMAP4_SSL("imap.163.com", 993) or
# server = imaplib.IMAP4_SSL("imap.gmail.com", 993)    #使用IMAP端口号均为465

# 网易邮箱需要发送额外的Command验证后才能登录，包括gmail （QQ邮箱不需要！）
# imaplib.Commands['ID'] = ('NONAUTH', 'AUTH', 'SELECTED')
# args = ("name", "imaplib", "version", "1.0.0")
# typ, dat = server._simple_command('ID', '("'+'""'.join(args) + '")')

receiver_email = input("Receiver's Email: ")
password = getpass("Password: ")
server.login(receiver_email, password)
server.select("Inbox")
type, data = server.search(None, "UNSEEN")  # or "SEEN","ALL"

# view everything
fetch_data_list = []
for num in data[0].split():
    type, fetch_data = server.fetch(num, '(RFC822)')
    fetch_data_list.append(fetch_data)

# view different sections
msg = email.message_from_bytes(fetch_data_list[0][0][1])
print('From: ', msg['from'])
print('Date: ', msg['date'])
print('To: ', msg['to'])

for fetch_data in fetch_data_list:
    message = email.message_from_bytes(fetch_data[0][1])
    dh = email.header.decode_header(message['Subject'])
    subject = dh[0][0].decode(dh[0][1])
    print('Subject：', subject)

    for part in message.walk():
        if part.get_content_maintype() == 'text':
            body = part.get_payload(decode=True)
            text = body.decode('utf-8')
        if part.get_content_maintype() == "image":
            filename = part.get_filename()
            content = part.get_payload(decode=True)
            with open(filename, "wb") as f:
                f.write(content)
            print(f"Save attachment {filename}")

# view photos
from IPython.display import Image

Image("photo")  # type(filename) == str

server.close()
server.logout()
