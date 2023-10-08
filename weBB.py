import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response= requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = response.json()
    return "http://image.tmdb.org/t/p/w500"+data['poster_path']
def recomendation(movi):
    movie_index=movies[movies["title"]==movi].index[0]   # is se hume us movie ka index mil jayega
    distance=similarity[movie_index]
    movie_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x: x[1])[1:10]
    recomend_movies=[]
    recomend_movies_poster=[]
    for i in movie_list:
        movie_id=movies.iloc[i[0]].movie_id
        recomend_movies.append(movies.iloc[i[0]].title)
        recomend_movies_poster.append(fetch_poster((movie_id)))
    return recomend_movies,recomend_movies_poster

movies_dict = pickle.load(open('movie2.pkl','rb'))
movies =pd.DataFrame(movies_dict)
similarity=pickle.load(open("similarity.pkl",'rb'))
st.title('Goofy movies')
selected_movie= st.selectbox('what would you like to watch with us',movies['title'].values)
if st.button('recomendation'):
    names,poster = recomendation(selected_movie)
    col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns(9)
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
    with col6:
        st.text(names[5])
        st.image(poster[5])
    with col7:
        st.text(names[6])
        st.image(poster[6])
    with col8:
        st.text(names[7])
        st.image(poster[7])
    with col9:
        st.text(names[8])
        st.image(poster[8])



