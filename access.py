import os
import csv

def path(argument):
    if os.stat("path.txt").st_size != 0:
        with open("path.txt", 'r') as file:
            check = csv.reader(file)
            for row in check:
                if argument in row[0]:
                    return row[1]
                
def url(argument):
    if os.stat("url.txt").st_size != 0:
        with open("url.txt", 'r') as file:
            check = csv.reader(file)
            for row in check:
                if argument in row[0]:
                    return row[1]
                

def personal_details(argument):
    if os.stat("my_mail_details.txt").st_size != 0:
        with open("my_mail_details.txt", 'r') as file:
            check = csv.reader(file)
            for row in check:
                if argument in row[0]:
                    return row[1],row[2]
                

def mail_details(argument):
    if os.stat("mail_details.txt").st_size != 0:
        with open("mail_details.txt", 'r') as file:
            check = csv.reader(file)
            for row in check:
                if argument in row[0]:
                    return row[1]
                
