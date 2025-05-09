# must be execute once to init database etudiants
import sqlite3

conn = sqlite3.connect('etudiants.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS etudiants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    sexe TEXT NOT NULL,
    date_naissance TEXT NOT NULL,
    lieu_naissance TEXT NOT NULL
)
''')

conn.commit()
conn.close()
print("Base de données initialisée avec succès.")


