# -*- coding: utf-8 -*-

from tkinter import *
from random import * 
import PIL # pour les captures d'ecran
import logging # la gestion d'erreur
from tkinter.font import * #les polices
import sys #le system pour sys.exit()
from time import sleep 
import os #l'os pour les fichier executable 
from classe_QCM import * #fichier dans le dossier envoyer 
try:#pygame sert uniquement au son est donc pas obligatoire le fichier sera se debrouiller si il n'est pas installer
    import pygame.mixer
    pygame_bol = True
except:
    pygame_bol = False

try: # pour unix et windows 
    if os.name == 'posix':  # Unix
        if 'Darwin' in os.uname():  # macos X
            pass
            # from tkmacosx import * # tkmacosx permet des truc sur mac 
except:
    pass # si cela casse c'est pas grave 

try:  # ce try  est juste pour rayan
    from fonction_recurante import *  # dans le pythonpath ou dans le dossier envoyer
except:
    sys.path.append("C:\\10 rayan\\NSI\\fonction")
    from fonction_recurante import *
    print('importé via sys')

logging.basicConfig(format='line=%(lineno)s %(message)s')  # pour la gestion d'érreur




# %% debut du code

Q = Questionaire()


class Son:
    """
    cette classe gere le son mais ne marche pas trés bien puis 
    elle ne s'exucute pas si pygame n'est pas installer 
    """
    def __init__(self):
        if pygame_bol:
            pygame.mixer.init()
            self.good_son = pygame.mixer.Sound(b'good.wav')
            self.nope_son = pygame.mixer.Sound(b'None.mp3')
        else:
            self.pygame_bol = False

    def good(self):
        self.good_son.play()

    def nope(self):
        self.nope_son.play()


class Fenetre:
    """
    Cette Class sert a la gestion de l'interface graphique en tkinter
    tous ce qui est print n'est pas lu par l'utlisateur mais pas le dev il sert donc a debugoger le jeux 
    """

    def __init__(self):
        """
        pour pouvoir la relancer si besoin
        """
        self.init()

    def init(self):
        """
        initialise notre fenetre avec nos couleur et la resolution ainsi que le pleine écran et d'autre chose
        :return:
        """
        self.epi = False  # mode epileptic (esteregg)
        self.root = Tk()
        self.root['bg'] = 'white'
        self.root.title("QCM")
        self.resolution(
            mode='auto')  # fonction qui mets la resolution automatiquement en fonction de la resolution de l'ecran 1
        self.root.attributes('-fullscreen', True)
        self.top_verif = False  # si nous souhaiton utiliser des toplevel permet de savoir si ils sont activer ou pas (chez nous non normalement)
        Button(self.root, height=0, relief=FLAT, width=0, highlightthickness=0, command=self.f_epi, bg='white').place(
            x=0, y=0)  # ester egg

        self.bu_fermer = Button(self.root, bg='red', width=10, height=0, relief=FLAT,
                                command=self.root.destroy)
        self.bu_fermer.place(relx=0.988, rely=0.0001)
        self.son_init()
        self.clavier()  # pour le f11 en plein ecran
        self.jeux_QCM()

    def son_init(self):
        if pygame_bol:
            self.S = Son()
            self.son_bol = True
        else:
            self.son_bol = False

    def init_top(self):
        """
        initialise un top
        :return:
        """
        self.top = Toplevel(self.root)
        self.top['bg'] = 'white'
        self.top.title("Top")
        self.top.geometry('1920x1080')
        self.top_verif = True
        full_screen(self.top)
        self.bu_fermer = Button(self.top, bg='red', width=10, highlightthickness=0, height=0, relief=FLAT,
                                command=self.root.destroy).place(relx=0.988, rely=0.0001)

    def clavier(self):
        """
        gere le pleine ecran
        :return:
        """
        self.root.bind("<F11>", self.f_full_screen)

    def f_full_screen(self, event):
        """
        cette fonction appelle la fonction full_screen dans fonction recurante
        :return:
        """
        if self.top_verif:
            full_screen(self.top)
        else:
            full_screen(self.root)

    def affichage(self, top=0):
        """
        Affiche le root
        ou le top si il est souhaitez
        :param top:
        :return:
        """
        if top == 0:
            self.root.mainloop()
        else:
            self.top.mainloop()
            
    def rename(self, nom, top=0):
        """
        pour rename les fenêtres
        :param nom:
        :return:
        """
        if top == False:
            self.root.title(nom)
        elif top == True:
            self.top.title(nom)

    def screen_shot(self, nom, extension=".png"):
        """
        effectue un screen shot
        :param nom:
        :return:
        """
        PIL.ImageGrap.grab().sabe(nom + extension)

    def open_image(self, nom):
        """

        :param nom: avec l'extension
        :return:
        """
        photo = PhotoImage(file=nom)

        return photo

    def fond(self, couleur='0', methode=False, top=False, renvoie=False):

        """
        change la couleur du fond
        inutile de lire cette fonction elle permet juste de gérer plein de chose pour l'ester egg
        :param couleur: la couleur souhaiter ou zero pour random
        :param methode: la methode utilisé dans couleur_random()
        :param top: si on veux modifier la couleur du top
        :return: nothing
        """
        if not renvoie:
            if not top:
                if couleur != '0':
                    self.root['bg'] = couleur
                elif methode != 0:
                    self.root['bg'] = couleur_random(methode)
                else:
                    try:
                        self.root['bg'] = couleur
                    except:
                        print('erreur sur le changement de fond couleur')
            elif top:
                if couleur != '0':
                    self.top['bg'] = couleur
                elif methode != 0:
                    self.top['bg'] = couleur_random(methode)
                else:
                    try:
                        self.top['bg'] = couleur
                    except:
                        print('erreur sur le changement de fond couleur')
        else:
            self.couleur_bu = couleur_random(methode)

    def resolution(self, taille='1920x1080', top=False, mode='manuel'):
        """
        change la resolution
        :param mode: manuel or auto
        :param taille: 1920x1080
        :param top: type bool
        :return: nothing
         si le mode est auto cela change la resolution automatiquement par rapport a la resolution de l'écran
        """
        if mode == 'auto':
            x = self.root.winfo_screenwidth()
            y = self.root.winfo_screenheight()
            taille = str(x) + 'x' + str(y)
        if top == False:
            self.root.geometry(taille)
        else:
            self.top.geometry(taille)

    def actualisation(self):
        """
        gere actualisation de la fenetre et s'auto appelle au bout de 50ms
        sert pour le moment au ester egg
        :return:
        """
        if self.epi:
            self.fond(methode=4)
            self.fond(methode=3, renvoie=True)

        self.root.after(50, self.actualisation)

    def f_epi(self):
        """
        ester egg sur le mode épileptique
        :return:
        """

        self.epi = True
        self.actualisation()

    #########################################################
    # %%spyderonly debut de la zone du QCM
    #########################################################

    def jeux_QCM(self):
        """
        la base de notre interface qcm nos stringvar sont initialiser dans la methode stringvar_mutli() nos bouton
        ainsi que nos label sont placer dans une autre methode (apparition()) certain bouton ou label sont définit
        ici mets placer uniquement lorsque qu'ils sont nécessaire



        :return:
        """
        self.score = 0
        self.stringvar_multi()
        self.police_ttg = Font(size=40, family='High Tower text')  # tres tres grand si vous n'avez pas la police high Tower text
        self.police = Font(size=20, family='High Tower text') # normalement inclus avec office mettez Times news roman
        couleur_bg = '#fafafa'
        self.couleur_fg = '#3d3d5c'
        ###### def de bouton et label
        self.question_text = Label(self.root, textvariable=self.question, bg=couleur_bg, fg=self.couleur_fg,
                                   font=self.police_ttg, width=50, height=3, wraplength=1000, bd=2, relief=RAISED)
        self.input_mot = Entry(self.root, textvariable=self.input_du_mot, bg=couleur_bg, fg=self.couleur_fg,
                               font=self.police,
                               relief=RAISED, width=20)  # sert si on rajoute une question non QCM
        self.input_mot.place_forget()  # pour le cacher car par default on a des case a cocher
        self.caseA = Button(self.root, textvariable=self.caseA_txt, bg=couleur_bg, fg=self.couleur_fg, bd=2,
                            font=self.police,
                            width=17, height=4, wraplength=250, command=self.verifA)
        self.caseB = Button(self.root, textvariable=self.caseB_txt, bg=couleur_bg, fg=self.couleur_fg, bd=2,
                            font=self.police,
                            width=17, height=4, wraplength=250, command=self.verifB)
        self.caseC = Button(self.root, textvariable=self.caseC_txt, bg=couleur_bg, fg=self.couleur_fg, bd=2,
                            font=self.police,
                            width=17, height=4, wraplength=250, command=self.verifC)
        self.caseD = Button(self.root, textvariable=self.caseD_txt, bg=couleur_bg, fg=self.couleur_fg, bd=2,
                            font=self.police,
                            width=17, height=4, wraplength=250, command=self.verifD)

        #####fin question debut score gagner perdu ##################

        self.gagner_l = Label(self.root, text='Gagné', fg=self.couleur_fg, bg=couleur_bg, bd=2, font=self.police_ttg,
                              relief=RAISED, width=25)
        self.perdu_l = Label(self.root, textvariable=self.perdu_txt, fg=self.couleur_fg, bg="#fafafa", bd=2,
                             font=self.police_ttg, relief=RAISED, width=35)
        self.score_la = Label(self.root, textvariable=self.score_txt, bg='white', fg=self.couleur_fg, font=self.police,
                              width=50, height=3, wraplength=1000)
        self.score_la.place(relx=0.5, rely=0.02, anchor=CENTER)

        #### debut ajout de question ####

        self.ajout_Question_BU = Button(self.root, text='Rajout de question', fg=self.couleur_fg, bg=couleur_bg, bd=1,
                                        relief=RAISED, width=20, command=self.ajout_Question)
        self.ajout_Question_input = Entry(self.root, textvariable=self.ajout_Question_txt, fg=self.couleur_fg, bg='white',
                                          bd=2, width=75, font=self.police, relief=RAISED)
        self.caseA_input = Entry(self.root, textvariable=self.ajout_Question_txt_A, fg=self.couleur_fg, bg='white',
                                 bd=2,
                                 font=self.police, relief=RAISED, width=20)
        self.caseB_input = Entry(self.root, textvariable=self.ajout_Question_txt_B, fg=self.couleur_fg, bg='white',
                                 bd=2,
                                 font=self.police, relief=RAISED, width=20)
        self.caseC_input = Entry(self.root, textvariable=self.ajout_Question_txt_C, fg=self.couleur_fg, bg='white',
                                 bd=2,
                                 font=self.police, relief=RAISED, width=20)
        self.caseD_input = Entry(self.root, textvariable=self.ajout_Question_txt_D, fg=self.couleur_fg, bg='white',
                                 bd=2,
                                 font=self.police, relief=RAISED, width=20)
        self.instruction_la = Label(self.root, text='Mettre entre crochet la bonne réponse [A] ', fg=self.couleur_fg, bg='white', bd=0,
                                 font=self.police, relief=RAISED, width=35)
        self.Bu_ok = Button(self.root, text='Envoyer', fg=self.couleur_fg, bg='white', bd=2,
                                 font=self.police, relief=RAISED, width=20, command=self.envoyer)
        self.fin_rajout_q = Button(self.root, text='Fin', fg=self.couleur_fg, bg='white', bd=1, relief=RAISED, width=5, command=self.retour_jeux)

        self.apparition()

    def stringvar_multi(self):
        """
        les stringvar sont des variable tkinter pour les widget (button , label ect)
        ont en a beaucoup a initialiser donc on le fais dans un methode
        """
        self.init_question()
        self.perdu_txt = StringVar()
        self.perdu_txt.set("Perdu")
        self.score_txt = StringVar()
        self.score_txt.set("Ton score est de 0/10")
        self.question = StringVar()
        self.question.set(self.question_var)
        self.input_du_mot = StringVar()
        self.input_du_mot.set('Question')
        self.root.title('QCM')
        self.caseA_txt = StringVar()
        self.caseA_txt.set(self.reponseA)
        self.caseB_txt = StringVar()
        self.caseB_txt.set(self.reponseB)
        self.caseC_txt = StringVar()
        self.caseC_txt.set(self.reponseC)
        self.caseD_txt = StringVar()
        self.caseD_txt.set(self.reponseD)
        self.ajout_Question_txt = StringVar()
        self.ajout_Question_txt.set('Taper une question a ajouter')
        self.ajout_Question_txt_A = StringVar()
        self.ajout_Question_txt_A.set("reponse A ")
        self.ajout_Question_txt_B = StringVar()
        self.ajout_Question_txt_B.set("reponse B")
        self.ajout_Question_txt_C = StringVar()
        self.ajout_Question_txt_C.set("reponse C")
        self.ajout_Question_txt_D = StringVar()
        self.ajout_Question_txt_D.set("reponse D")

    # les verifA,B,... sert a verifier les bonnes réponses
    def verifA(self):
        if 'A' == self.bonnereponse:
            self.gagner()
        else:
            self.perdu()

    def verifB(self):
        if 'B' == self.bonnereponse:
            self.gagner()
        else:
            self.perdu()

    def verifC(self):
        if 'C' == self.bonnereponse:
            self.gagner()
        else:
            self.perdu()

    def verifD(self):
        if 'D' == self.bonnereponse:
            self.gagner()
        else:
            self.perdu()

    def gagner(self):
        """
        :return:

        """
        if self.son_bol:
            self.S.good()
        self.disparition()
        self.gagner_l.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.root.after(500, self.clic)  # pour éviter les miss clic
        self.score += 1

    def clic(self):
        self.root.bind('<Button-1>', self.suite)  # clique gauche

    def perdu(self):
        if self.son_bol:
            self.S.nope()
        self.disparition()
        self.perdu_txt.set(f"Perdu c'était \n {self.bonnereponse_fu()}")
        self.perdu_l.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.root.after(600, self.clic)  # pour éviter les miss clic

    def suite(self, event):
        '''
        en tkinter time sleep ne marche pas alors je mets autre chose lorsque
        l'user clique je mets la question suivante
        :return:
        '''
        self.score_txt.set(f"Ton score est de {self.score}/10")
        self.root.unbind('<Button-1>')
        self.event = event  # event ne me sert a rien pour le moment (peut etre un ester egg en plus dans le futur)
        self.perdu_l.place_forget()
        self.gagner_l.place_forget()
        self.apparition()
        self.new_question()
        self.actualise_question()

    def disparition(self):
        """
        fais disparaitre le label et les spinbox
        :return:
        """
        self.question_text.place_forget()
        self.input_mot.place_forget()
        self.caseA.place_forget()
        self.caseB.place_forget()
        self.caseC.place_forget()
        self.caseD.place_forget()
        self.ajout_Question_BU.place_forget()

    def apparition(self):
        "fais apparaitre les boutons et label sauf input mot"
        position = self.place_random() #pour placer aléatoirement les reponses
        self.caseA.place(relx=position[0], rely=0.5, anchor=CENTER)
        self.caseB.place(relx=position[1], rely=0.5, anchor=CENTER)
        self.caseC.place(relx=position[2], rely=0.5, anchor=CENTER)
        self.caseD.place(relx=position[3], rely=0.5, anchor=CENTER)
        self.question_text.place(relx=0.5, rely=0.2, anchor=CENTER)
        self.ajout_Question_BU.place(relx=0.97, rely=0.99, anchor=CENTER)

    def place_random(self):
        """
        Melange un liste
        :return: Liste melanger len = 4
        """
        liste = [0.2, 0.4, 0.6, 0.8]
        liste_bis = [ liste.pop(randint(0, len(liste)-1)) for i in range(4) ]
        return liste_bis


    def init_question(self):
        """

        :return:
        """
        Q.file_question(10)
        self.new_question()

    def new_question(self):
        """ change de question """
        question_actuelle = Q.recup_question()
        print(question_actuelle) #pour le debogage 
        if question_actuelle == "Stop":
            print('fin')
            self.fin()
        self.question_var = question_actuelle[0]
        self.reponseA = question_actuelle[1]
        self.reponseB = question_actuelle[2]
        self.reponseC = question_actuelle[3]
        self.reponseD = question_actuelle[4]
        self.bonnereponse = question_actuelle[5]

    def bonnereponse_fu(self):
        """
        recurere la bonne reponse
        :return:
        """
        if self.bonnereponse == 'A':
            return self.reponseA
        elif self.bonnereponse == 'B':
            return self.reponseB
        elif self.bonnereponse == 'C':
            return self.reponseC
        elif self.bonnereponse == 'D':
            return self.reponseD

    def actualise_question(self):
        """ actualise l'affichage des question """
        self.question.set(self.question_var)
        self.caseA_txt.set(self.reponseA)
        self.caseB_txt.set(self.reponseB)
        self.caseC_txt.set(self.reponseC)
        self.caseD_txt.set(self.reponseD)

    def ajout_Question(self):
        self.disparition()
        self.score_la.place_forget()
        self.ajout_Question_input.place(relx=0.5, rely=0.2, anchor=CENTER)
        self.caseA_input.place(relx=0.2, rely=0.5, anchor=CENTER)
        self.caseB_input.place(relx=0.4, rely=0.5, anchor=CENTER)
        self.caseC_input.place(relx=0.6, rely=0.5, anchor=CENTER)
        self.caseD_input.place(relx=0.8, rely=0.5, anchor=CENTER)
        self.instruction_la.place(relx=0.5, rely=0.1, anchor= CENTER)
        self.Bu_ok.place(relx=0.5, rely=0.8, anchor=CENTER)
        self.fin_rajout_q.place(relx=0.99, rely=0.99, anchor=CENTER)

    def envoyer(self):
        reponseA = self.ajout_Question_txt_A.get()
        reponseB = self.ajout_Question_txt_B.get()
        reponseC = self.ajout_Question_txt_C.get()
        reponseD = self.ajout_Question_txt_D.get()
        question = self.ajout_Question_txt.get()
        reponseA.upper()
        reponseB.upper()
        reponseC.upper()
        reponseD.upper()
        if '[' in reponseA:
            bonnereponse = 'A'
            reponseA = reponseA.replace('[','')
            reponseA =reponseA.replace(']','')
        elif '[' in reponseB:
            bonnereponse = 'B'
            reponseB = reponseB.replace('[', '')
            reponseB = reponseB.replace(']', '')
        elif '[' in reponseC:
            bonnereponse = 'C'
            reponseC = reponseC.replace('[', '')
            reponseC = reponseC.replace(']', '')
        elif '[' in reponseD:
            bonnereponse = 'D'
            reponseD = reponseD.replace('[', '')
            reponseD = reponseD.replace(']', '')
        question = maj_premiere(question)
        self.ajout_Question_txt.set('Taper une question a ajouter')
        self.ajout_Question_txt_A.set("reponse A")
        self.ajout_Question_txt_B.set("reponse B")
        self.ajout_Question_txt_C.set("reponse C")
        self.ajout_Question_txt_D.set("reponse D")
        Q.rajout_question(question, reponseA, reponseB, reponseC, reponseD, bonnereponse)

    def retour_jeux(self):
        self.fin_rajout_q.place_forget()
        self.ajout_Question_input.place_forget()
        self.caseA_input.place_forget()
        self.caseB_input.place_forget()
        self.caseC_input.place_forget()
        self.caseD_input.place_forget()
        self.instruction_la.place_forget()
        self.Bu_ok.place_forget()
        self.apparition()
        self.score_la.place(relx=0.5, rely=0.02, anchor=CENTER)


    def fin(self):
        """

        :return:
        """
        self.disparition()
        if self.score < 5:
            msg = f"Nul ton score est de {self.score}"
        elif self.score < 7:
            msg = f"Ca va mais vous pouvez mieux faire ton score est de {self.score}"
        elif self.score < 9:
            msg = f"Bravo ton score est de {self.score}"
        else:
            msg = f"Parfais 10/10"
        self.msg_fin = Label(self.root, text=msg, bg='white', fg=self.couleur_fg, font=self.police, width=50, height=3,
                             wraplength=1000)
        self.msg_fin.place(anchor=CENTER, relx=0.5, rely=0.5)


