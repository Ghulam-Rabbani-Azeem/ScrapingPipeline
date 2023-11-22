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
response = requests.get('https://sheets.googleapis.com/v4/spreadsheets/19B9f42dHc3G77BBlFrmgXVxJsPzh0h0IO7lf_aBeETc/values/Sheet1?key=AIzaSyBbxq_EC9F1S584vNQh0xjwgP0b1x6RHv4')

# Check if the request was successful
if response.status_code == 200:
    # Load the JSON data into a variable
    data = response.json()
    col=data['values'][0]
  
    # Convert JSON data to DataFrame
    df = pd.DataFrame(data['values'][1:], columns=col)
    
    # # Print the DataFrame
    print(df)
    # save df as csv
    df.to_csv('Directory/data.csv')

    # create sqlite database
    conn = sqlite3.connect('Directory/data.db')
    c = conn.cursor()
    # create table
    c.execute('''CREATE TABLE IF NOT EXISTS stock (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                close REAL
            )''')
    print(df)
    # insert data into table
    for i in range(len(df)):
        c.execute('''INSERT INTO stock (date, close) VALUES (?,?)''', (df['date'][i], df['close'][i]))
    # commit changes
    conn.commit()
    # close connection
    conn.close()




else:
    print("Failed to fetch data. Status code:", response.status_code)
