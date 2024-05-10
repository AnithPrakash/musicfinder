import streamlit as st 
import pickle 
import pandas as pd 
import requests


def fetcch_poster(music_title):
    response=requests.get('https://saavn.dev/api/search/songs?query={}&page=1&limit=2'.format(music_title))
    data=response.json()
    return data['data']['results'][0]['images'][2]['link']

def recommend(music):
    music_index=music[music['title'] == selected_music].index[0]
    distance=similarity[music_index]
    music_list=sorted(list(enumerate(distance)), reverse=True, key=lambda x:x[1])[1:6]
    recommend_music=[]
    recommend_music_poster=[]
    for i in music_list:
        music_title=music.iloc[i[0]].title
        recommend_music.append(music.iloc[1[0]].title)
        recommend_music_poster.append(fetcch_poster(music_title))
    return recommend_music,recommend_music_poster


music_dict=pickle.load(open('music.pkl','rb'))
music=pd.DataFrame(music_dict)

similarity=pickle.load(open('similarities.pkl','rb'))
st.title("Music Recommendation System")

selected_music_name=st.selectbox("Select a music you like",music['title'].values)


if st.button('Recommend'):
    names,posters=recommend(selected_music_name)

    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col4:
        st.text(names[4])
        st.image(posters[4])
