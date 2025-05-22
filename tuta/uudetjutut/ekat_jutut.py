


def calcs():

	'''

	Laske muuttuva yksikkökustannus tuotteille, joita Biohajotus Oy alkaisi valmistaa sopimusten toteutuessa.

	Yksikkö: €/tynnyri - Syötä vastaus yhden euron tarkkuudella.

	'''


	# ====================================================================================================
	# ====================================================================================================
	# ====================================================================================================

	# Täytä omat luvut tähän!!!!
	volume_tynnyri = 200 # 200 liter barrel

	asiakkaille_toimitetut_tynnyrit = 1310 # kpl
	myyntihinta_per_kappale = 740 # €/kpl

	myyntikatetuottoprosentti = 0.75 # 75 %

	muut_kustannukset = 329000 # euros

	prosenttimuutos = 0.09 # Tämä on muutos hinnassa tehtävässä 5!!!!

	myyntiedustajan_palkka_vuodessa = 48000

	# ====================================================================================================
	# ====================================================================================================
	# ====================================================================================================

	liikevaihto = myyntihinta_per_kappale * asiakkaille_toimitetut_tynnyrit

	# Here is the thing...

	# yksikkökustannus = kokonaiskustannukset / tuotettujen yksiköiden määrä

	kulut_myynti = liikevaihto * (1 - myyntikatetuottoprosentti)
	# Remember: Here we do NOT include muut_kustannukset!!!!!!!!!!!
	yksikkökustannus = (kulut_myynti) / asiakkaille_toimitetut_tynnyrit
	print("Yksikkökustannus: "+str(yksikkökustannus))

	# Laske mikä sopimusten toteutuessa on tuotteen kriittinen myyntihinta.

	# Kriittinen myyntihihta, kun määrä vakio, on P = F / Q + C , missä P on hinta C muuttuva kustannus kappaleelta Q kappalemäärä ja F kiinteät kustannukset

	# C = muut_kustannukset / asiakkaille_toimitetut_tynnyrit + kulut_myynti / asiakkaille_toimitetut_tynnyrit

	C = kulut_myynti / asiakkaille_toimitetut_tynnyrit # This is assumed to stay constant

	P = muut_kustannukset / asiakkaille_toimitetut_tynnyrit + kulut_myynti / asiakkaille_toimitetut_tynnyrit
	assert P <= myyntihinta_per_kappale # We should sell at a profit
	print("Kriittinen myyntihinta: "+str(P))

	# Ok, so this far we should be correct...

	# Laske mikä sopimusten toteutuessa on tuotteen kriittinen myyntimäärä.

	# Kun hinta vakio, kriittinen myyntimäärä on Q = F / (P - C)

	Q = muut_kustannukset / (myyntihinta_per_kappale - C)
	print("Kriittinen myyntimäärä: "+str(Q))

	# Now calculate this bullshit here: Laske paljonko tyypillisen toimintavuoden käyttökate (EBITDA) olisi jos sopimusehdotukset toteutuvat.


	'''

	 Liikevaihto
	- Myytyjen tuotteiden materiaalikustannus
	= Myyntikate
	- Liiketoiminnan muut kustannukset
	= Käyttökate (EBITDA)

	'''

	käyttökate = liikevaihto - kulut_myynti - muut_kustannukset

	print("Käyttökate: "+str(käyttökate))

	# Neuvottelujen aikana tuotteiden myyntihinta saa ison roolin, ja Biohajotus Oy päätyy harkitsemaan sen tiputtamista suunnitelman toteutumisen takaamiseksi. Eräs asiakasyritys on jo tarjoutunut ostamaan koko tulevien vuosien tuotannon, jos hintaa lasketaan riittävästi. Uudessa sopimusehdotuksessa myyntihinta/tuote olisi 9 % alkuperäistä arviota pienempi, mutta myyntimäärä, tuotteen yksikkökustannus, ja liiketoiminnan muut kustannukset olisivat alkuperäisen arvion mukaisia. 

	# Laske mikä Biohajotus Oy:n myyntikatetuottoprosentti olisi uudella myyntihinnalla.

	# We have to essentially work backwards here.

	# myyntikateprosentti = myyntikate / liikevaihto * 100 # so we need to calculate the new myyntikate and liikevaihto

	uusi_hinta = myyntihinta_per_kappale * (1 - prosenttimuutos) # add the 9 % here...
	uusi_liikevaihto = uusi_hinta * asiakkaille_toimitetut_tynnyrit

	'''
		 Liikevaihto
	- Myytyjen tuotteiden materiaalikustannus
	= Myyntikate
	'''
	# kulut_myynti = liikevaihto * (1 - myyntikatetuottoprosentti)

	# uusi_kulut_myynti = uusi_liikevaihto * (1 - myyntikatetuottoprosentti)
	uusi_myyntikate = uusi_liikevaihto - kulut_myynti # We assume selling costs do not change....

	uusi_myyntikateprosentti = uusi_myyntikate / uusi_liikevaihto

	print("Uusi myyntikateprosentti: "+str(uusi_myyntikateprosentti))

	# Laske polttoainetynnyreille uuden myyntihinnan mukainen kriittinen myyntimäärä.

	# Kun hinta vakio, kriittinen myyntimäärä on Q = F / (P - C)

	Q_uusi = muut_kustannukset / (uusi_hinta - C)
	print("Uusi kriittinen myyntimäärä: "+str(Q_uusi))

	# Laske mikä Biohajotus Oy:n tyypillisen vuoden käyttökate olisi, jos uusi sopimusehdotus hyväksytään?

	'''
	 Liikevaihto
	- Myytyjen tuotteiden materiaalikustannus
	= Myyntikate
	- Liiketoiminnan muut kustannukset
	= Käyttökate (EBITDA)

	'''

	vuoden_uusi_käyttökate = uusi_liikevaihto - kulut_myynti - muut_kustannukset

	print("Uusi käyttökate: "+str(vuoden_uusi_käyttökate))

	'''
	
	Hintakysymyksen käydessä hankalaksi omistajat toteavat tavoitteiden saavuttamisen todennäköisesti olevan mahdollista myös tekemällä osan sopimuksista nyt, ja neuvottelemalla loput valmiiksi tilikauden edetessä. Tällöin hintaa ei tarvitsisi laskea alkuperäisestä ehdotuksesta, mutta muut kulut nousisivat. Arvion mukaan riittävän asiakasmäärän kerääminen edellyttäisi ylimääräisen myyntiedustajan palkkaamista, ja tämä maksaisi yritykselle 48000 €.

	Biohajotus Oy päättää palkata uuden myyntiedustajan. Laske montako tuotetta enemmän yrityksen olisi myytävä, jotta päätös ei vaikuttaisi tilikauden tulokseen.

	'''

	# myyntiedustajan_palkka_vuodessa

	# Just solve the equation myyntiedustajan_palkka_vuodessa = (tuotto_per_tynnyri * x)   where x is the number of barrels.

	tuotto_per_tynnyri = myyntihinta_per_kappale - (kulut_myynti / asiakkaille_toimitetut_tynnyrit) # Use the original price here.
	assert tuotto_per_tynnyri >= 0.0 # Sanity checking
	print("Tuotto per tynnyri alkuperäisen sopimuksen mukaisesti: "+str(tuotto_per_tynnyri))

	# Now solve

	tuotetta_enemmän = myyntiedustajan_palkka_vuodessa / tuotto_per_tynnyri

	print("Montako tuotetta enemmän yrityksen olisi myytävä, jotta päätös ei vaikuttaisi tilikauden tulokseen? : "+str(tuotetta_enemmän))
	return

