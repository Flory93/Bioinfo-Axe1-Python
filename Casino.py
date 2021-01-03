#!/usr/bin/python3.8
# -*- coding: utf-8 -*-

# Ce fichier abrite le code du jeu Casino

from math import ceil
from random import randrange

#Déclaration des variables
Argent = 5000
Continuer_partie = True #Booléen qui est vrai tant qu'on doit continuer la partie

print("Vous vous installez à la table de roulette avec",Argent,"$")

while Continuer_partie:#tant qu'on doit continuer la partie
  pari = -1
  while pari < 0 or pari > 49:
      pari = input("Sur quel numéro voulez vous parier entre 0 et 49 ? : ")	
      try:
      	pari = int(pari) # On convertit le nombre misé
      except ValueError:
        print("Vous n'avez pas saisi de nombre")
        pari = -1
        continue
      if pari < 0:
        print ("Ce nombre est négatif")
      if pari > 49:
        print ("Ce nombre est supérieur à 49")
  
  # A présent on séléctionne la somme à miser sur le nombre
  mise = 0
  while mise <= 0 or mise > Argent:
        mise = input("Tapez le montant de votre mise: ")
        try:
          mise = int(mise)
        except ValueError:
          print ("Vous n'avez pas saisi de nombre")
          continue
        if mise <= 0:
          print ("La mise saisi est négative ou nulle\nVeuillez modifier votre mise")
        if mise > Argent:
          print ("Vous ne pouvez miser autant, vous n'avez que", Argent, "$\nVeuillez modifier votre mise")
  
  #Le nombre misé et la mise ont été sélectionné
  #On fait touner la roulette

  print ("Vous avez misé", mise, "$ \nIl est temps de lancer la roulette !\nC'est parti, les jeux sont faits, rien ne va plus........ ")
  result = randrange(50)
  print ("Et le numéro gagnant est ...", result,"!")
  

  # On établit le gain du joueur
  if result==pari:
          Argent += mise*3
          print ("Bravo ! Votre Numéro","(", pari,")","et le résultat du lancé","(",result,") sont identiques ! \nVous remportez 3 fois votre mise\nCela correspond à", (mise*3),"$")
          print ("Votre cagnotte s'élève donc à", Argent,"$")
  elif result%2 == pari%2: #Ils sont de la même couleur
          Argent += ceil(mise/2)
          print ("Bravo !", pari, "et", result, "sont des nombres impairs \nVous remportez la moitiée de votre mise\nCela correspond à", ceil(mise/2),"$")
          print ("Votre cagnotte s'élève donc à", Argent,"$")
  else :
          Argent -= mise
          print ("Manque de chance, vous avez perdu !\nVotre mise est récupérée par le croupier \n Votre cagnote s'élève donc à",Argent,"$")
  
  # On interrompt la partie si le joueur est ruiné               
  if Argent == 0:
            Continuer_partie = False
            print ("Malheureusement, vous n'avez plus d'argent\nVous devez quitter la table\nRevenez une prochaine fois !")

  elif Argent > 0:
    
    
    décision = "innexistante"
    while décision == "innexistante": 
            reponse = input("Souhaitez vous continuer la partie (oui/non) ?: ")
            try:
              reponse == "oui" or reponse == "non" 
              assert reponse == "oui" or reponse == "non"
            except AssertionError:
              print ("Veuillez répondre par oui ou par non s'il vous plait")
              continue
            décision += reponse
            if reponse == "oui":
                print("La partie continue")
            elif reponse == "non":
                Continuer_partie = False
                print ("Vous avez décidé de quitter la partie\nMerci à vous\nNous espérons vous revoir très vite.")

                #fin du game
                #Corrections Openclassroom
                

          
  	
	