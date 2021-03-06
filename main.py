from dotenv import load_dotenv
load_dotenv()
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import tkinter as tk
import webbrowser

def open_spotify(url):
    webbrowser.open(url, new = 2)
def create_label(text):
    return tk.Label(master = frm_recommendations, text = text)
def create_button(text , url):
    return tk.Button(master = frm_recommendations,  text = text, command = lambda:open_spotify(url))
def clear(*args):
    args.destroy()
def display_recommendations(responses):
    lbl_track_name = tk.Label(master = frm_recommendations, text = 'Track Name')
    lbl_artist_name = tk.Label(master = frm_recommendations, text = 'Artist Name')
    lbl_play_it = tk.Label(master = frm_recommendations, text = 'Play It')
    lbl_track_name.grid(row=0 , column=0)
    lbl_artist_name.grid(row=0 , column=1)
    lbl_play_it.grid(row=0 , column=2)
    for idx, track in enumerate(response['tracks']):
        lbl_track_name_recommend = create_label(track['name'])
        lbl_track_name_recommend.grid(row = idx + 1, column = 0)
        lbl_artist_name_recommend = create_label(track['artist'][0]['name'])
        lbl_artist_name_recommend.grid(row = idx + 1, column = 1)
        btn_play_it_recommend = create_button('Play It' , track['external_urls']['spotify'])
        btn_play_it_recommend.grid(row = idx + 1, column = 2 , padx =  10)

    def get_recommendations():
        search = ent_search.get()
        sp = spotify.Spotify(client_credentials_manager = SpotifyClientCredentials("c46eff9037ea4153bf2bb087b3998b41","2e9a0ae8263741d3968f1ed0ecda64bf"))
        result = sp.search(q = search, limit = 1)
        id_list = [result['tracks']['items'][0]['id']]
        recommendations = sp.recommendations(seed_tracks = id_list , limiit = 10)
        display_recommendations(recommendations)

    window = tk.Tk()
    frm_search_field = tk.Frame(master = window, width =100)
    frm_recommendations = tk.Frame(master = window)
    frm_search_field.pack()
    frm_recommendations.pack()
    ent_search = tk.Entry(master = frm_search_field , width = 25)
    btn_get_recommendations = tk.Button(master = frm_search_field, text = 'Get Recommendations', command = get_recommendations)
    ent_search.grid(row= 0 , column= 0 , pady= 10 , padx= 10)
    btn_get_recommendations.grid(row= 0 , column= 1 , pady= 10 , padx= 10)
    window.mainloop()

