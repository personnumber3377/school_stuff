
def calcs():
	# Do the calculations here...
	# Mikä on yrityksen vaihto-omaisuus avaavassa taseessa?

	käyttöomaisuus_alussa = 800000
	raaka_ainevarasto_alussa = 40000
	valmisvarasto = 96000
	valmisvarasto_yksiköt_alussa = 120000

	myyntisaamiset_alussa = 39000
	rahat_ja_pankkisaamiset_alussa = 190000

	#  Vieraan pääoman tuottovaade vastaa korkoa, kun taas oman pääoman tuottovaade on 12 %

	tuottovaade = 0.12 # 12%


	osakepääoma = 555400
	kertynyt_tulos = 0
	tilikauden_tulos = 100000
	pitkäaikaiset_lainat = 350000
	lyhytaikaiset_lainat = 150000

	kaikki_lainat = pitkäaikaiset_lainat + lyhytaikaiset_lainat

	kaikki_lainat_alussa = kaikki_lainat

	ostovelat_alussa = 9600

	yksiköt_varastossa_alussa = 50000  # "Tilikauden alussa yrityksellä on varastossa 50000 annosta raaka-ainetta."
	
	ostohinta_annos = 0.8 # 80 snt / annos

	# This here should match always

	assert valmisvarasto == valmisvarasto_yksiköt_alussa * ostohinta_annos # Should match

	tilikauden_poistot = 200000 # Do the stuff here...

	vuosikorko = 0.06 # 6%

	yhteisövero = 0.2 # 20%



	# Here is what happens during the year...

	# Liiketoiminnan muut kustannukset ovat yhteensä 300000 €, joista 240000 € muodostuu henkilöstökuluista ja loput 60000 € jalostuskoneiston ylläpitokuluista sekä logistiikastakuluista. 

	maksetut_osingot = 55000 # Maksetut osingot for now...

	henkilöstökulut = 240000

	kone_ja_logistiikkakulut = 60000 

	muut_kulut = henkilöstökulut + kone_ja_logistiikkakulut

	assert muut_kulut == 300000 # Known value for now...



	myyntihinta = 3.9 # 3.9 eur / litra

	investointi_tuotantolaitteistoon = 150000 # Tuotantolaitteistoon

	ostetut_annokset = 80000 # 80000 annosta ostettu tilikauden aikana...

	jalostetut_litrat = 90000 # How many liters of the shit we do...

	# Ekopoltetta myös myydään 200000 litraa, keskimääräiseen myyntihintaan 3.9 €/litra.

	myyntimäärä_yksiköt = 200000

	# This is at the end of the year:

	# Yrityksellä on tilikauden lopussa myyntisaamisia 52000 € edestä, ja ostovelkoja 6400 € edestä. Yritys maksaa erääntyvät lainat tilikauden lopussa, ja nostaa samalla uutta lainaa yhteensä 100000 € edestä. Seuraavalla tilikaudella erääntyvää lainaa on 125000 €. Koko lainapääoman keskimääräinen vuosikorko on 6 %. Vieraan pääoman tuottovaade vastaa korkoa, kun taas oman pääoman tuottovaade on 12 %. Tilikauden poistot ovat 200000 € ja yritys investoi tilikauden aikana uuteen tuotantolaitteistoon 150000 € edestä. Omistajilleen Biohajotus Oy maksaa verrattain matalien palkkojen tasapainottamiseksi tilikaudella osinkoja 55000 € edestä. Osakepääoma ei muutu tilikauden aikana. Hinnoissa ei tarvitse huomioida arvonlisäveroa, ja verollisesta tuloksesta maksettava yhteisövero on 20 %. 





	# Yrityksellä on tilikauden lopussa myyntisaamisia 52000 € edestä, ja ostovelkoja 6400 € edestä. Yritys maksaa erääntyvät lainat tilikauden lopussa, ja nostaa samalla uutta lainaa yhteensä 100000 € edestä. Seuraavalla tilikaudella erääntyvää lainaa on 125000 €. Koko lainapääoman keskimääräinen vuosikorko on 6 %. Vieraan pääoman tuottovaade vastaa korkoa, kun taas oman pääoman tuottovaade on 12 %. Tilikauden poistot ovat 200000 € ja yritys investoi tilikauden aikana uuteen tuotantolaitteistoon 150000 € edestä. Omistajilleen Biohajotus Oy maksaa verrattain matalien palkkojen tasapainottamiseksi tilikaudella osinkoja 55000 € edestä. Osakepääoma ei muutu tilikauden aikana. Hinnoissa ei tarvitse huomioida arvonlisäveroa, ja verollisesta tuloksesta maksettava yhteisövero on 20 %. 

	myyntisaamiset_lopussa = 52000
	ostovelat_lopussa = 6400

	# Yritys maksaa erääntyvät lainat tilikauden lopussa, ja nostaa samalla uutta lainaa yhteensä 100000 € edestä. Seuraavalla tilikaudella erääntyvää lainaa on 125000 €.

	maksetut_lainat = lyhytaikaiset_lainat

	otetut_lainat = 100000 

	kaikki_lainat_lopussa = kaikki_lainat


	kaikki_lainat_lopussa -= maksetut_lainat
	kaikki_lainat_lopussa += otetut_lainat

	lyhytaikaiset_lainat_lopussa = 125000

	pitkäaikaiset_lainat_lopussa = kaikki_lainat_lopussa - lyhytaikaiset_lainat_lopussa # We assume that all the loan which is not short term is long term here I think...

	assert kaikki_lainat_lopussa == lyhytaikaiset_lainat_lopussa + pitkäaikaiset_lainat_lopussa

	# print("Uudet lainat: "+str(kaikki_lainat_lopussa))

	# assert kaikki_lainat_lopussa == 125000 # Should be 125000€ worth of loans...

	# Calculate the "Mikä on yrityksen vaihto-omaisuus avaavassa taseessa?"

	# vaihto_omaisuus_alussa = raaka_ainevarasto_alussa + valmisvarasto_yksiköt_alussa * ostohinta_annos

	vaihto_omaisuus_alussa = raaka_ainevarasto_alussa + valmisvarasto_yksiköt_alussa * myyntihinta

	print("Vaihto-omaisuus alussa: "+str(vaihto_omaisuus_alussa))

	# Now we know that the rahoitusomaisuus is defined as the "Rahat - ja pankkisaamiset + myyntisaamiset", so we do that here.

	# Mikä on yrityksen rahoitusomaisuus avaavassa taseessa?

	rahoitus_omaisuus_alussa = rahat_ja_pankkisaamiset_alussa + myyntisaamiset_alussa

	print("Rahoitusomaisuus alussa: "+str(rahoitus_omaisuus_alussa))

	# "Mikä on yrityksen käyttöpääoma avaavassa taseessa?"

	'''
	Vaihto-omaisuus
	+ Myyntisaamiset
	- Ostovelat
	= Käyttöpääoma
	'''

	käyttöpääoma_alussa = vaihto_omaisuus_alussa + myyntisaamiset_alussa - ostovelat_alussa

	print("Käyttöpääoma alussa: "+str(käyttöpääoma_alussa))

	# "Laske tilikauden liikevaihto."

	# To calculate liikevaihto (revenue or turnover), you multiply the amount of product sold by the average selling price per unit.

	liikevaihto = myyntimäärä_yksiköt * myyntihinta

	print("Liikevaihto: "+str(liikevaihto))

	# Laske tilikauden myyntikate.



	myyntikate = liikevaihto - myyntimäärä_yksiköt * ostohinta_annos # We remove the material costs from here.

	print("Myyntikate: "+str(myyntikate))

	# Calculate the käyttökate which is used  for the calculation of liikevoitto

	käyttökate = myyntikate - muut_kulut

	# Laske tilikauden liikevoitto (EBIT).



	'''
	 Liiketoiminnan muut kustannukset
	= Käyttökate (EBITDA)
	- Poistot
	= Liikevoitto (EBIT)
	'''

	liikevoitto = käyttökate - tilikauden_poistot

	print("Liikevoitto: "+str(liikevoitto))

	# Laske tilikauden nettotulos.

	# I think the nettotulos is just "Tilikauden tulos" which is just liikevoitto - korot - verot

	korot_tilikauden_aikana = kaikki_lainat_alussa * vuosikorko

	tilikauden_tulos = (liikevoitto - korot_tilikauden_aikana) * (1 - yhteisövero)

	print("Tilikauden nettotulos: "+str(tilikauden_tulos))

	# Laske yrityksen investointien rahavirta (CFinv) tilikauden ajalta.

	# Investointien rahavirta = Käyttöomaisuus tilikauden alussa - Poistot - Käyttöomaisuus tilikauden lopussa.

	# Now we first need to calculate the käyttöomaisuus at the end

	kaikki_investoinnit = investointi_tuotantolaitteistoon

	# Thanks ChatGPT

	# Käyttöomaisuus (loppu) = Käyttöomaisuus (alku) + Investoinnit – Poistot

	käyttöomaisuus_lopussa = käyttöomaisuus_alussa + kaikki_investoinnit - tilikauden_poistot



	CF_inv = käyttöomaisuus_alussa - tilikauden_poistot - käyttöomaisuus_lopussa

	print("CF_inv: "+str(CF_inv))

	# Laske yrityksen tilikauden rahoituksen rahavirta CFfin

	#  CFfin = Uudet lainat – Lainanlyhennykset – Osingot

	CF_fin = otetut_lainat - maksetut_lainat - maksetut_osingot

	print("CF_fin: "+str(CF_fin))

	# Laske käyttöpääoman muutos tilikauden aikana.

	assert käyttöpääoma_alussa == 165400
	# Let's copy this thing:

	# 	käyttöpääoma_alussa = vaihto_omaisuus_alussa + myyntisaamiset_alussa - ostovelat_alussa

	# Let's copy this thing here:
	# 	vaihto_omaisuus_alussa = raaka_ainevarasto_alussa + valmisvarasto_yksiköt_alussa * ostohinta_annos

	# The final amount is the start amount + bought amount - used amount

	raaka_ainevarasto_lopussa = ( yksiköt_varastossa_alussa + ostetut_annokset - jalostetut_litrat ) * ostohinta_annos

	valmisvarasto_yksiköt_lopussa = valmisvarasto_yksiköt_alussa - myyntimäärä_yksiköt + jalostetut_litrat

	vaihto_omaisuus_lopussa = raaka_ainevarasto_lopussa + valmisvarasto_yksiköt_lopussa * ostohinta_annos

	käyttöpääoma_lopussa = vaihto_omaisuus_lopussa + myyntisaamiset_lopussa - ostovelat_lopussa

	käyttöpääoman_muutos = käyttöomaisuus_lopussa - käyttöpääoma_alussa

	print("d_käyttöpääoma: "+str(käyttöpääoman_muutos))

	return

'''

Jatketaan Biohajotus Oy:n toiminnan tarkastelua katetuottolaskelmallisesta perspektiivistä.

Biohajotus Oy on toistaiseksi myynyt vuosittain vaihtelevia määriä Ekopoltetta, mutta tutkimusbudjetin takaamisen kannalta olisi eduksi, jos myyntimäärät olisivat tasaisempia. Omistajat ovat tämän nojalla aloittaneet neuvottelut pidempiaikaisista sopimuksia joidenkin vakioasiakkaiden kanssa, jotta tulevien vuosien tuotantotahtia olisi helpompi optimoida. Samalla myös kiinteät kustannukset putoaisivat, koska logistiikka yksinkertaistuisi ja asiakashankintaan kuluisi vähemmän työtunteja. Polttoainaemarkkinoilla yleisen standardin mukaisesti tuotteina sopimuksissa toimisivat 200 litran teräksiset polttoainetynnyrit, jotka täytetään Ekopoltteella.

Ensimmäisistä sopimusneuvotteluista palattuaan Biohajotus Oy:n myyntiedustaja toteaa, että tämänhetkisten sopimusehdotusten toteutuessa tyypillisen toimintavuoden luvut näyttäisivät seuraavanlaisilta: asiakkaille toimitettu tynnyrimäärä on 1310 kpl, myyntihinta on 740 €/kpl, myyntikatetuottoprosentti 75 %, ja liiketoiminnan muut kustannukset 329000 €.




'''


def calcs2():

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


if __name__=="__main__":
	# calcs()
	calcs2()
	exit(0)
