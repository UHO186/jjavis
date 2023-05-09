import audio_test as at
import clova_voice as cv
# import naver_tts as nt
import simsims as si
import time
# import playsound
import webbrowser

while True:
    time.sleep(5)
    cv.clova(si.sims(at.recordAudio()))
    break

webbrowser.open("TTS.mp3")