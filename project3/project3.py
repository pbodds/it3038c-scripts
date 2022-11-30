from flask import Flask, render_template, request
import lyricsgenius

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/lyric-search/',  methods=['GET', 'POST'])
def lyric_search():
	token = request.form['tokenName']
	artist = request.form['artistName']
	song = request.form['songName']
	genius = lyricsgenius.Genius(token)
	genius.response_format = 'plain'
	artistG = genius.search_artist(artist, max_songs=2, sort="title", include_features=True)
	songG = artistG.song(song)
	return render_template("lyric-search.html", lyrics=songG.lyrics)
if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')