
'''

Yritys on toimittanut tuotteita 8600 eurolla. Näiden tuotteiden materiaalikustannukset ovat 5400 euroa. Yrityksen palkat, vuokrat ja sähköt ovat yhteensä 1300 euroa. Yrityksen investointien määrä on 2800 euroa ja kaikki nämä investoinnit poistetaan 5:ssä vuodessa tasapoistona. Vuotuinen poisto on näin ollen 560. Yrityksellä on velkaa 2700 euroa , josta se maksaa korkoa 5% vuodessa. Yhteisövero on 20%.

Kuinka paljon on yrityksen käyttökate euroina?

'''

def s():
	# First calculate the liikevaihto:

	liikevaihto = 8600 # euros
	# Then reduce all of the costs and stuff
	velat = 2700
	vuosikorko = 0.05
	materiaalikulut = 5400
	muut_kulut = 1300
	# poistot = 560


	käyttökate = liikevaihto - materiaalikulut - muut_kulut #  - poistot
	print("Käyttökate: "+str(käyttökate))

	# Paljonko yrityksen pitää maksaa korkoja tilikaudella euroina? 

	korot_per_vuosi = velat * vuosikorko

	print("Korot vuodessa: "+str(korot_per_vuosi))

	# Paljonko on yrityksen tilikauden tulos euroina?

	

	tilikauden_tulos = 

	return

if __name__=="__main__":
	s()
	exit(0)
