import imaplib
import email

# -------------------------------------------------
# Reading Mail from Python
# ------------------------------------------------

class Xeretador():

    def read_email_from_gmail():
        file1 = open("C:/pass.txt","r")

        ORG_EMAIL   = "@gmail.com"
        FROM_EMAIL  = "" + ORG_EMAIL #input("digita o prefixo do e-mail pra mim: ") + ORG_EMAIL
        FROM_PWD    = file1.read()
        SMTP_SERVER = "imap.gmail.com"
        SUBJECT = "no coffee no work" # input("Digita o assunto bb:")
        try:
            mail = imaplib.IMAP4_SSL(SMTP_SERVER)
            mail.login(FROM_EMAIL,FROM_PWD)
            mail.select('inbox')

            type, maildata = mail.search(None, '(SUBJECT "'+ SUBJECT + '")')
            for num in maildata[0].split():
                typ, maildata = mail.fetch(num, '(RFC822)' )
                raw_email = maildata[0][1]
                raw_email_string = raw_email.decode('utf-8')
                email_message = email.message_from_string(raw_email_string)
                for response_part in maildata:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_string(response_part[1].decode('utf-8'))
                        # email_subject = msg['subject']
                        # email_from = msg['from']
                        # print ('From : ' + email_from + '\n')
                        # print ('Subject : ' + email_subject + '\n')

            mail.logout()
            return msg.as_string().strip()

        except Exception as e:
            print(str("exception: " + e))
            mail.logout()

    if __name__ == '__main__':
        read_email_from_gmail()