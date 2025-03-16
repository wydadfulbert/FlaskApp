import psycopg2
from flask import Flask

app = Flask(__name__)

# Paramètres de connexion à PostgreSQL
DB_HOST = 'postgres-service'  # Nom du service PostgreSQL dans Kubernetes
DB_PORT = '5432'
DB_NAME = 'mon_flask_db'      # Nom de la base de données
DB_USER = 'postgres'          # Utilisateur PostgreSQL
DB_PASSWORD = 'mysecretpassword'  # Mot de passe de PostgreSQL

# Fonction pour connecter à la base de données PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT message FROM greetings LIMIT 1;')
    message = cur.fetchone()[0]
    cur.close()
    conn.close()
    return f'PostgreSQL says: {message}'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
