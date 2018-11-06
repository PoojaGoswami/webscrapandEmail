import smtplib
# from email.MIMEMultipart import MIMEMultipart
# from email.MIMEText import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from email.mime.image import MIMEImage
# from email.mime.base import MIMEBase
# from email import encoders

from string import Template
# from os.path import basename

import datetime

def get_contact(filename):
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename.
    """
    names =[]
    emails=[]
    with open(filename, mode='r', encoding='UTF-8') as contact_file:
        for a_contact in contact_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
        return names, emails

def read_message(filename):
    """
    Returns a Template object comprising the contents of the
    file specified by filename.
    """
    fr =  open(filename, mode='r')
    message = fr.read()
    return Template(message)

def main():
    names, emails = get_contact('/home/pooja/Documents/projects/python/python/daily/contact.txt')
    message_template = read_message('/home/pooja/Documents/projects/python/python/daily/template.txt')
    emails_str = ','.join(emails)
    print(emails_str)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('poojacs11@gmail.com', 'XXXXXXXXXXX')  # create application specific password if u have 2 step authentication enabled
    msg = MIMEMultipart()

    msg['From'] = 'pxxxx@XXXXXX.com'
    msg['To'] = emails_str
    msg['Bcc'] = 'pxxxx@XXXXXX.com'
    Today = datetime.date.today() + datetime.timedelta(days=1)
    msg['Subject'] = 'Quote of the day ' + Today.strftime("%d-%m-%Y")
    # message = message_template.substitute(PERSON_NAME=name.title())
    message = message_template.substitute()
    print(message)
    # msg.attach(MIMEText(message, 'plain'))

    # open the file to be sent
    # filename = 'quote-of-the-day.jpg'
    # attachment = open('daily/quote-of-the-day.jpg', 'rb')
    #
    # # instance of MIMEBase and named as p
    # p = MIMEBase('application', 'octet-stream')
    #
    # # To change the payload into encoded form
    # p.set_payload((attachment).read())
    #
    # #encode into base 64
    # encoders.encode_base64(p)
    #
    # p.add_header('content-Disposition', "attachment; filename= %s" % filename)
    #
    # msg.attach(p)


    # Encapsulate the plain and HTML versions of the message body in an
    # 'alternative' part, so message agents can decide which they want to display.

    # msgAlternative = MIMEMultipart('alternative')
    # msg.attach(msgAlternative)
    #
    # msgAlternative.attach(msgText)

    # We reference the image in the IMG SRC attribute by the ID we give it below
    msgText = MIMEText(message + '<br><img src="cid:image1" width="500"><br>', 'html')
    msg.attach(msgText)
    print('quote-of-the-day-'+ str(datetime.date.today()) +'.jpg')
    # This example assumes the image is in the current directory
    fp = open('quote-of-the-day-'+ str(datetime.date.today()) +'.jpg', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image1>')
    msg.attach(msgImage)

        # /text = msg.as_string()
    server.send_message(msg)
    del msg

    # Terminate the SMTP session and close the connection
    server.quit()
    print("mail sent")

if __name__ =='__main__':
    main()
