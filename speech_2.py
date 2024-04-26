import pyttsx3

# Initialisation de la synthèse vocale
engine = pyttsx3.init()

# Fonction pour contrôler la vitesse de lecture
def say(text, speed=150):  # Vitesse de lecture par défaut : 150 mots par minute
    engine.setProperty('rate', speed)  # Vitesse de lecture
    engine.setProperty('voice', 'com.apple.speech.synthesis.voice.Alex')
    engine.say(text)
    engine.runAndWait()

# Utilisation
phrase = "Bonjour, comment ça va?"
say(phrase, speed=200)  # Changer la vitesse si nécessaire


# engine.runAndWait()