import pandas as pd

from sqlalchemy import create_engine

# Database connection details
server = 'JG-ASUS'
database = 'Dominion'
username = 'integration'
password = '!Pr0ject'

# Create connection string
connection_string = f"mssql+pyodbc://{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"

# Create engine
engine = create_engine(connection_string)

# Read CSV file into DataFrame
df = pd.read_csv(r'C:\Users\8bit1\OneDrive\Documents\GitHub\Dominion-Queen\scraped_table.csv')

#print(df)


# Write DataFrame to SQL Server
df.to_sql('CardList', engine, if_exists='replace', index=False)

#print("Data imported successfully!")
