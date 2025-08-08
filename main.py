from controler import Controler
from interface import AppWindow
from playback import AudioPlayback



#init view 
controler = Controler()
app = AppWindow(controler=controler)
audio_driver = AudioPlayback(controler)


controler.link_main_view(app)
controler.link_playback_driver(audio_driver)
controler.bindViewButtons()

app.mainloop()