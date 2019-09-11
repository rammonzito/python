import smtplib
import time
import imaplib
import email

ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "" + ORG_EMAIL
FROM_PWD    = ""
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993

# -------------------------------------------------
#
# Reading Gmail from Python
#
# ------------------------------------------------

def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')

        data = mail.search(None, '(SUBJECT "teste")' )
        mail_ids = data[1]

        # print(mail_ids)

        # print(mail_ids[:1])

        # first_email_id = mail_ids[0]
        # latest_email_id = int(mail_ids[-1])

        # print("Reading emails from {} to {}.\n\n".format(latest_email_id, first_email_id))

        print(0)
        for i in range(7190,7191, -1):
            print(1)
            typ, data = mail.fetch(str.encode(str(i)), '(RFC822)')
            
            for response_part in data:
                # if isinstance(response_part, tuple):
                #     msg = email.message_from_string(response_part[1])
                    print(response_part)
                    email_subject = msg['subject']
                    email_from = msg['from']
                    print('From : ' + email_from)
                    print('Subject : ' + email_subject)
        mail.logout()

    except Exception as e:
        print(str(e))
        mail.logout()

if __name__ == '__main__':
    read_email_from_gmail()