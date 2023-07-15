import requests
import pandas as pd

df=pd.DataFrame()
for i in range(1,429):
    response = requests.get('https://api.themoviedb.org/3/movie/top_rated?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US&page={}'.format(i))
    temp_df = pd.DataFrame(response.json())
    # df = df.append(temp_df,ignore_index=True)
    df = pd.concat([df, temp_df], ignore_index=True)
print(df)