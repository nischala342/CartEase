import smtplib
def send_email(email,text,subject):
    s = smtplib.SMTP_SSL('smtp.gmail.com', 567)
    s.starttls()
    s.login("ebuy.vce@gmail.com", "vce@1234")
    message = 'Subject: {}\n\n{}'.format(subject, text)
    s.sendmail("ebuy.vce@gmail.com", email , message)
    s.quit()