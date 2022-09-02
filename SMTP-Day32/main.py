import smtplib
from random import randint
import datetime as dt

my_email = "ryokushen37.emailtesting@gmail.com"
my_password = 'dnusjddnuzmhsmym'


def send_email(quote):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="ryokushen37@yahoo.com",
            msg=f"Subject:Mondays' Quote\n\n{quote}."
        )

now = dt.datetime.now()
day_of_week = now.weekday()

with open("quotes.txt", "r") as quotes:
    quotelist = quotes.readlines()
    if day_of_week == 4:
        send_email(quotelist[randint(0, 102)])





