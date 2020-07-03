import requests
import pandas as pd
from bs4 import BeautifulSoup

page = requests.get('https://www.moneycontrol.com/markets/indian-indices/')
soup = BeautifulSoup(page.content, 'html.parser')
divisions = soup.find(class_='responsive')
tr = divisions.find('tr')

#for heading
heads = tr.find_all('th')
heading = [head.get_text() for head in heads]

#for values
tbody = divisions.find('tbody')
tr_bodys = tbody.find_all('tr')
values = [tr_body.get_text() for tr_body in tr_bodys]

##print(values)

val = []
for value in values:
     value = list(value.split('\n'))
     while '' in value:
          value.remove('')
     val.append(value)
##print(heading)
##for each in val:
##     print(each)

df = pd.DataFrame(data = val, columns=heading)
df.to_csv('data2.csv')
print(df)
