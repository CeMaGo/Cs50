#to be run in terminal

import pyttsx3

# engine = pyttsx3.init()
# engine.say("hello,world")
# engine.runAndWait()


engine = pyttsx3.init()
name = input("Name: ")
engine.say(f"hello, {name}")
engine.runAndWait()


