# <BLANKLINE> correspond a une ligne vide
import logging
import random
def espace(x=1):
    '''
    >>> espace(4)
    <BLANKLINE>
    <BLANKLINE>
    <BLANKLINE>
    <BLANKLINE>
    '''
    for i in range(x):
        print('')

        
def tup_to_liste(tupple):
    '''
     Pour convertir le tupple en liste
     >>> tup_to_liste((2,1,5,1,'je suis un test'))
     [2, 1, 5, 1, 'je suis un test']
    '''
    liste=[]
    for i in tupple:
        liste.append(i)
    return(liste)

def ecrire(fichier,entre_mot,nb,*arg):
    '''
    Cette fonction sert a écrire autant d'objet avec write (le nom de la variable,ce qui faut mettre entre les mots a écrire,si on formate le mot pour aligner 0/1 ,ce qui faut écrire)
    
    '''

    if len(arg)==1:
        arg=arg[0]
    a=0
    for i in arg:
        a+=1
        mot = i
        try : mot = mot.lower()
        except: pass
        if nb==0: mot=str(mot)
        elif nb==1: mot=format(mot,'<12')
        fichier.write(mot)
        if  a!= len(arg) : # Pour écrire les espaces par exemples saufs à la fin
            fichier.write(entre_mot)
    fichier.write("\n")



def demande_de_lvl(nb_lvl,phrase,test): #on ne l'a pas utliser dans le pendu
    '''
    Parameters
    ----------
    nb_lvl : type= list or int or str or tupple
        le nombre de lvl
    phrase : type= list or tupple
        les phrases a dire
    test : type= bool 
        True pour faire un test

    Returns Le choix 
    -------
    >>> demande_de_lvl(3,['lvl 1 ','lvl 2','lvl 3'],True)
    <BLANKLINE>
    <BLANKLINE>
    lvl 1 
    lvl 2
    lvl 3
    vous avez choisis le niveau:   1
    <BLANKLINE>
    <BLANKLINE>
    1
    
    '''
    espace(2)
    if type(nb_lvl)==int or type(nb_lvl)==str:# la on convertis le nombre de lvl en liste
        nb_lvl=int(nb_lvl)
        liste_temp=[]
        for i in range(nb_lvl):
            liste_temp.append(i+1)
        nb_lvl=liste_temp
        
   
    for i in phrase:
        print(i) #pour afficher les niveau  
    
        
    if test==True:
        choix=1  
    else:
        verif=False
        while verif==False:
            try:
                choix=int(input('Alors quelle niveau voulez vous ? '))
                assert( choix in nb_lvl ) # pour verifier que le choix existe 
                verif=True
            except:
                print('erreur lors de la verification du niveau ')
                print('veuillez recommencer')
                
    print('vous avez choisis le niveau:  ',choix)
    espace(2)
    return(choix)


def recupe_date(date):
    '''
    cette fonction recupere les date d'une date  et les renvoie en 3 variables int

    Parameters
    ----------
    date : str
        dd/mm/aaaa or dd-mm-aaaa

    Returns
    -------
    None.
    >>> recupe_date('01/01/2019')
    (1, 1, 2019)
    >>> recupe_date('01-01-2019')
    (1, 1, 2019)
    '''
    j=0
    day=''
    month=''
    year=''
    for i in date:
        j+=1
        if j<=2:
            day+=i
        elif 3<j<=5:
            month+=i
        elif j>=7:
            year+=i
    return(int(day),int(month),int(year))


def print_list(liste):
    """

    Parameters
    ----------
    liste : list or tupple
        DESCRIPTION.

    Returns
    -------
    Print la liste en ligne 
    
    >>> print_list(('a','b','c'))
    a
    b
    c
    """
    for i in liste:
        print(i)

def full_screen(root):
    """

    :param root:
    :return:
    """
    root.attributes("-fullscreen",not root.attributes("-fullscreen"))

def couleur_random(methode=2,test=False):
    """

    :return: color in hex

    >>> couleur_random(test=True)
    '#FFFFFF'


    """
    """
    le saviez vous que dans un code couleur hexadecimal
    #0000FF est le bleu et correspond a 
    # 00 00 FF 
      R  G  B
      0  0  255
    donc le code hexadecimal correspond au code RGB
    
    """


    if test == True:
        return '#FFFFFF'

    # méthode 1 donne des couleur plutôt sombre
    elif methode == 1:
        x=random.randint(0,16777215)
        hexa = str(hex(x))
        hexa= hexa.replace('0x','')
        taille = len(hexa)
        zero = ''
        for i in range(6-taille):
            zero += '0'
        couleur ='#'+ zero + hexa
        return couleur
    # méthode 2
    elif methode == 2:
        couleur = '#'
        for i in range(6):
            couleur += random.choice('0123456789ABCDEF')
        return couleur
    # méthode 3  donne des couleur primaire, secondaire, tertiaire (27 couleurs)
    elif methode == 3:
        liste_couleur= ['FF','80','00']# 255 128 0
        couleur = '#'
        for i in range(3):
            couleur += liste_couleur[random.randint(0,2)]
        return  couleur
    # méthode 4 donne des couleur primaire ou secondaire (9 couleurs)
    elif methode == 4:
        liste_couleur = ['FF', '00']  # 255 0
        couleur = '#'
        for i in range(3):
            couleur += liste_couleur[random.randint(0,1 )]
        return couleur

def maj_premiere(mot):
    """

    :param mot:
    :return:
    """
    mot_up = ''
    a = 0
    for i in mot:
        a += 1
        if a==1: i = i.upper()
        mot_up += i
    return mot_up

print('fichier fonction_recurante bien importer .')

if __name__ == '__main__':
    import doctest
    aa= False
    aa= True
    doctest.testmod(verbose=aa)