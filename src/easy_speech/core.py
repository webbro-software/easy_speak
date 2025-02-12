import io
import pygame
from gtts import gTTS

def easy_speech(text, lang="en"):
    with io.BytesIO() as file:
        gTTS(text=text, lang=lang).write_to_fp(file)
        file.seek(0)
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue