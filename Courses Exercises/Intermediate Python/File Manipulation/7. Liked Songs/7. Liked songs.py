liked_songs = {
    '309': "Nsqk",
    'En pr no hace frio': 'Alvaro Diaz',
    'Shape of you': "Ed Sheeran",
    'Uptown Funk': "Mark Ronson ft. Bruno Mars",
    'Ghost': "Justin Bieber"
}

def write_liked_songs_to_file(liked_songs, file_name):
    file = open(file_name, 'w')
    for key, value in liked_songs.items():
        file.write(f"{key}, by {value}\n")
    file.close()

write_liked_songs_to_file(liked_songs, "favorite_songs")
    
