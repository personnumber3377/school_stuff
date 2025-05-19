
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

if __name__=="__main__":
	calcs()
	exit(0)
