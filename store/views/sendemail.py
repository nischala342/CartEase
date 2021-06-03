import smtplib
def send_email(email):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("ebuy.vce@gmail.com", "vce@1234")
    text = "Order placed successfully!"
    subject="EBuy Orders Update"
    message = 'Subject: {}\n\n{}'.format(subject, text)
    s.sendmail("ebuy.vce@gmail.com", email , message)
    s.quit()