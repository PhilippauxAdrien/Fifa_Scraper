# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import pandas as pd
import os 

url = "https://www.fifaindex.com/fr"


page = requests.get(url)

html = page.content
soup = BeautifulSoup(html,'lxml')

A=[]
B=[]
C=[]
#LIGUE 1
for i in range(1,20):
    print(i)
    url_temp = url+'/players/'+str(i)+'/?league=16&order=desc'
    
    while(True):
        print("Getting page "+str(i))
        try:
            page = requests.get(url_temp)
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            print(e)
            continue
        break

    html = page.content
    soup = BeautifulSoup(html,'lxml')
    right_table=soup.find('table', class_='table table-striped table-players')
    teams = soup.findAll('a', attrs={'class':'link-team'})
    
    for team in teams:
        C.append(team["title"])

    for row in right_table.findAll("tr"):
        cells = row.find("td")
        if(cells!=None):
            a = cells.find("a")
            if(a!=None):
                A.append(a["title"])
                B.append(a["href"])
    df=pd.DataFrame({'Name':A, 'url' : B, 'team' : C})
    print(df)
df.to_csv('Ligue1-Names.csv', index = False, encoding = 'utf-8')

#BPL
A=[]
B=[]
C=[]

for i in range(1,4):
    print(i)
    url_temp = url+'/players/'+str(i)+'/?league=13&order=desc'
    
    while(True):
        print("Getting page "+str(i))
        try:
            page = requests.get(url_temp)
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            print(e)
            continue
        break

    html = page.content
    soup = BeautifulSoup(html,'lxml')
    right_table=soup.find('table', class_='table table-striped table-players')
    teams = soup.findAll('a', attrs={'class':'link-team'})
    
    for team in teams:
        C.append(team["title"])
    for row in right_table.findAll("tr"):
        cells = row.find("td")
        if(cells!=None):
            if(team!=None):
                print(team)
            a = cells.find("a")
            if(a!=None):
                A.append(a["title"])
                B.append(a["href"])
    df=pd.DataFrame({'Name':A, 'url' : B, 'team' : C})
    print(df)
df.to_csv('BPL-Names.csv', index = False, encoding = 'utf-8')

##run Pictures.py
os.system('python Pictures.py')