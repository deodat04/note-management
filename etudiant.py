class Etudiant:
    def __init__(self, nom, prenom, sexe, date_de_naissance, lieu_de_naissance):
        self.__nom = nom
        self.__prenom = prenom
        self.__sexe = sexe
        self.__date_de_naissance = date_de_naissance
        self.__lieu_de_naissance = lieu_de_naissance

    # Getter et Setter 
    def get_nom(self):
        return self.__nom

    def set_nom(self, nom):
        self.__nom = nom

    def get_prenom(self):
        return self.__prenom

    def set_prenom(self, prenom):
        self.__prenom = prenom

    def get_sexe(self):
        return self.__sexe

    def set_sexe(self, sexe):
        self.__sexe = sexe

    def get_date_de_naissance(self):
        return self.__date_de_naissance

    def set_date_de_naissance(self, date_de_naissance):
        self.__date_de_naissance = date_de_naissance

    def get_lieu_de_naissance(self):
        return self.__lieu_de_naissance

    def set_lieu_de_naissance(self, lieu_de_naissance):
        self.__lieu_de_naissance = lieu_de_naissance


    # methode retournant les infos de l'étudiant
    def Infos_Etudiant(self):
        print("Informations de l'étudiant")
        print(f"Nom                : {self.__nom}")
        print(f"Prénoms            : {self.__prenom}")
        print(f"Sexe               : {self.__sexe}")
        print(f"Date de naissance  : {self.__date_de_naissance}")
        print(f"Lieu de naissance  : {self.__lieu_de_naissance}")
