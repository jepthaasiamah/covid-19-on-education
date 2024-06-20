import requests
import pandas as pd
from bs4 import BeautifulSoup

# getting response from host then pulling tables from table class
url = 'https://en.wikipedia.org/wiki/Impact_of_the_COVID-19_pandemic_on_education'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find_all('table', attrs={'class': 'wikitable'})

# collecting columns for table of interest, caption:'Country-wide school closures by country/territory'
columns = table[0].find_all('th')
columns = BeautifulSoup(str(columns), 'html.parser').get_text()

# finding and saving the rows using 'tr' under the 'th' tab
rows = table[0].find_all('tr')
print(f'table_size: {len(table)}')
rows_tr = []
for row in rows:
    str_cell = str(row)
    row = BeautifulSoup(str_cell, 'html.parser').get_text()
    rows_tr.append(row)

# creating a dataframe to save 
df = pd.DataFrame(rows_tr[:])
covid_edu = df[0].str.split('\n', expand=True)

# convert to csv
raw_data = covid_edu.to_csv(index=False, path_or_buf='csv/raw_data.csv')