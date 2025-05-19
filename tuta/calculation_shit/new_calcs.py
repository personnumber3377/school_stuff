
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

	vaihto_omaisuus_alussa = raaka_ainevarasto_alussa + valmisvarasto_yksiköt_alussa * ostohinta_annos

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

	maksetut_verot = (liikevoitto - korot_tilikauden_aikana) * (yhteisövero)

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

	# vaihto_omaisuus_lopussa = raaka_ainevarasto_lopussa + valmisvarasto_yksiköt_lopussa * myyntihinta

	# We actually want to use the buying price here.

	vaihto_omaisuus_lopussa = raaka_ainevarasto_lopussa + valmisvarasto_yksiköt_lopussa * ostohinta_annos

	käyttöpääoma_lopussa = vaihto_omaisuus_lopussa + myyntisaamiset_lopussa - ostovelat_lopussa

	# käyttöpääoma_alussa should be correct

	käyttöpääoman_muutos = käyttöpääoma_lopussa - käyttöpääoma_alussa

	print("d_käyttöpääoma: "+str(käyttöpääoman_muutos))

	assert käyttöpääoman_muutos == -79800

	# Laske yrityksen tilikauden liiketoiminnan rahavirta CFops.

	# CFops = Liikevoitto (EBIT)+Poistot−Maksetut verot−Käyttöpääoman muutos

	# CF_ops = liikevoitto + tilikauden_poistot - maksetut_verot - käyttöpääoman_muutos

	# Liiketoiminnan rahavirta = Käyttökate + Käyttöpääoma tilikauden alussa - Käyttöpääoma tilikauden lopussa - korot - verot

	CF_ops = käyttökate + käyttöpääoma_alussa - käyttöpääoma_lopussa - korot_tilikauden_aikana - maksetut_verot

	print("CF_ops: "+str(CF_ops))

	# Rahavarojen muutos = Liiketoiminnan rahavirta + Investointien rahavirta + Rahoituksen rahavirta 


	# Rahavarojen muutos

	rahavarojen_muutos = CF_ops + CF_inv + CF_fin

	print("Rahavarojen muutos: "+str(rahavarojen_muutos))

	# rahoitusomaisuus = rahat ja pankkisaamiset + myyntisaamiset

	# rahoitus_omaisuus_alussa

	rahat_ja_pankkisaamiset_lopussa = rahat_ja_pankkisaamiset_alussa + rahavarojen_muutos # Assume no change


	rahoitus_omaisuus_lopussa = rahat_ja_pankkisaamiset_lopussa + myyntisaamiset_lopussa

	# rahat_ja_pankkisaamiset_lopussa = alussa + rahavarojen_muutos

	d_rahoitusomaisuus = rahoitus_omaisuus_lopussa - rahoitus_omaisuus_alussa

	print("d_rahoitusomaisuus: "+str(d_rahoitusomaisuus))

	# Laske päättävän taseen loppusumma.

	# Päättävän taseen loppusumma=Pysyvät vastaavat+Vaihtuvat vastaavat+Rahoitusomaisuus

	# Now do the shit here...

	# Pysyvät vastaavat

	pysyvät_vastaavat = käyttöomaisuus_lopussa

	'''
	The vaihtuvat vastaavat are essentially these

	Vaihtuvat vastaavat:
	- Raaka-ainevarasto:           40 000 €
	- Valmisvarasto:               96 000 €
	- Myyntisaamiset:              39 000 €
	- Rahat ja pankkisaamiset:    190 000 €

	# Actually I think we need to use this formula here instead:

	 Kertynyt tulos avaavassa taseessa
	+ Tilikauden tulos avaavassa taseessa
	- Jaetut osingot
	= Kertynyt tulos päättävässä taseessa 

	

	'''

	kertynyt_tulos_avaavassa_taseessa = 0 # Taken verbatim...

	# 	- Tilikauden tulos	100000

	# tilikauden_tulos

	# vaihtuvat_vastaavat_lopussa = raaka_ainevarasto_lopussa + valmisvarasto_yksiköt_lopussa * ostohinta_annos + myyntisaamiset_lopussa + rahat_ja_pankkisaamiset_lopussa

	# päättävän_taseen_loppusumma = pysyvät_vastaavat + vaihtuvat_vastaavat_lopussa + rahoitus_omaisuus_lopussa



	'''
	original_tulos = 100000
	print("kertynyt_tulos_avaavassa_taseessa: "+str(kertynyt_tulos_avaavassa_taseessa))
	print("tilikauden_tulos: "+str(tilikauden_tulos))
	print("maksetut_osingot: "+str(maksetut_osingot))

	kertynyt_tulos_päättävässä_taseessa = kertynyt_tulos_avaavassa_taseessa + original_tulos - maksetut_osingot
	
	'''

	vaihtuvat_vastaavat_alussa = raaka_ainevarasto_alussa + valmisvarasto_yksiköt_alussa * ostohinta_annos + myyntisaamiset_alussa + rahat_ja_pankkisaamiset_alussa


	vaihtuvat_vastaavat_lopussa = raaka_ainevarasto_lopussa + valmisvarasto_yksiköt_lopussa * ostohinta_annos + myyntisaamiset_lopussa + rahat_ja_pankkisaamiset_lopussa

	# Laske päättävän taseen loppusumma. = kaikki vastattavat = kaikki vastaavat

	kertynyt_tulos_päättävässä_taseessa = pysyvät_vastaavat + vaihtuvat_vastaavat_lopussa # Kaikki vastaavat 

	päättävä_tase = kertynyt_tulos_päättävässä_taseessa

	# Vastaavat yhteensä tai vastattavat yhteensä

	# print("100000 - 55000 == "+str(100000 - 55000))


	'''
	print("kertynyt_tulos_päättävässä_taseessa: "+str(kertynyt_tulos_päättävässä_taseessa))

	# Now calculate ROCE: ROCE = liikevoitto / (oma pääoma + korolliset velat)

	# Now calculate the aloittava_tase (this assumes the similar format to päättävä_tase)

	aloittava_tase = pysyvät_vastaavat + vaihtuvat_vastaavat_alussa

	aloittavan_ja_päättävän_taseen_keskiarvo = (aloittava_tase + päättävä_tase) / 2
	'''


	# average_sijoitettu_paaoma = (oma_pääoma_alussa + korolliset_velat_alussa + oma_paaoma_lopussa + korolliset_velat_lopussa) / 2

	# kaikki_lainat_alussa

	# Oma pääoma alussa = Osakepääoma + Kertynyt tulos (from previous years)

	oma_pääoma_alussa = osakepääoma + kertynyt_tulos_avaavassa_taseessa

	oma_pääoma_lopussa = osakepääoma + kertynyt_tulos_päättävässä_taseessa

	average_sijoitettu_paaoma = (oma_pääoma_alussa + kaikki_lainat_alussa + oma_pääoma_lopussa + kaikki_lainat_lopussa) / 2 # (oma_pääoma_alussa + kaikki_lainat_alussa + oma_pääoma_lopussa + kaikki_lainat_lopussa) / 2

	# ROCE = liikevoitto / (average_sijoitettu_paaoma) * 100

	'''
	 Osakepääoma
	+ Kertynyt tulos
	+ Laskettavan tilikauden tulos
	= Oma pääoma

	'''

	# ROCE = liikevoitto / ()	



	# oma_pääoma_paska = osakepääoma + kertynyt_tulos + tilikauden_tulos

	# oma_pääoma_paska = osakepääoma + kertynyt_tulos_päättävässä_taseessa + tilikauden_tulos


	# oma_pääoma_lopussa

	# pääoma_keskiarvo = (oma_pääoma_lopussa + oma_pääoma_alussa) / 2

	# print("ROCE: "+str(ROCE))

	# ROCE = liikevoitto / (päättävä_tase - ostovelat_lopussa)
	# lainat_keskiarvo = (kaikki_lainat_alussa + kaikki_lainat_lopussa) / 2
	# ROCE = liikevoitto / (oma_pääoma_lopussa + kaikki_lainat_lopussa)

	# fuck = oma_pääoma_lopussa + oma_pääoma_alussa + kaikki_lainat_alussa + kaikki_lainat_lopussa



	# fuck = fuck / 2 # Get average stuff..

	pääoma_paska = (oma_pääoma_alussa + oma_pääoma_lopussa) / 2



	# lainat_keskiarvo

	# päättävä_tase+ 



	# ROCE = liikevoitto / (fuck) * 100

	ROCE = liikevoitto / (kaikki_lainat_lopussa + pääoma_paska) * 100

	print("ROCE: "+str(ROCE))


	return

if __name__=="__main__":
	calcs()
	exit(0)
