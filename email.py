 import smtplib
import imaplib
import email
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener=sr.Recognizer()
engine=pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()


try:
    def read_mail():
        mail=imaplib.IMAP4_SSL('imap.gmail.com',993)
        mail.login('yourEmailId@gmail.com','yourPassword')
        mail.select('INBOX')
        data=mail.search(None,'ALL')
        mail_ids=data[1]
        id_list=mail_ids[0].split()
        #first_email_id=int(id_list[0])
        latest_email_id=int(id_list[-1])
        #for i in range(latest_email_id,first_email_id,-1):
        data=mail.fetch(str(latest_email_id),'(RFC822)')
        for j in data:
            arr=j[0]
            if isinstance(arr,tuple):
                msg=email.message_from_string(str(arr[1],'utf-8'))
                print('From : '+msg['From'])
                talk('email is received from')
                talk(msg['From'])
                print('Subject :'+msg['Subject'])
                talk('subject of this email is ')
                talk(msg['Subject'])
                for k in msg.get_payload():
                    if k.get_content_type()=="text/plain":
                        body=k.get_payload(decode=True)
                        body=body.decode()
                        print('Content :',end=' ')
                        print(body)
                        talk('content of this email is')
                        talk(body)
                        
                    else:
                        continue
                    
                    
except:
    pass


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice=listener.listen(source)
            info=listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass
def send_mail(receiver,subject,message):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('yourEmailID@gmail.com','yourPassword')
    email = EmailMessage()
    email['From'] = 'rakhimx27@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)

email_list={
    'president': 'presidentboss2009@gmail.com',
    'rakhi': 'rakhipundhir2711@gmail.com',
    'firstid': 'pundhirrakhi270@gmail.com',
    'simran' : 'simranpundhir27@gmail.com'
}

def get_email_info():
    talk('Rakhi to whom do you want to send mail')
    name=get_info()
    receiver=email_list[name]
    print(receiver)
    talk('tell me the subject of your email')
    subject=get_info()
    talk('Now tell me the text of your email')
    message=get_info()
    send_mail(receiver,subject,message)
    talk('Rakhi your email was successfully sent !!!')
    
    



talk('hello, rakhi to send email speak good morning else to read email speak anything you like')
user=get_info()
if user=='goodmorning' or user=='good morning':
    get_email_info()
else:
    read_mail()
talk('bye, rakhi, meet you next time')
