from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

START_URL = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
page = requests.get(START_URL)

soup = BeautifulSoup(page.text,'html.parser')
target = soup.find('table')

temp_list = []
rows = target.find_all('tr')
for tr in rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

Proper_Names = []
Distances =[]
Masses = []
Radii =[]
Luminosity = []

for i in range(1,len(temp_list)):
    Proper_Names.append(temp_list[i][1])
    Distances.append(temp_list[i][3])
    Masses.append(temp_list[i][5])
    Radii.append(temp_list[i][6])
    Luminosity.append(temp_list[i][7])
    
df2 = pd.DataFrame(list(zip(Proper_Names,Distances,Masses,Radii,Luminosity)),columns=['Proper_Names','Distances','Masses','Radii','Luminosity'])
print(df2)

df2.to_csv('bright_stars.csv')