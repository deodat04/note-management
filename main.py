import sqlite3
from etudiant import Inscription

def save_etudiant(e):
    try:
        conn = sqlite3.connect('etudiants.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO etudiants (nom, prenom, sexe, date_naissance, lieu_naissance)
            VALUES (?, ?, ?, ?, ?)
        ''', (e.get_nom(), e.get_prenom(), e.get_sexe(), e.get_date_de_naissance(), e.get_lieu_de_naissance()))
        conn.commit()
        print("Étudiant enregistré dans la base de données avec succès.")
    except sqlite3.Error as error:
        print("Erreur lors de l'enregistrement :", error)
    finally:
        if conn:
            conn.close()

## to display datas save in database
def view_datas_database():
    try:
        conn = sqlite3.connect('etudiants.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM etudiants')

        rows = cursor.fetchall()
        if rows:
            print("Liste des étudiants enregistrés")
            for row in rows:
                print(row)
        else:
            print("Aucun étudiant enregistrer dans la base de donnée.")
    
    except sqlite3.Error as error:
        print("Erreur lors de la lecture de la base de données :", error)
    
    finally:
        if conn:
            conn.close()



if __name__ == "__main__":
    etudiant_instance = Inscription()
    etudiant_instance.Infos_Etudiant()
    save_etudiant(etudiant_instance)
    #view_datas_database()
    
