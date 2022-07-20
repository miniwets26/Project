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
from memory_profiler import profile
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from project import stats
from project import read_file

x = [('Task', 'Time', 'Size', 'Severity'), ('Capstone', '7', '8', '10'), ('Upload_schedule', '2', '5', '9'), ('Take_out_Trash', '5', '8', '8'), 
('Upload_Homework', '10', '10', '4'), ('Do_Dishes', '8', '2', '8'), ('High_Test', '10', '10', '10'), ('Mid_Test', '5', '5', '5'), ('Low_Test', '1', '1', '1')]
def test_read_file():
    assert read_file() == x

def test_stats():    
   assert stats() == True

test_stats()
test_read_file()
