#importing pandas for section 1
from unittest import result
import pandas as pd
# importing requests and json for section 2
import requests
import json
from google.cloud import bigquery
import os

# SECTION 1

# reading the first tab of the dataset and assigning it to a variable called tab1
tab1 = pd.read_excel('data/AHQ Data File 2016.xls',sheet_name=0)
print(tab1) 
# reading the second tabe of the dataset and assigning it to a variable called tab2
tab2 = pd.read_excel('data/AHQ Data File 2016.xls',sheet_name=1)
print(tab2) 

# SECTION 2
# using request to import data from API
apiDataset = requests.get('https://data.cms.gov/data-api/v1/dataset/d697b5d4-7464-4b91-83f9-3eaa0011e81b/data')
# assigning the json value to data
apiDataset = apiDataset.json()
print(apiDataset)

# SECTION 3
# defining project name and google application credentials 
gcp_project = 'fauzia-507'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/fauziakolia/Downloads/fauzia-507-3ecba60996ce.json"
# connecting to biquery client using credentials 
client = bigquery.Client(project=gcp_project)   
# first query using hacker news dataset (stories table) only grabbing 100 rows
query1 = client.query("SELECT * FROM `bigquery-public-data.hacker_news.stories` LIMIT 100")
# grabbing the results from the previous query 
results1 = query1.result()
# converting to dataframe and assigning to variable called bigquery1
bigquery1 = results1.to_dataframe()
print(bigquery1)
# second query using JHU covid dataset (summary table) only grabbing 100 rows
query2= client.query("SELECT * FROM `bigquery-public-data.covid19_jhu_csse.summary` LIMIT 100")
# grabbing the results from the previous query 
results2 = query2.result()
# converting to dataframe and assigning to variable called bigquery2
bigquery2 =results2.to_dataframe()
print(bigquery2)