import pyttsx3
import speech_recognition as sr

r= sr.Recognizer()
mic= sr.Microphone()

with mic as source:
	print("You can speak now")
	r.adjust_for_ambient_noise(source)
	audio= r.listen(source)

try:
	print("Translating your speech")
	print("You said  " + r.recognize_google(audio))
	command = "You said" + r.recognize_google(audio)
	engine =pyttsx3.init()
	engine.say(command)
	engine.runAndWait()
	engine.stop()
except:
	command ="speech unrecognizable"
	engine = pyttsx3.init()
	engine.say(command)
	engine.runAndWait()
	engine.stop()
