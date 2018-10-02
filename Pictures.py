# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import pandas as pd
import shutil
import csv
import os

url = "https://www.fifaindex.com"

# file_reader= open('Ligue1-Names.csv', "rt", encoding="utf8")
# read = csv.reader(file_reader)
# print("Ligue1... Read completed")

# next(read) #skip first line

# for row in read :
#     url_temp = url+row[1]
#     print(url_temp)
#     while(True):
#         print("Getting page for "+row[0])
#         try:
#             page = requests.get(url_temp)
#         except requests.exceptions.RequestException as e:  # This is the correct syntax
#             print(e)
#             continue
#         break

#     html = page.content
#     soup = BeautifulSoup(html,'lxml')
    
#     Nat = soup.find('img')
#     print(Nat['src'])
#     while(True):
#         try:
#             response = requests.get(url+Nat['src'], stream=True)
#         except requests.exceptions.RequestException as e:  # This is the correct syntax
#             print(e)
#             continue
#         break
#     with open('Pictures/Ligue1'+row[0]+'.png', 'wb') as out_file:
#         shutil.copyfileobj(response.raw, out_file)
#     del response


file_reader= open('BPL-Names.csv', "rt", encoding="utf8")
read = csv.reader(file_reader)
print("BPL... Read completed")

next(read) #skip first line

for row in read :
    url_temp = url+row[1]
    print(url_temp)
    while(True):
        print("Getting page for "+row[0])
        try:
            page = requests.get(url_temp)
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            print(e)
            continue
        break

    html = page.content
    soup = BeautifulSoup(html,'lxml')
    
    Nat = soup.find('img')
    print(Nat['src'])
    while(True):
        try:
            response = requests.get(url+Nat['src'], stream=True)
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            print(e)
            continue
        break

    if not os.path.exists('Pictures/BPL/'):
        os.makedirs('Pictures/BPL/')
    with open('Pictures/BPL/'+row[0]+'.png', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response