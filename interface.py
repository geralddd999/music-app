import ttkbootstrap as ttk
import tkinter as tk
from tkinter import filedialog
from ttkbootstrap.icons import Emoji




from pathlib import Path
from track_info import extract_metadata
from playback import AudioPlayback
class AppWindow(ttk.Window):

    def __init__(self, controler):
        super().__init__(themename='darkly')
        self.title("GMP Music Player")
        self.geometry("1280x720")
        self.controler = controler


        self.misc_widgets()
        self.media_ctrl_widgets()
        self.place_window_center()
        
        #self.mainloop()


    def misc_widgets(self):
        misc_widgets_frame = ttk.Frame(self)
        self.select_folder_btn = ttk.Button(misc_widgets_frame, text="Select Folder")
        self.select_folder_btn.pack()
        
        cover = "TO COMPLETE WITH ARTWORK TAKEN FROM METADATA"
        
        misc_widgets_frame.pack(side= 'top',anchor='e')

        listbox_frame = ttk.Frame(misc_widgets_frame)
        listbox_frame.pack()
        scrollbar = ttk.Scrollbar(
            master = listbox_frame )
        track_list = ttk.Treeview(
            master =listbox_frame ,
            yscrollcommand=scrollbar.set,
            show='tree')
        track_list.pack(side='left')
        scrollbar.pack(side='right')

    
    def media_ctrl_widgets(self):
        ctrl_frame = ttk.Frame(self)
        ctrl_frame.pack(fill='x', expand = True)

        prev_btn = ttk.Button(
            master = ctrl_frame,
            text = Emoji.get('black left-pointing double triangle with vertical bar'),
            padding = 10)

        prev_btn.pack(side ='left', fill='x', expand = True)

        self.play_pause_btn = ttk.Button(
            master=ctrl_frame, 
            text = Emoji.get("black right-pointing triangle"),
            padding = 10)
        
        self.play_pause_btn.pack(side = 'left', fill = 'x', expand = True)
        #play_pause_btn.bind('<Button-1>', self.playaudio)
        
        next_btn = ttk.Button(
            master = ctrl_frame,
            text = Emoji.get('black right-pointing double triangle with vertical bar'),
            padding = 10)
        
        next_btn.pack(side = 'left', fill ='x', expand = True)


    def displayErrorBox(self):
        ttk.show_error('')





if __name__== '__main__':
    app = AppWindow()
    #app.mainloop()