import smtplib

my_email = "ryokushen37.emailtesting@gmail.com"
my_password = 'dnusjddnuzmhsmym'

connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=my_email, password=my_password)
connection.sendmail(from_addr=my_email, to_addrs="ryokushen37@yahoo.com", msg="Hello World.")
connection.close()