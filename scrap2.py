# !pip install 'SQLAlchemy==1.4.46'
import json
import requests
import sqlite3
import pandas as pd

#-------------------------------------------------------------------------------------------------------------------------------
# 1st Data Source
#-------------------------------------------------------------------------------------------------------------------------------

import pandas as pd
import requests

# Fetch the JSON data
response = requests.get('https://api.jsonbin.io/v3/b/655df0470574da7622ca292b')

# Check if the request was successful
if response.status_code == 200:
    # Load the JSON data into a variable
    data = response.json()
    col=data['record'][0]
  
    # Convert JSON data to DataFrame
    df = pd.DataFrame(data['record'][1:], columns=col)
    
    # # Print the DataFrame
    print(df)
    # save df as csv
    df.to_csv('Directory/data2.csv')

    # create sqlite database
    conn = sqlite3.connect('Directory/data.db')
    c = conn.cursor()
    # create table
    c.execute('''CREATE TABLE IF NOT EXISTS stock2 (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                close REAL
            )''')
    print(df)
    # insert data into table
    for i in range(len(df)):
        c.execute('''INSERT INTO stock2 (date, close) VALUES (?,?)''', (df['date'][i], df['close'][i]))
    # commit changes
    conn.commit()
    # close connection
    conn.close()




else:
    print("Failed to fetch data. Status code:", response.status_code)
