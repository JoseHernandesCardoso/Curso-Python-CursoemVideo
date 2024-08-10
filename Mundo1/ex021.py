from pygame import mixer

mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.set_volume(0.75)
mixer.music.play()
a = input('Digite qualquer tecla para parar: ')
