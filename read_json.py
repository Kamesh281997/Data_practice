import pandas as pd
import mysql.connector
pd.read_json("train.json")
read=pd.read_json('https://api.exchangerate-api.com/v4/latest/INR')
conn = mysql.connector.connect(host='localhost',user='root',password='',database='world')
df = pd.read_sql_query("SELECT * FROM countrylanguage",conn)
df
# print(read)
