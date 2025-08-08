import mutagen

#from mutagen.easyid3 import EasyID3
#from mutagen.flac import FLAC
#from mutagen.mp3 import MP3

def extract_metadata(track_path: str):
    """
        Extracts the metadata from a given audio-track, to be later passed to the GUI to fine-tune.
    """
    info = None
    try:
        track_info = mutagen.File(track_path) #dict

        if track_info is None:
            return

        #Differentiate between different file types

        track_title = track_info.get('title', 'Unknown Track')[0]
        track_artist = track_info.get('artist', 'Unknown Artist')[0]
        track_album = track_info.get('album', 'Unknown Album')[0]
        #track_lenght = track_info.info.lenght

        #minutes, seconds = divmod(track_lenght, 60)

        #track_duration = f"{int(minutes):02d}:{int(seconds):02d}"
        track_duration = 59
        info = {'title': track_title,'artist': track_artist, 'album': track_album, 'duration': track_duration}

    except Exception as ex:
        print("Error whilst fetching the metadata")

    return(info)

if __name__ == "__main__":
    track_path = "/home/geronimo/Downloads/viId7PU/SSU/01. CN TOWER.flac"
    #print(mutagen.File(track_path))
    print(extract_metadata(track_path))
