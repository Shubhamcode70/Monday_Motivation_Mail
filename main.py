import datetime as dt
import random
import smtplib

now = dt.datetime.now()
weekday = now.weekday()

username = "mu@gmail.com"
password = "oasdd"

if weekday == 0:
    with open("quotes.txt") as qt:
        quotes = qt.readlines()
        r_quote = random.choice(quotes)
    print(r_quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(username, password)
        connection.sendmail(from_addr=username, to_addrs="apple@gmail.com", msg=f"Subject:Monday Motivation {r_quote}")


