# Importing Modules
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

# Getting Page Using GET Method
url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
page = requests.get(url)

# Starting bs4 And Finding The Table
soup = bs(page.text, 'html.parser')
star_table = soup.find_all('table')

# Creating A Temporary List And Finding Table Rows
temp_list = []
table_rows = soup.find_all('tr')

# Putting Data in Rows
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

# Creating Empty Arrays Of Specified Modules That Are To Be Scraped
Star_names = []
Distance = []
Mass = []
Radius = []
Lum = []

# Specifying Modules To Scrape
for i in range(1,len(temp_list)):
    Star_names.append(temp_list[i][1])
    Distance.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])
    Lum.append(temp_list[i][7])
    
# Printing Data into a 'data.csv' file
df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,Lum)),columns=['Star Names','Distance(ly)','Mass(M)','Radius(R)','Luminosity(L)'])
df2.to_csv('stars.csv')