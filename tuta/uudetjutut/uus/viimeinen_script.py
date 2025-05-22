# Tehtävän vakioluvut, täytä tähän omasi!!!!!!!

# ====================================================================================================
# ====================================================================================================
# ====================================================================================================

# !!!!! Omat arvot tähän kohtaan !!!!!

tuotannon_aloittamisen_kustannus = 330000 # euros
myyntimäärä_litraa = 120000 # liters
vuosittainen_kasvu = 0.057 # 5.7 percent
myyntihinta_per_litra = 3.73 # euros / litre
raaka_ainekustannukset = 1.25 # euros / produced litre
muut_kustannukset = 170000 # euros / year
tuottovaatimus = 0.095 # 9.5 %
tuotantolaitteiston_elinikä = 5 # 5 years
yhteisövero = 0.2 # 20 %
uusi_tuottovaade = 0.118 # Uusi tuottovaade kysymyksessä 12
uusi_kasvuprosentti = 0.019 # Uusi kasvuprosentti kysymyksessä 12
tuotantolaitteiston_myyntihinta_tehtävässä_12 = 198000 # Tuotantolaitteiston myyntihinta tehtävässä 12
vuodet_jaljella = 2 # Vuodet, jotka on tehtävässä 12 jäljellä, kun talous kääntyy laskusuhdanteeseen...


# ====================================================================================================
# ====================================================================================================
# ====================================================================================================







# These are just some basic numbers for now


investoinnit = 0 # we do not do investments during PRODUCTION YEARS!!!

liikevaihto = myyntimäärä_litraa * myyntihinta_per_litra
myytyjen_tuotteiden_materiaalikustannus = myyntimäärä_litraa * raaka_ainekustannukset
käyttökate = liikevaihto - myytyjen_tuotteiden_materiaalikustannus - muut_kustannukset

vuotuiset_poistot = tuotannon_aloittamisen_kustannus / tuotantolaitteiston_elinikä # Poistot joka vuodelta. Tämä on tuotantolaitteiston kustannus jaettuna vuosien määrä




# This here is to decide wether we should continue or sell.

def evaluate_continue_or_sell(last_known_volume, myyntihinta_per_litra, raaka_ainekustannukset, muut_kustannukset,
							  yhteisövero, poistot, WACC_new, kasvuprosentti_uusi, years_left=3):

	npv_continue = 0
	volume = last_known_volume

	for t in range(1, years_left + 1):
		volume *= (1 + kasvuprosentti_uusi)
		revenue = volume * myyntihinta_per_litra
		materials = volume * raaka_ainekustannukset
		ebitda = revenue - materials - muut_kustannukset
		ebit = ebitda - poistot
		tax = ebit * yhteisövero
		fcf = ebit * (1 - yhteisövero) + poistot
		npv_continue += fcf / (1 + WACC_new)**t

	return npv_continue


def evaluate_sale(sale_price, WACC_new):
	# t=1 because payment is end of year 3
	return sale_price / (1 + WACC_new)**1

def sum_term(WACC, FCF_t, t):
	return FCF_t / (1 + WACC)**t

def toinen_sivu():

	# Let's first establish some basic numbers first...

	# Let's also calculate the liikevoitto for now...

	'''
	Liikevaihto
	- Myytyjen tuotteiden materiaalikustannus
	= Myyntikate
	- Liiketoiminnan muut kustannukset
	= Käyttökate (EBITDA)
	- Poistot
	= Liikevoitto (EBIT)
	'''

	liikevoitto = käyttökate - vuotuiset_poistot

	# Taxes is just the liikevoitto times the percentage

	verot = liikevoitto * yhteisövero

	'''
	 Liikevaihto
	- Myytyjen tuotteiden materiaalikustannus
	= Myyntikate
	- Liiketoiminnan muut kustannukset
	= Käyttökate (EBITDA)
	'''

	# Laske uuden tuotteen käyttökatetuotto-% tilikaudella 1

	# käyttökatetuotto = Käyttökate / liikevaihto

	käyttökatetuotto = käyttökate / liikevaihto

	print("Käyttökatetuotto (%): "+str(käyttökatetuotto*100))

	# Laske ensimmäisen tuotantovuoden vapaa kassavirta.

	# Vapaa kassavirta = Käyttökate – Investoinnit – Verot



	vapaa_kassavirta = käyttökate - investoinnit - verot

	print("Vapaa kassavirta: "+str(vapaa_kassavirta))

	# Laske investoinnin nettonykyarvo.

	'''
	Investoinnin nettonykyarvo saadaan ylläolevan kaavan
	mukaisesti:
	(1) arvioimalla kaikki sen synnyttämät tulevat vapaat
	rahavirrat kausikohtaisesti
	(2) diskonttaamalla kunkin kauden vapaan rahavirran
	nykyarvoiseksi
	(3) summaamalla nämä nykyarvot yhteen
	Alkuinvestointi huomioidaan nykyhetkessä (t=0) toteutuvana
	negatiivisena rahavirtana
	'''

	# So the sum from t = 0 to 5 years of FCF_t / (1 + WACC)**t where t is the year.

	FCF_0 = -1*tuotannon_aloittamisen_kustannus # This is the cost of the initial investment...

	# Now we just sum all of the stuff.

	WACC = tuottovaatimus # This is just the tuottovaatimus

	# Now calculate the FCF_t for each t=1...5

	# To calculate FCF_t we need liikevoitto

	'''

	Liikevoitto × (1 - Tuloveroprosentti)
	+ Poistot
	+ Käyttöpääoma kauden alussa
	- Käyttöpääoma kauden lopussa
	+ Investointien rahavirta
	= Vapaa rahavirta (FCF)

	'''

	# Now we can just ignore the käyttöpääoma, because it doesn't change from year to year. Also same with the investments cashflow

	# FCF_t = (liikevoitto) * (1 - yhteisövero) + vuotuiset_poistot #  + käyttöpääoma_kauden_alussa - käyttöpääoma_kauden_lopussa + investointien_rahavirta # We can safely ignore these.

	# NPV = sum(sum_term(WACC, FCF_t, t) for t in range(1,6)) + sum_term(WACC, FCF_0, 0) # 1 2 3 4 and 5
	# print("NPV (Nettonykyarvo): "+str(NPV))


	npv = FCF_0  # start with investment at year 0

	for t in range(1, tuotantolaitteiston_elinikä + 1):
		# Calculate sales volume for year t
		myyntimäärä_litraa_t = myyntimäärä_litraa * ((1 + vuosittainen_kasvu) ** (t - 1))

		# Calculate revenues and costs for year t
		liikevaihto_loop = myyntimäärä_litraa_t * myyntihinta_per_litra
		materiaalikustannukset = myyntimäärä_litraa_t * raaka_ainekustannukset

		# Käyttökate = liikevaihto - materiaalikustannukset - muut_kustannukset
		käyttökate_loop = liikevaihto - materiaalikustannukset - muut_kustannukset

		# Liikevoitto = käyttökate - poistot
		liikevoitto_loop = käyttökate_loop - vuotuiset_poistot

		# Verot = liikevoitto * vero
		verot_loop = liikevoitto * yhteisövero

		# Vapaat kassavirrat FCF = liikevoitto*(1 - vero) + poistot
		FCF_t_loop = liikevoitto * (1 - yhteisövero) + vuotuiset_poistot

		# Discount and add to npv
		npv += FCF_t_loop / (1 + tuottovaatimus)**t

	print("NPV: "+str(npv))

	# Question 12 (this was by far the hardest part in the entire thing...)

	# ===================== Add this to your main function =====================

	# Last known sales volume = volume at end of year 2
	myyntimäärä_year2 = myyntimäärä_litraa * (1 + vuosittainen_kasvu)**1

	npv_continue = evaluate_continue_or_sell(
		last_known_volume=myyntimäärä_year2,
		myyntihinta_per_litra=myyntihinta_per_litra,
		raaka_ainekustannukset=raaka_ainekustannukset,
		muut_kustannukset=muut_kustannukset,
		yhteisövero=yhteisövero,
		poistot=vuotuiset_poistot,
		WACC_new=uusi_tuottovaade,
		kasvuprosentti_uusi=uusi_kasvuprosentti
	)

	npv_sell = evaluate_sale(tuotantolaitteiston_myyntihinta_tehtävässä_12, uusi_tuottovaade)

	# Answers to questions 12 and 13

	print("Jatkamisen NPV: "+str(npv_continue))
	print("Tuotannon lopettamisen NPV: "+str(npv_sell))

	return


'''

Virhe ennusteessa

Investoinnin myötä alkanut EkopoltePlus-tuotanto on nyt ollut käynnissä kaksi vuotta, ja investoinnin kolmas tilikausi on juuri alkamassa. Myyntimäärät vastasivat odotuksia vuosina 1 ja 2, mutta markkinat ovat kääntyneet laskusuhdanteeseen. Vuosille 3-5 ennustetaan huomattavasti heikompaa, 1.9 % kasvua. Muutokset yrityksen rahoitusrakenteessa ovat myös vaikuttaneet tuottovaateisiin siten, että pääoman keskimääräinen tuottovaade on 11.8 %.

Eräs energiateollisuusalan johtava korporaatio on jo pitkään ollut kiinnostunut Biohajotus Oy:n teknologiasta, ja on jopa harkinnut yrityksen ostamista. Korporaatio haluaa kuitenkin ensin testata Biohajotus Oy:n uutta tekniikkaa tuotannon skaalautuvuuden varmistamiseksi, ja tarjoutuu ostamaan EkopoltePlus-tuotantolaitteiston ensi vuoden alussa, käypään 198000 € hintaan (mikä sattumalta vastaa sen tämänhetkistä arvoa taseessa, eli myynnillä ei olisi verovaikutusta). Kauppojen ehtona kuitenkin on, että maksu suoritetaan vasta tilikauden 3 lopussa kun laitteisto on integroitu jalostamoon ja sen käyttö alkaa.

Biohajotus Oy:n likviditeetti on tyydyttävällä tasolla, mutta jo suunnitteilla oleva seuraava prototyyppi syö tutkimusbudjettia nopeasti. Pitääkseen rahoitustilanteen mahdollisimman vakaana omistajat haluavat varmistaa tekevänsä valinnan, joka maksimoi EkopoltePlus-investoinnin tuottamat tulevat rahavirrat.

Biohajotus Oy voi siis joko jatkaa tuotantoa heikentyneessä tilanteessa, tai lopettaa EkopoltePlussan tuotannon ja myydä siihen liittyvät tuotantolaitteistot.

'''


if __name__=="__main__":
	# calcs()
	toinen_sivu()
	exit(0)

