import speech_recognition as sr

r=sr.Recognizer()
audio='hindi1.wav'
with sr.AudioFile(audio) as source:
    print("If microphone is in Use then Say something?")
    audio=r.record(source)
    print("Done listening")
try:
    print("Audio-To-Text : "+r.recognize_google(audio))
except Exception:
    print("Say something else")



