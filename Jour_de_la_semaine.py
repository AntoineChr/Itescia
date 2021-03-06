def dizaine_annee (annee): #Prendre la dizaine et unité de l'année
	total = annee[2] + annee[3]
	total = int(total)
	return total

def div_entiere (total): #Ajouter le quart au total
	total = total + total // 4
	return total

def ajout_jour (jour, total): #Y ajouter le numéro du jour
	total  = total + jour
	return total

def ajout_mois (mois, total): #Y ajouter un nombre en fonction du mois
	if mois == 2 or mois == 3 or mois == 11:
		total = total + 3
	elif mois == 4 or mois == 7:
		total = total + 6
	elif mois == 5:
		total = total + 1
	elif mois == 6:
		total = total + 4
	elif mois == 8:
		total = total + 2
	elif mois == 9 or mois == 12:
		total = total + 5
	return total

def bisex_and_jan_or_fev (annee, total): #Savoir si l'année est bisextile et que le mois est janvier ou février
	annee = int(annee) #Conversion de la variable en int pour effecteur la division ci-desssous
	if (annee%4 == 0 and mois == 1): #Année bisextile si le reste de la division euclidienne de l'année par 4 vaut 0
		total = total - 1
	elif (annee%4 == 0 and mois == 2):
		total = total - 1
	return total

def siecle (annee, total): #Ajouter au total un nombre en fonction du siècle
	if (annee[0] == "1" and annee [1] == "6"):
		total = total + 6
	elif (annee[0] == "1" and annee [1] == "7"):
		total = total + 4
	elif (annee[0] == "1" and annee [1] == "8"):
		total = total + 2
	elif (annee[0] == "1" and annee [1] == "9"):
		total = total + 0
	elif (annee[0] == "2" and annee [1] == "0"):
		total = total + 6
	elif (annee[0] == "2 "and annee [1] == "1"):
		total = total + 4
	return total

def jour_de_la_semaine (total): #Affichage du jour de la semaine en fonction du reste du total
	r = total % 7
	if r == 0:
		print("Le %d / %d / %s était un Dimanche\n" %(jour, mois, annee))
	elif r == 1:
		print("Le %d / %d / %s était un Lundi\n" %(jour, mois, annee))
	elif r == 2:
		print("Le %d / %d / %s était un Mardi\n" %(jour, mois, annee))
	elif r == 3:
		print("Le %d / %d / %s était un Mercredi\n" %(jour, mois, annee))
	elif r == 4:
		print("Le %d / %d / %s était un Jeudi\n" %(jour, mois, annee))
	elif r == 5:
		print("Le %d / %d / %s était un Vendredi\n" %(jour, mois, annee))
	elif r == 6:
		print("Le %d / %d / %s était un Samedi\n" %(jour, mois, annee))
	return

#Demander la date
jour = int(input("Entrez le jour\t"))
mois = int(input("Entrez le mois\t"))
annee = input("Entrez l'année\t")

#Appel des fonctions
total = dizaine_annee (annee)
total = div_entiere (total)
total = ajout_jour (jour, total)
total = ajout_mois (mois, total)
total = bisex_and_jan_or_fev (annee, total)
total = siecle (annee, total)
jour_de_la_semaine (total)