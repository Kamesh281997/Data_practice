import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
#     'Referer': 'https://www.ambitionbox.com/list-of-companies?page=1'
# }
# # response = requests.get(url, headers=headers)
# response = requests.get('https://www.ambitionbox.com/list-of-companies?page=1', headers=headers).text
# # webpage=requests.get('https://www.ambitionbox.com/list-of-companies?page=1').text
# soup=BeautifulSoup(response,'lxml')
# print(soup.find_all('h1'))

# for i in soup.find_all('h2'):
#   print(i.text.strip())
  
  
# for i in soup.find_all('p'):
#   print(i.text.strip())
  
# len(soup.find_all('a' , class_='review-count'))
  
# company=soup.find_all('div',class_='company-content-wrapper')

# final=pd.DataFrame()
for j in range(1,1001):
  webpage=requests.get('https://www.ambitionbox.com/list-of-companies?page={}'.format(j)).text
  soup=BeautifulSoup(webpage,'lxml')
  company=soup.find_all('div',class_='company-content-wrapper')
  name=[]
  rating=[]
  reviews=[]
  ctype=[]
  hq=[]
  how_old=[]
  no_of_employee=[]

  for i in company:

    try:
       name.append(i.find('h2').text.strip())
    except:
       name.append(np.nan)

    try:
       rating.append(i.find('p',class_='rating').text.strip())
    except:
       rating.append(np.nan)
   
    try:
        reviews.append(i.find('a' , class_='review-count').text.strip())
    except:
      reviews.append(np.nan)

    try:

      ctype.append(i.find_all('p',class_='infoEntity')[0].text.strip())
    except:
      ctype.append(np.nan)
    try:

      hq.append(i.find_all('p',class_='infoEntity')[1].text.strip())
    except:
      hq.append(np.nan)
    
    try:

      how_old.append(i.find_all('p',class_='infoEntity')[2].text.strip())
    except:
      how_old.append(np.nan)
    try:
      no_of_employee.append(i.find_all('p',class_='infoEntity')[3].text.strip())
    except:
      no_of_employee.append(np.nan)
      
    df=pd.DataFrame({'name':name,
    'rating':rating,
    'reviews':reviews,
    'company_type':ctype,
    'Head_Quarters':hq,
    'Company_Age':how_old,
    'No_of_Employee':no_of_employee,
    })
  
  final=final.append(df,ignore_index=True)
