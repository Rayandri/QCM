# -*- coding: utf-8 -*-
import random
import sys
try:
    from fonction_recurante import *  # dans le pythonpath ou dans le dossier
except:
    sys.path.append("C:\\10 rayan\\NSI\\fonction")
    from fonction_recurante import *
    print('impote via sys.path')


class Questionaire:
    """
    cette classe crée une file de question et permet de la manipuler 
    elle utile une base de donnée en .txt
    """
    
    def __init__(self):
        self.init()
    
    def init(self):
        """
        cree une liste self.liste_question
        :return:
        """
        self.liste_question = []
        with open("base_questions.txt", 'r', encoding='utf-8') as fichier: #ferme automatiquement le fichier en sortant du bloc
            for i in fichier.readlines(): # permet de lire ligne par vide
                liste_ligne = ['je suis vide'] #pour ne pas avoir d'espace en premier caractere 
                for lettre in i: # on va regarde lettre par lettre pour avoir un liste sous la forme liste('question','repA','repB','repC','repD','bonnerep')
                    # les instruction qui suivent permet de gerer le format du document base_question.txt
                    if liste_ligne[0] == 'je suis vide':
                        liste_ligne[0] = lettre
                    elif lettre == '\n':
                        pass
                    elif  lettre == ';':
                        pass
                    elif lettre == '?':
                        liste_ligne[-1] += lettre
                    elif lettre == '[':
                        liste_ligne.append('')
                    elif lettre == ']':
                        pass
                    elif lettre == '/':
                        liste_ligne.append('')

                    else:
                        liste_ligne[-1] += lettre
                self.liste_question.append(liste_ligne)

    def file_question(self, x):
        """
        crée une file de question au hasard puis l'inverse pour avoir un FIFO
        :param x: nb de question
        :return:
        """
        self.question_en_cour = []
        if x > len(self.liste_question):
            return "Trop de question par rapport a la base de donner"
        verif = 0
        while verif != x: # on rentre dans la boucle et on remplis notre self.question_en_cour
            nb = random.randint(0, len(self.liste_question) - 1)
            question = self.liste_question[nb]
            if not(question in self.question_en_cour):
                verif += 1
                self.question_en_cour.append(question)
        self.question_en_cour.reverse() # pour avoir un FIFO

    def recup_question(self):
        if not self.question_en_cour: # si self.question est vide 
            return 'Stop'
        else:
            return self.question_en_cour.pop()


    def rajout_question(self, question, a, b, c, d, bonne_reponse):
        """
        cette fonction est ecrit dans le fichier base_question.txt 
        avec un formatage precis
        :param question: la question en str
        :param a: la reponse A type=str
        :param b: la reponse B 
        :param c: la reponse C
        :param d: la reponse D
        :param bonne_reponse: la bonne reponse 
        :return: nothing
        """
        txt = f"{question} ? /{a} /{b} /{c} /{d} [{bonne_reponse}];\n"
        with open("base_questions.txt", 'a', encoding='utf-8') as fichier: #with open permet de fermer automatiquemnt
            fichier.write(txt)
            print(txt)




