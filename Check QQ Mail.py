import webbrowser
import imaplib
import email
from email.header import Header
from IPython.core.display_functions import display
from IPython.display import Image

receiver_email = "2227264431@qq.com"
server = imaplib.IMAP4_SSL("imap.qq.com", 993)
password = "bjtsttafrpdwdiha"
server.login(receiver_email, password)
server.select("Inbox")

typ, data = server.search(None, "UNSEEN")
fetch_data_list = []
email_list = data[0].split()

if len(email_list) == 0:
    print("\n😯 Oops! There are no new emails!")
else:
    print("\nP.S: Please excuse the content if a word is split in half at the end of each line!" + "\n" +
          "The link in the content cannot be directed by clicking, please copy and visit it on another page.")
    print("\nThe following contents are transferred from your email address " + receiver_email + ":\n\n")

    for num in email_list:
        typ, fetch_data = server.fetch(num, '(RFC822)')
        fetch_data_list.append(fetch_data)

    msg = email.message_from_bytes(fetch_data_list[0][0][1])
    if msg['from']:
        header = email.header.decode_header(msg['from'])
        if len(header) == 1:
            try:
                print("From: " + header[0][0].decode("utf-8"))
            except BaseException:
                print("From: " + str(header[0][0]))
        if len(header) == 2:
            try:
                print("From: " + header[0][0].decode("utf-8") + header[1][0].decode("utf-8"))
            except BaseException:
                print("From: " + str(header[0][0]) + str(header[1][0]))
        if len(header) == 3:
            try:
                print("From: " + header[1][0].decode("utf-8") + header[2][0].decode("utf-8"))
            except BaseException:
                print("From: " + str(header[1][0]) + str(header[2][0]))
    if msg['date']:
        print("Date: " + str(email.header.decode_header(msg['date'])[0][0]))
    if msg['to']:
        try:
            print("To: " + email.header.decode_header(msg['to'])[0][0].decode("utf-8"))
        except BaseException:
            print("To: " + str(email.header.decode_header(msg['to'])[0][0]))

    for num in data[0].split():
        typ, fetch_data = server.fetch(num, '(RFC822)')
        fetch_data_list.append(fetch_data)

    for fetch_data in fetch_data_list:
        message = email.message_from_bytes(fetch_data[0][1])
        dh = email.header.decode_header(message['Subject'])
        if str(dh[0][0]).startswith("b'"):
            subject = dh[0][0].decode(dh[0][1])
        else:
            subject = dh[0][0]
        print('Subject：', subject)
        break

    for part in message.walk():
        if part.get_content_type() == 'text/plain':
            body = part.get_payload(decode=True)
            try:
                text = body.decode('utf-8')
            except BaseException:
                text = str(body)
            print("\n" + text + "\n")

        if part.get_content_type() == 'text/html':
            body = part.get_payload(decode=True)
            try:
                text = body.decode('utf-8')
            except BaseException:
                text = str(body)
            x = input("\n⚠️ You have an html file to receive. Do you want to receive (A) or ignore (B)? ")
            if x == "A":
                name = input("Choose a name to save the html file: ")
                with open(f"{name}.html", "w") as f:
                    f.write(text)
                webbrowser.open(f"file:///Users/gogo/Desktop/Programming/GogoPython/Python Projects/{name}.html")
            else:
                pass

        if part.get_content_maintype() == "image":
            y = input("\n⚠️ You have an image to receive. Do you want to receive (A) or ignore (B)? ")
            if y == "A":
                filename = part.get_filename()
                content = part.get_payload(decode=True)
                with open(filename, "wb") as f:
                    f.write(content)
                print(f'Saved attachment "{filename}"!')
                show = input('Display the image content below (1) or in a separate page (2) (Type "1" or "2") ? ')
                if show == "1":
                    display(Image(content))
                elif show == "2":
                    webbrowser.open(f"file:///Users/gogo/Desktop/Programming/GogoPython/Python Projects/{filename}")
                else:
                    break
            else:
                break
            break

    server.close()
    server.logout()
