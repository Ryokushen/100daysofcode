##################### Normal Starting Project ######################

# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.



import pandas as pd
import random as rd
import datetime as dt
import smtplib

now = dt.datetime.now()
today = (now.month, now.day)

birthdays = pd.read_csv('birthdays.csv')
birth_dates = {(data_row['month'], data_row['day']): data_row for (index, data_row) in birthdays.iterrows()}

my_email = "fakeemail.emailtesting@gmail.com"
my_password = '14141546626'


def send_email(letter):
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birth_dates[today]['email'],
            msg=f"Subject:Happy Birthday\n\n{letter}"

        )


if today in birth_dates:
    with open(f'letter_templates/letter_{rd.randint(1,3)}.txt', 'r') as letter:
        birthday_person = birth_dates[today]
        replacement = letter.read()
        new_letter = replacement.replace("[NAME]", f"{birthday_person['name']}")
        send_email(new_letter)











