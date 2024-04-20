import PyPDF2
import pyttsx3

def lire_pdf(chemin_pdf, voix):
    # Ouvrir le fichier PDF
    with open(chemin_pdf, 'rb') as fichier:
        lecteur_pdf = PyPDF2.PdfFileReader(fichier)
        
        # Lire chaque page du PDF
        for num_page in range(lecteur_pdf.numPages):
            page = lecteur_pdf.getPage(num_page)
            texte = page.extractText()
            
            # Lire le texte avec la voix sélectionnée
            lire_texte(texte, voix)

def lire_texte(texte, voix):
    # Initialiser le moteur de synthèse vocale
    moteur = pyttsx3.init()
    
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
chemin_pdf = 'C:/Users/LENOVO/Desktop/PyBot/plan esme.pdf'

# Demander à l'utilisateur de choisir la voix
voix = input("Choisissez une voix (féminine/masculine) : ").lower()

# Lire le PDF avec la voix sélectionnée
lire_pdf(chemin_pdf, voix)