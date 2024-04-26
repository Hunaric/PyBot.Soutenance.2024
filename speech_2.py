import pyttsx3 as p


engine = p.init('sapi5')
# rate = engine.getProperty('rate')
# engine.setProperty('rate', rate )
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

def say(text):
    engine.say(text)
    engine.runAndWait()
    
if __name__ == '__main__':
    say("Je vis maintenant à Akpakpa")