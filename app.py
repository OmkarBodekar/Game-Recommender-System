import streamlit as st
import pickle

def fetch_poster(game_id):
    return "https://cdn.cloudflare.steamstatic.com/steam/apps/{}/header.jpg".format(game_id)

def recommend(game):
    game_index = games_list[games_list['appname'] == game].index[0]
    distances = similarity[game_index]
    games_list1 = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_games = []
    recommended_games_posters = []
    for i in games_list1:
        game_id = games_list.iloc[i[0]].appid
        recommended_games.append(games_list.iloc[i[0]].appname)
        recommended_games_posters.append(fetch_poster(game_id))
    return recommended_games, recommended_games_posters

games_list = pickle.load(open('games.pkl', 'rb'))
games = games_list['appname'].values

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Game Recommender System')

selected_game_name = st.selectbox(
    "Select Game",
    games
)

if st.button('Recommend'):
    names, posters = recommend(selected_game_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    cols = {0: col1, 1: col2, 2: col3, 3: col4, 4: col5}
    for key in cols:
        with cols[key]:
            st.header(names[key])
            st.image(posters[key])
