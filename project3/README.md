# Project 3

Patrick Boddy

### Welcome to my third and final project! I will be organizing my project in this folder.

This script will host a flask webpage on localhost 5000. The webpage will be a lyric search that will take an artist, song name and token to provide the lyrics to the song. For it to work correctly, the user will need to input a Genius client access token. The link for obtaining the token is found at: https://genius.com/api-clients. To run the script, download the dependencies and run the file with the template folder included in the folder you are running from. Open up a webpage and go to the URL http://localhost:5000/. 

## Dependencies
To ensure the script runs properly, make sure to install flask and lyricsgenius. 

`pip install flask`  
`pip install lyricsgenius`

## Usefulness

This is a project I find useful as I am deeply into music and listen to many different genres. A problem for me is hearing what the lyrics are, especially in a punk song, where it is hard to distinguish some words at times. To help, I wanted to create a script with a cool module I found called lyricsgenius that uses BeautifulSoup to scrape Genius for lyrics. It would be easier to go to Genius, but if this were an .exe then I believe this to be the fastest way to find lyrics in a song. 