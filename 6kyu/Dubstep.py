def song_decoder(song):
    new = song.replace("WUB", " ")
    return " ".join(new.split()).strip()