import smtplib

email="report.vvs@gmail.com"
password ="fhwwtlvxatblopjc"

subject = "Test Email from Python"
body = "Hello, this is a test email sent from a Python script!"
message = f"Subject: {subject}\n\n{body}"

receiver = input("enter reciver email:")
server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(email,password)
server.sendmail(email,receiver,message)
server.quit()
