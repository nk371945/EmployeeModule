
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders


def send_mail(send_from, send_to, subject, text, pre_file, post_file, url, server, port, username, password, isTls=True):
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = send_to
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    html = f'<html>\
                    <head>\
                    <p>Dear Sir/Mam,</p>\
                    <p>My Test-Report-URLs :</p>\
                    </head>\
                    <body>\
                     <table style="font-family: arial, sans-serif;border-collapse: collapse;width: 50%;">\
                       <tr style="border: 1px solid #dddddd; text-align: left; padding: 8px;">\
                       <th style="border: 1px solid #dddddd; text-align: left; padding: 8px;">URL-Employee-Payroll</th>\
                       <th style="border: 1px solid #dddddd; text-align: left; padding: 8px;">{url}</th>\
                       </tr>\
                    </table>\
                     </body>\
                     </html>'
    msg.attach(MIMEText(html, 'html'))

    msg.attach(MIMEText(text))

    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(pre_file, "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="Pre-Process(Before Automation).xlsx"')
    msg.attach(part)

    part1 = MIMEBase('application', "octet-stream")
    part1.set_payload(open(post_file, "rb").read())
    encoders.encode_base64(part1)
    part1.add_header('Content-Disposition', 'attachment; filename="Post-Process(After Automation).xlsx"')
    msg.attach(part1)
    #context = ssl.SSLContext(ssl.PROTOCOL_SSLv3)
    # SSL connection only working on Python 3+
    #with smtplib.SMTP_SSL(server, port, context=context) as server:
    #    server.login(username, password)
    smtp = smtplib.SMTP(server, port)
    if isTls:
        smtp.starttls()
    smtp.login(username, password)

    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()
