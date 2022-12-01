#importing
from flask import Flask, render_template, request
import lyricsgenius

#Creating the flask app and setting the template folder
app = Flask(__name__, template_folder='templates')

#First route for my index page, localhost5000/. 
@app.route('/')
def index():
    return render_template("index.html")

#Second route for my lyrics search result page, Localhost5000/lyric-search. 
@app.route('/lyric-search/',  methods=['GET', 'POST'])
def lyric_search():
	#Creating variables for search parameters, pulled from index.html
	token = request.form['tokenName']
	artist = request.form['artistName']
	song = request.form['songName']
	#Accepting the token for API calls to Genius
	genius = lyricsgenius.Genius(token)
	genius.response_format = 'html'
	#Search for an artist with a max of 2 songs
	artistG = genius.search_artist(artist, max_songs=2, sort="title", include_features=True)
	#When the artist is found, find the song that was given above as a request.  
	songG = artistG.song(song)
	#On the template lyric-search, pass lyrics to lyric-search. songG.Lyrics will output the song lyrics from song. 
	return render_template("lyric-search.html", lyrics=songG.lyrics)

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')