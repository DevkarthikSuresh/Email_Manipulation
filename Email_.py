
import imaplib
import email
from email.header import decode_header
import yagmail

IMAP_SERVER = 'imap.gmail.com'
IMAP_PORT = 993

EMAIL = 'sansuresh311@gmail.com'
PASSWORD = 'yydv ddux xlbx beks'

mail = imaplib.IMAP4_SSL(IMAP_SERVER,IMAP_PORT) #connection to server
mail.login(EMAIL,PASSWORD)
mail.select('INBOX')

typ, data = mail.search(None,'FROM','devkarthik300@gmail.com') #returns 2 element tuple of message IDs of email in data,output in type in 'OK'

if typ == 'OK':
    for num in data[0].split():
        typ,msg = mail.fetch(num,'(RFC822)') #finds the message related to that ID in RFC822 format(format for display)
        if typ == 'OK':
            msg = email.message_from_bytes(msg[0][1]) #msg is a tuple,msg[0][1] access the first element ie another tuples second element
            sender = msg['From']
            subject = msg['Subject']
            date = msg['Date']


            subject = decode_header(subject)[0][0] #decodes subject
            if isinstance(subject,bytes): #checks if subject is in bytes
                subject = subject.decode()
            print(f'From: {sender}')
            print(f'Subject: {subject}')
            print(f'Date: {date}')

            for part in msg.walk(): #iterates over the email content (1st iteration for first part (first part maybe html,plain text etc) then next part,so it iterates over that para until that type ends)
                if part.get_content_type() == 'text/plain' and part.get('Content-Disposition') is None:
                    # Print plain text email content without headers
                    print(part.get_payload(decode=True).decode('utf-8'))




mail.logout()
