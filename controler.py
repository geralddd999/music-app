from interface import AppWindow
from playback import AudioPlayback
from tkinter import filedialog
from pathlib import Path
class Controler:

    def __init__(self):
        self.audio_path = None 
        

        #player states
        self.play = None
        self.pause = None
        self.pause = None

        #views
        self.view = None 
        self.eq_view = None
        
        #AudioPaths
        self.TrackPathArray = None
        #action
        self.playback_driver = None 
        

    def link_main_view(self, app_view: AppWindow):
        self.app_gui = app_view
    
    def link_playback_driver(self, playback_driver: AudioPlayback):
        self.playback_driver = playback_driver

    def extract_tracks_from_path(self):
        self.folder_path = filedialog.askdirectory(title= "Select Files Directory")

        allowed_extensions = ["*.mp3", "*.flac", "*.wav", "*.m4a"]
        self.audio_files = []

        if self.folder_path: #user inputs
            self.folder_path= Path(self.folder_path)
            print(self.folder_path)
            for audio_ext in allowed_extensions:
                self.audio_files.extend(self.folder_path.glob(audio_ext))
        
        self.TrackPathArray = not None


    def bindViewButtons(self):
        self.app_gui.select_folder_btn.config(command=self.extract_tracks_from_path)
        self.app_gui.play_pause_btn.config(command =self.playback_driver.startAudioStream)


    def raiseError(self, error_desc):
        return(f'{error_desc}')
        
        
    



