import streamlit as st
import pickle
import pandas as pd
import requests
import numpy as np

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{m_id}?api_key=1101f53ced5f3dd9242cfd61c8cf3b48&language=en-US".format(m_id=movie_id)
    data = requests.get(url)
    data = data.json()
    return "https://image.tmdb.org/t/p/original/"+data['poster_path']

def recommend(movie):
    def Sort_Tuple(tup):
        lst = len(tup)
        for i in range(0, lst):
            for j in range(0, lst - i - 1):
                if (tup[j][1] < tup[j + 1][1]):
                    temp = tup[j]
                    tup[j] = tup[j + 1]
                    tup[j + 1] = temp
        return tup

    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    sorted_distances = Sort_Tuple(list(enumerate(similarity[movie_index])))[1:6]
    y = []
    y_poster=[]
    for i in sorted_distances:
        movie_id = movies.iloc[i[0]].id
        y.append(movies.iloc[i[0]].title)
        y_poster.append(fetch_poster(movie_id))
    return y,y_poster
movies_list = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_list)

#similarity
similarity1=pickle.load(open('similarity1.pkl','rb'))
similarity2=pickle.load(open('similarity2.pkl','rb'))
similarity3=pickle.load(open('similarity3.pkl','rb'))
similarity4=pickle.load(open('similarity4.pkl','rb'))
similarity5=pickle.load(open('similarity5.pkl','rb'))
similarity6=pickle.load(open('similarity6.pkl','rb'))
similarity7=pickle.load(open('similarity7.pkl','rb'))
similarity8=pickle.load(open('similarity8.pkl','rb'))
similarity9=pickle.load(open('similarity9.pkl','rb'))
similarity10=pickle.load(open('similarity10.pkl','rb'))
similarity=np.concatenate((similarity1,similarity2,similarity3,similarity4,similarity5,similarity6,similarity7,similarity8,similarity9,similarity10))

st.title('Movie Recommender System')

movie_name = st.selectbox(
    "Enter the movie Name",movies['title'].values
)

if st.button("Recommend"):
    names,poster=recommend(movie_name)

    col1,col2,col3,col4,col5=st.columns(5,gap="large")
    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col2:
        st.text(names[1])
        st.image(poster[1])
    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])
