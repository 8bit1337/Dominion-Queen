# import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re

# URL of the web page with the table
# url = 'https://wiki.dominionstrategy.com/index.php/List_of_cards'  
file_path=r'C:\Users\8bit1\OneDrive\Documents\GitHub\Dominion-Queen\List of cards - Dominion Strategy Wiki.htm'


#Name,Set,Types,Cost,Text,Actions / Villagers,Cards,Buys,Coins / Coffers,Trash / Return,Exile,Junk,Gain,Victory Points

# Send a GET request to fetch the HTML content
#response = requests.get(url)
#html_content = response.content

###
# Read the content of the HTML file
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

file.close()
###

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the table on the web page (assuming there's only one table)
table = soup.find('table')

# Extract table headers
headers = []
for th in table.find_all('th'):
    headers.append(th.text.strip())

# Extract table rows
rows = []
for row in table.find_all('tr'):
    cells = row.find_all('td')
    row_data=[]
    if cells:  # Only process rows with <td> elements
        array = np.array(cells, dtype=object)
        
        for cell in cells:
            # array=np.array(cell, dtype=object)
            txt=cell.text.strip()
            if txt=='':  #when there is no text we need to potentially parse the image tag
                txt=cell.find('img')
                if txt is not None:
                    txt = txt['src'].split('/')[-1]
                    
                    # Split and extract the part with the number
                    cost = txt.split("-")[1].split(".")[0]
                    if "Coin" in cost:
                        match = re.search(r'Coin(\d+)', cost)
                        if match:
                            txt=match.group(1)
                    if "Debt" in cost:
                        match = re.search(r'Debt(\d+)', cost)
                        if match:
                            txt="-" + match.group(1)
                    
            row_data.append(txt)
        rows.append(row_data)

# Create a DataFrame from the extracted data
df = pd.DataFrame(rows, columns=headers)

# Print or save the DataFrame
#print(df)
# Optionally save to a CSV file
df.to_csv('scraped_table.csv', index=False)