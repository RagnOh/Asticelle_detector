import cv2
import os
import random

# Cartella con le immagini originali
cartella_originale = "/Users/ragno/Downloads/Mol2/"  # Sostituisci con il nome della tua cartella

# Cartella per le immagini ruotate
cartella_ruotate = "immagini_ruotate"  # Sostituisci con il nome che preferisci

# Numero di copie ruotate per ogni immagine
n_copie = 21

# Percorso completo delle cartelle
percorso_originale = os.path.join(os.getcwd(), cartella_originale)
percorso_ruotate = os.path.join(os.getcwd(), cartella_ruotate)

# Creare la cartella per le immagini ruotate se non esiste
if not os.path.exists(percorso_ruotate):
    os.makedirs(percorso_ruotate)

# Elenco delle immagini nella cartella originale
immagini_originali = os.listdir(percorso_originale)

# Per ogni immagine originale...
for immagine in immagini_originali:
    # Nome dell'immagine senza estensione
    nome_senza_estensione, estensione = os.path.splitext(immagine)

    # Caricare l'immagine originale
    immagine_originale = cv2.imread(os.path.join(percorso_originale, immagine))

    # Ruotare l'immagine per n_copie volte con angoli casuali
    for i in range(n_copie):
        # Centro dell'immagine
        (h, w) = immagine_originale.shape[:2]
        centro = (w // 2, h // 2)

        # Angolo casuale tra -180 e 180 gradi
        angolo_casuale = random.randint(-180, 180)

        # Matrice di rotazione
        M = cv2.getRotationMatrix2D(centro, angolo_casuale, 1.0)

        # Ruotare l'immagine
        immagine_ruotata = cv2.warpAffine(immagine_originale, M, (w, h))
        ruota="ruota"
        # Salvare l'immagine ruotata con un nome univoco
        nome_ruotato = f"{nome_senza_estensione}_{ruota}_{i+1:02d}{estensione}"
        cv2.imwrite(os.path.join(percorso_ruotate, nome_ruotato), immagine_ruotata)
