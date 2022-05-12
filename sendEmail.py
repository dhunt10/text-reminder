import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class sendEmail:
    def __init__(self, subject="Message From Patient", filename=None):
        self.subject = subject
        self.port = 465
        self.sender_email = 'dhunt10@gmail.com'
        #self.receiver_email = 'darin@onspotdermatology.com'
        self.receiver_email = 'dhunt10@gmail.com'
        self.password = ******
        self.smtp_server = 'smtp.gmail.com'
        self.message = MIMEMultipart("alternative")
        self.message["From"] = self.sender_email
        self.message["To"] = self.receiver_email


    def prepEmail(self, data, number):
        data = data + '\n from: {}'.format(number)
        message = MIMEText(data, "plain")
        self.message["Subject"] = "Message From Patient: {}".format(number)
        self.message.attach(message)
        self.sendEmail()

    def sendEmail(self):
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.smtp_server, self.port, context=context) as server:
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, self.receiver_email, self.message.as_string())
