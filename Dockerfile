# Utiliser une image Python officielle comme base
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Installer toutes les dépendances listées dans requirements.txt
RUN pip install -r requirements.txt

# Copier tous les fichiers de l'application dans le conteneur
COPY . .

# Exposer le port sur lequel l'app écoute
EXPOSE 5000

# Lancer l'application
CMD ["python", "app2.py"]
