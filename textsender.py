from email.message import EmailMessage
import smtplib
import ssl

def send(message, number):
    email_sender = 'pythonemailtesthack@gmail.com'
    email_password = 'oewolknngiaswfmq'
    email_receiver = number + '@tmomail.net'

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, message)

if __name__ == "__main__":
    main()