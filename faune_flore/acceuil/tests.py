import csv
from .models import Plante
with open('C:\\Users\\rouan\\OneDrive\\Bureau\\Projet\\Full_DNP_YE2.csv') as csvfile:
	spamreader = csv.reader(csvfile,delimiter=';')
	for column in spamreader:
			_,created = Sujet.objects.update_or_create(
				InChIKey=column[1],
        	    nom_commun=column[0]
            	)