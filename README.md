# Projet de gestion des notes

### Exécution

#### 1. Créer la base de donnée :
```bash
python3 datas/init_database.py
```

#### 2. Vérifier la connexion à la base (optionnel) :
```bash
python3 datas/database_login.py
```


#### 3. Exécuter le fichier main :
```bash
python3 main.py
```

### Informations sur l'architecture du projet
- `controllers/inscription_controller.py` : fichier permettant de vérifier les informations donnnées par l'utilisateur avant de le passer à la vue
- `datas` dossier contenant les fichiers de création et de connexion à la base de donnée
- `interfaces`dossier contenant les fichiers des interfaces du logiciel
- `utils`dossier pour le fichier de génération de fiche pour étudiant