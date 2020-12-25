#!/usr/bin/python3.8
# -*- coding: utf-8 -*-

# Ce fichier abrite le code du jeu Casino

from math import ceil
from random import randrange

#Déclaration des variables
Argent = 5000
Continuer_partie = True

print("Vous vous installez à la table de roulette avec",Argent,"$")

while Continuer_partie:#tant qu'on doit continuer la partie
  pari = -1
  while pari == -1:
      Numero = input("Sur quel numéro voulez vous parier entre 0 et 49 ? : ")	
      try:
      	Numero = int(Numero)
      	assert Numero > -1 and Numero < 50
      except AssertionError:
        print("Votre numéro n'est pas compris entre 0 et 49 \nVeuillez changer de numéro s'il vous plait")
        continue
      pari += (Numero+1)
      print ("Vous avez parié sur le numéro", Numero,".","Passons à l'argent que vous voulez miser")
  
  mise = 0
  while mise == 0:
        argent_mise = input("Votre mise: ")
        try:
          argent_mise = int(argent_mise)
          assert argent_mise > 0 and argent_mise <= Argent
        except AssertionError:
          print ("Vous ne pouvez pas parier cette somme \nSoit vous n'avez pas assez d'argent, soit votre mise n'est pas supérieure à 0$ \nVeuillez modifier votre mise s'il vous plait")
          continue
        mise += argent_mise
        print ("Vous avez misé", argent_mise, "$ \nIl est temps de lancer la roulette !\nC'est parti, les jeux sont faits, rien ne va plus........ ")
        result = randrange(50)
        print ("Et le numéro gagnant est ...", result,"!")
  if result==Numero:
          Argent += argent_mise*3
          print ("Bravo ! Votre Numéro","(", Numero,")","et le résultat du lancé","(",result,") sont identiques ! \nVous remportez 3 fois votre mise\nCela correspond à", (argent_mise*3),"$")
          print ("Votre cagnotte s'élève donc à", Argent,"$")
  elif result%2!=0 and Numero%2!=0:
          Argent += ceil(argent_mise/2)
          print ("Bravo !", Numero, "et", result, "sont des nombres impairs \nVous remportez la moitiée de votre mise\nCela correspond à", ceil(argent_mise/2),"$")
          print ("Votre cagnotte s'élève donc à", Argent,"$")
  elif result%2==0 and Numero%2==0:
          Argent += ceil(argent_mise/2)
          print ("Bravo !", Numero, "et", result, "sont des nombres pairs \nVous remportez la moitiée de votre mise\nCela correspond à", ceil(argent_mise/2),"$")
          print ("Votre cagnotte s'élève donc à", Argent,"$")
  else :
          Argent -= argent_mise
          print ("Manque de chance, vous avez perdu !\nVotre mise est récupérée par le croupier \n Votre cagnote s'élève donc à",Argent,"$")
                 
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
                print ("Vous avez décidé de quitter la partie\nMerci à vous\nNous espérons vous revoir très vite")
                

          
  	
	