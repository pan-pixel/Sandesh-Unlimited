import smtplib
from email.mime.text import MIMEText
import csv
import re
from math import ceil
import threading

MAX_PER_THREAD = 5

def start_thread(users, sub, body):
    thread = threading.Thread(target=send_email, args=(users, sub, body))
    thread.start()

def send_email_regex(subject, message):
    results = []
    with open("./uploads/receipts.csv", 'r', encoding="utf-8-sig") as file:
        csvreader = csv.reader(file)
        headers = next(csvreader)
        for row in csvreader:
            results.append(row)
    for person in results:
        try:
            from_email = "admin@harshitkhandwalia.me"
            from_password = "qWERT12YUIop"
            smtp_server = "box.harshitkhandwalia.me"
            smtp_port = 587
            message = message.format(name = person[0])
            print(message)
            msg = MIMEText(message)
            msg["Subject"] = subject
            msg["From"] = from_email

            server = smtplib.SMTP(smtp_server, smtp_port)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(from_email, from_password)
            server.sendmail(from_email, person[2], msg.as_string())
            server.quit()
            print("Email sent successfully!")
        except Exception as e:
            print(f"Failed to send email. Error: {e}")


def entry(sub, body):
    results =[]
    with open("./uploads/receipts.csv", 'r') as file:
        csvreader = csv.reader(file)
        headers = next(csvreader)
        for row in csvreader:
            results.append(row)
    mails = []
    for person in results:
        mails.append(person[1])
    print(mails)
    for i in range(0, int(ceil(len(mails)/MAX_PER_THREAD))):
        curr_reciepts = mails[i*MAX_PER_THREAD:i*MAX_PER_THREAD+MAX_PER_THREAD]
        print(curr_reciepts)
        start_thread(curr_reciepts, sub, body)            


def send_email(to, subject, message):
    try:
        from_email = "admin@harshitkhandwalia.me"
        from_password = "qWERT12YUIop"
        smtp_server = "box.harshitkhandwalia.me"
        smtp_port = 587
        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = from_email
        msg["To"] = from_email

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(from_email, from_password)
        server.sendmail(from_email, to, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")
