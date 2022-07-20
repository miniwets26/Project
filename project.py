#!/user/bin/env python3
import os
import re
import sys
import csv
import time 
import sched
import psutil
import shutil
import logging
import smtplib
import datetime
import smtplib, ssl
import datetime as dt
from csv import reader
from email import encoders
from dotenv import load_dotenv
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart

load_dotenv()

def stats():
    print('The CPU usage is: ', psutil.cpu_percent(4))
    print('RAM memory % used:', psutil.virtual_memory()[2])
    path = 'C:\\Users\\Jorda\\OneDrive\\Desktop\\VSCode\\New folder\\Capstone\\project.py'
    print(f'{"Disk usage statistics:"}  {shutil.disk_usage(path)}')
    return True

# open file in read mode
def read_file():
    with open('C:\\Users\Jorda\OneDrive\Desktop\VSCode\\New folder\Capstone\Capstonespreadsheet.csv', 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Get all rows of csv from csv_reader object as list of tuples
        list_of_tuples = list(map(tuple, csv_reader))
        # display all rows of csv
        return list_of_tuples

def formula(tuples):
    newlist = []
    dictionary = {}
    newlist.append(tuples[0])
    # Identify/focus on tuples after header 
    tuples = tuples[1:]
    for tup in tuples:
        x = tup
        y = list(x)
        for i in range(len(tup)):
            if i == 0:
                pass
            elif i == 1:
                y[1] = int(x[1])*2
            elif i == 2:
                y[2] = int(int(x[2])*3)
            elif i == 3:
                y[3] = int(x[3])*5
        x = tuple(y)
        total_score = int(x[1]) + int(x[2]) + int(x[3])
        print(f'{x[0]}: {total_score}')
        dictionary[x[0]] = total_score
        newlist.append(x)
        
        print()
    
    return dictionary

def updated_list(dictionary):
    with open('Testing.txt', 'w') as files:
        dictionary = {k: v for k, v in sorted(dictionary.items(), key = lambda item: item[1], reverse=True)}
        dictionary = str(dictionary)
        files.write(dictionary)

def email_list():
    pattern =  r"(\w+)?\+?(\w+)@(\w+)\.(\w+)"
    f = open('email_list.txt', 'r') # open the file
    emails = f.readlines() # returns one string per file line
    for email in emails:
        result = re.match(pattern, email)
        if not result:
            print(f"{email} is an invalid email address")
            continue
        elif result:
            send_email(email) # prints each line
    f.close()
def send_email(email):
    mail_content = '''Hello,
    Please see attachment for the current task listing.
    Once your current task is completed please email back saying its completed.
    Thank You
    '''
    #The mail addresses and password
    sender_address = os.getenv("email_address")
    """ Input your app password for sender_pass"""
    sender_pass = os.getenv("password")
    receiver_address = email # this will be a recieving list 
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'This is an updated task list. Please work your way left to right unless otherwise instructed.'
    #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    attach_file_name = 'TP_python_prev.pdf'
    attach_file = open('Tasklist.txt', 'rb') # Open the file as binary mode
    payload = MIMEBase('application', 'octate-stream', name = 'Tasklist.txt')
    payload.set_payload((attach_file).read())
    encoders.encode_base64(payload) #encode the attachment
    #add payload header with filename
    payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
    message.attach(payload)
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')

def main():
    stats()
    readfile = read_file()
    z = formula(readfile)
    updated_list(z)
    print("Done")
    email_list(email_list.txt)
    while True:
    # Removing the date and microseconds from the full format
        t = str(datetime.datetime.now())[7:-7]
        if t == "07:00:00":
            email_list()
            # Wait, so it doesn't trigger the function more times
            time.sleep(1)
            break
        else:
            print("Not time yet!")
            break
        

if __name__ == "__main__":
    main()
