import PyPDF2
import pyttsx3
import threading
import keyboard

def lire_pdf(chemin_pdf, voix):
    # Initialiser le moteur de synthèse vocale une seule fois
    moteur = pyttsx3.init()
    
    # Ouvrir le fichier PDF
    with open(chemin_pdf, 'rb') as fichier:
        lecteur_pdf = PyPDF2.PdfReader(fichier)
        
        # Lire chaque page du PDF
        for num_page in range(len(lecteur_pdf.pages)):
            page = lecteur_pdf.pages[num_page]
            texte = page.extract_text()
            
            # Créer un thread pour lire le texte avec la voix sélectionnée
            thread_lecture = threading.Thread(target=lire_texte, args=(moteur, texte, voix))
            thread_lecture.start()
            
            # Attendre que l'utilisateur appuie sur 's' pour arrêter la lecture
            while True:
                if keyboard.is_pressed('s'):
                    moteur.stop()
                    break

def lire_texte(moteur, texte, voix):
    # Sélectionner la voix
    voix_feminine = None
    voix_masculine = None
    for voix_disponible in moteur.getProperty('voices'):
        if "femme" in voix_disponible.name.lower():
            voix_feminine = voix_disponible.id
        elif "homme" in voix_disponible.name.lower():
            voix_masculine = voix_disponible.id
            
    if voix == "féminine" and voix_feminine:
        moteur.setProperty('voice', voix_feminine)
    elif voix == "masculine" and voix_masculine:
        moteur.setProperty('voice', voix_masculine)
        
    # Lire le texte
    moteur.say(texte)
    moteur.runAndWait()

# Chemin vers le fichier PDF
chemin_pdf = 'plan_esme.pdf'

# Demander à l'utilisateur de choisir la voix
voix = input("Choisissez une voix (féminine/masculine) : ").lower()

# Lire le PDF avec la voix sélectionnée
lire_pdf(chemin_pdf, voix)
