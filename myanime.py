import streamlit as st
import numpy as np
import pandas as pd


st.title("Movie/TV Show Recommendation App ✨")

st.markdown("""
This web app simply recommend some Movie or TV Show for the user according to their preferences. Hope enjoy my simple web app!!
* **Data Source:** [Netflix-Movies-and-TV-Shows.kaggle](https://www.kaggle.com/satpreetmakhija/netflix-movies-and-tv-shows-2021)
""" )

st.balloons()

df = pd.read_csv('newanime.csv')
df = df.dropna(axis = 0, how ='any')
df = df.astype({"Score": int})
df = df.astype({"Episodes": string})
#st.dataframe(df)



st.sidebar. write('Prepared by : Fatin Arisya Binti Azhar')




#genre

option = st.sidebar.selectbox(
    'Select Genre',
['Action','Adventure','Comedy','Slice of Life','Drama','Samurai','Game','Sci-Fi','Military','Space','Music','Mecha','Supernatural','Historical','Mystery','School','Fantasy','Horror','Kids','Sports','Dementia','Magic','Romance','Police','Cars','Shounen','Demons','Ecchi','Psychological','Shoujo','Parody','Super','Vampire','Martial','Seinen','Thriller','Josei'])
if option=='Action':
    rslt_df = df.loc[df['Genre'] == 'Action']
    
elif option=='Adventure':
    rslt_df = df.loc[df['Genre'] == 'Adventure']
  
elif option=='Comedy':
    rslt_df = df.loc[df['Genre'] == 'Comedy']
    
elif option=='Slice of Life':
    rslt_df = df.loc[df['Genre'] == 'Slice of Life']
 
elif option=='Drama':
    rslt_df = df.loc[df['Genre'] == 'Drama']
    
elif option=='Samurai':
    rslt_df = df.loc[df['Genre'] == 'Samurai']
  
elif option=='Game':
    rslt_df = df.loc[df['Genre'] == 'Game']
    
elif option=='Sci-Fi':
    rslt_df = df.loc[df['Genre'] == 'Sci-Fi']
    
elif option=='Military':
    rslt_df = df.loc[df['Genre'] == 'Military']
    
elif option=='Space':
    rslt_df = df.loc[df['Genre'] == 'Space']
  
elif option=='Music':
    rslt_df = df.loc[df['Genre'] == 'Music']
    
elif option=='Mecha':
    rslt_df = df.loc[df['Genre'] == 'Mecha']
 
elif option=='Supernatural':
    rslt_df = df.loc[df['Genre'] == 'Supernatural']
    
elif option=='Mystery':
    rslt_df = df.loc[df['Genre'] == 'Mystery']
  
elif option=='School':
    rslt_df = df.loc[df['Genre'] == 'School']
    
elif option=='Fantasy':
    rslt_df = df.loc[df['Genre'] == 'Fantasy']
    
elif option=='Horror':
    rslt_df = df.loc[df['Genre'] == 'Horror']
    
elif option=='Kids':
    rslt_df = df.loc[df['Genre'] == 'Kids']
  
elif option=='Sports':
  
  rslt_df = df.loc[df['Genre'] == 'Sports']
    
elif option=='Dementia':
  
  rslt_df = df.loc[df['Genre'] == 'Dementia']
 
elif option=='Magic':
  
  rslt_df = df.loc[df['Genre'] == 'Magic']
    
elif option=='Romance':
    rslt_df = df.loc[df['Genre'] == 'Romance']
  
elif option=='Police':
    rslt_df = df.loc[df['Genre'] == 'Police']
    
elif option=='Cars':
    rslt_df = df.loc[df['Genre'] == 'Cars']
    
elif option=='Shounen':
    rslt_df = df.loc[df['Genre'] == 'Shounen']
    
elif option=='Demons':
    rslt_df = df.loc[df['Genre'] == 'Demons']
  
elif option=='Ecchi':
    rslt_df = df.loc[df['Genre'] == 'Ecchi']
    
elif option=='Psychological':
    rslt_df = df.loc[df['Genre'] == 'Psychological']
 
elif option=='Shoujo':
    rslt_df = df.loc[df['Genre'] == 'Shoujo']
    
elif option=='Parody':
    rslt_df = df.loc[df['Genre'] == 'Parody']
  
elif option=='Super':
    rslt_df = df.loc[df['Genre'] == 'Super']
    
elif option=='Vampire':
    rslt_df = df.loc[df['Genre'] == 'Vampire']
    
elif option=='Martial':
    rslt_df = df.loc[df['Genre'] == 'Martial']
  
elif option=='Seinen':
    rslt_df = df.loc[df['Genre'] == 'Seinen']
    
elif option=='Thriller':
    rslt_df = df.loc[df['Genre'] == 'Thriller']

else:
    rslt_df = df.loc[df['Type'] == 'Josei']
   

#score

values = st.sidebar.slider('Pick a score', 1, 10)

if  values==1:
    rslt_df_1 = rslt_df.loc[rslt_df['Score'] == 1]
    

elif values==2:
     rslt_df_1 = rslt_df.loc[rslt_df['Year'] == 2]
     

elif values==3:
     rslt_df_1 = rslt_df.loc[rslt_df['Year'] == 3]
     

elif values==4:
     rslt_df_1 = rslt_df.loc[rslt_df['Year'] == 4]
     

elif values==5:
     rslt_df_1 = rslt_df.loc[rslt_df['Year'] == 5]
        

elif values==6:
     rslt_df_1 = rslt_df.loc[rslt_df['Year'] == 6]
     

elif values==7:
     rslt_df_1 = rslt_df.loc[rslt_df['Year'] == 7]
     

elif values==8:
     rslt_df_1 = rslt_df.loc[rslt_df['Year'] == 8]
     

elif values==9:
     rslt_df_1 = rslt_df.loc[rslt_df['Year'] == 9]    

else:
    rslt_df_1 = rslt_df.loc[rslt_df['Year'] == 10]
    st.dataframe(rslt_df_1)



#Rating

option = st.sidebar.selectbox(
    'Select Rating',
    ['R - 17+ (violence & profanity)',	'PG-13 - Teens 13 or older'	,'PG - Children',	'G - All Ages'])



if  option=='R - 17+ (violence & profanity)':
    rslt_df_2 = rslt_df_1.loc[rslt_df['Rating'] =='R - 17+ (violence & profanity)']
    st.dataframe(rslt_df_2)

elif option=='PG-13 - Teens 13 or older':
     rslt_df_2 = rslt_df_1.loc[rslt_df['Rating'] =='PG-13 - Teens 13 or older']
     st.dataframe(rslt_df_2)

elif option=='PG - Children':
     rslt_df_2 = rslt_df_1.loc[rslt_df['Rating'] =='PG - Children']
     st.dataframe(rslt_df_2)

else:
     st.dataframe(rslt_df_1)

