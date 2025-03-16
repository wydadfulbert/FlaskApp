# Utilisation de l'image officielle Python comme base
FROM python:3.9-slim

# Créer un répertoire dans le container pour le code
WORKDIR /app

# Copier les fichiers locaux (ici, ton script Python) vers le container
COPY . /app

# Installer Flask à l'intérieur du container
RUN pip install --no-cache-dir flask

# Exposer le port 5000 sur lequel le service Flask tourne
EXPOSE 5000

# Lancer ton script Flask quand le container démarre
CMD ["python", "script1.py"]
