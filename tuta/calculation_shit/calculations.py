






''''

Vaikka biopolttoaineen kysyntä on kasvanut lentokoneiden ympäristöystävällisyyteen liittyvien tekijöiden korostuessa, haluaa yrityksen johto varmistaa, että Biohajotus Oy:n nykyinen liiketoiminta riittää myös tulevien tutkimusinvestointien rahoittamiseen. 

Tarkastellaan tilikautta 1.1.2023 – 31.12.2023. Tilikauden alussa yrityksellä on varastossa 55000 annosta raaka-ainetta. Voidaan olettaa, että 1 annoksella raaka-ainetta voidaan tuottaa 1 annos levää, josta puolestaan voidaan jalostaa 1 litra biopolttoainetta. Kirjanpidon kannalta varastonhallintaa on yksinkertaistettu siten, että välivarastoa ei lasketa, vaan ravinneannoksista tuotettu jalostuskelpoinen levä lasketaan raaka-aineeksi, kunnes se on jalostettu biopolttoaineeksi. Valmistuotevarastossa myyntiä odottaa 170000 litraa käyttökelpoista Ekopoltetta. Tilikauden avaava tase (1.1.2023) näyttää seuraavalta:


Vastaavaa (€) 	 		Vastattavaa (€) 	 
Pysyvät vastaavat 	 		Oma pääoma	 
- Käyttöomaisuus	800000		- Osakepääoma 	624010
Vaihtuvat vastaavat	 		- Kertynyt tulos	0
- Raaka-ainevarasto	47850		- Tilikauden tulos	100000
- Valmisvarasto	147900		Vieras pääoma	 
- Myyntisaamiset	38700		- Pitkäaikaiset lainat	250000
- Rahat ja pankkisaamiset 	100000		- Lyhytaikaiset lainat  	150000
 	 		- Ostovelat	10440

Tilikauden aikana Biohajotus Oy ostaa 70000 annosta raaka-ainetta hintaan 0.87 €/annos. Yritys jalostaa tilikauden aikana raaka-aineesta yhteensä 100000 litraa Ekopoltetta. Ekopoltetta myös myydään 220000 litraa, keskimääräiseen myyntihintaan 3.87 €/litra. Liiketoiminnan muut kustannukset ovat yhteensä 330000 €, joista 264000 € muodostuu henkilöstökuluista ja loput 66000 € jalostuskoneiston ylläpitokuluista sekä logistiikastakuluista. 

Yrityksellä on tilikauden lopussa myyntisaamisia 56760 € edestä, ja ostovelkoja 6090 € edestä. Yritys maksaa erääntyvät lainat tilikauden lopussa, ja nostaa samalla uutta lainaa yhteensä 200000 € edestä. Seuraavalla tilikaudella erääntyvää lainaa on 125000 €. Koko lainapääoman keskimääräinen vuosikorko on 7 %. Vieraan pääoman tuottovaade vastaa korkoa, kun taas oman pääoman tuottovaade on 12 %. Tilikauden poistot ovat 200000 € ja yritys investoi tilikauden aikana uuteen tuotantolaitteistoon 250000 € edestä. Omistajilleen Biohajotus Oy maksaa verrattain matalien palkkojen tasapainottamiseksi tilikaudella osinkoja 80000 € edestä. Osakepääoma ei muutu tilikauden aikana. Hinnoissa ei tarvitse huomioida arvonlisäveroa, ja verollisesta tuloksesta maksettava yhteisövero on 20 %. 

'''

def calcs():
	# Do the calculations here...
	# Mikä on yrityksen vaihto-omaisuus avaavassa taseessa?

	käyttöomaisuus = 800000
	raaka_ainevarasto = 47850
	valmisvarasto = 147900
	myyntisaamiset = 38700
	rahat_ja_pankkisaamiset = 100000

	osakepääoma = 624010
	kertynyt_tulos = 0
	tilikauden_tulos = 100000
	pitkäaikaiset_lainat = 250000
	lyhytaikaiset_lainat = 150000
	ostovelat = 10440

	# yksiköt = 100_000
	myyntimäärä_yksiköt = 220_000
	# tuottohinta_per_yksikkö = 0.87

	raaka_aine_ostohinta = 0.87
	myyntihinta = 3.87

	# henkilöstökulut + kone_ja_logistiikkakulut

	henkilöstökulut = 264000

	kone_ja_logistiikkakulut = 66000

	tilikauden_poistot = 200000 # Do the stuff here...

	vuosikorko = 0.07 # 7%

	yhteisövero = 0.2 # 20%

	# Now do the shit here...

	# Vaihto-omaisuus muodostuu hyödykkeistä, jotka on tarkoitettu myytäviksi eteenpäin. Käytännössä tämä on sama kuin yrityksen varasto, ja se jaetaan osiin valmistusasteen mukaan: aineet ja tarvikkeet, keskeneräinen tuotanto, sekä valmiit tuotteet.

	vaihto_omaisuus = raaka_ainevarasto + valmisvarasto
	print(vaihto_omaisuus)
	assert vaihto_omaisuus == 195750 # This is a known answer...

	# Mikä on yrityksen rahoitusomaisuus avaavassa taseessa?

	# Rahoitusomaisuus sisältää myyntisaamiset ja muut vastaavat saamiset, rahoitusarvopaperit sekä pankkivarat ja pankkisaamiset.

	rahoitusomaisuus = myyntisaamiset + rahat_ja_pankkisaamiset

	print(rahoitusomaisuus)

	assert rahoitusomaisuus == 138700

	# Mikä on yrityksen käyttöpääoma avaavassa taseessa?

	# I don't have a fucking clue for this one here.

	# Laske tilikauden liikevaihto.

	# Just how much product we have sold in euros.

	liikevaihto = myyntimäärä_yksiköt * myyntihinta

	print(liikevaihto)

	assert liikevaihto == 851400

	tuotteiden_tuottohinta = raaka_aine_ostohinta * myyntimäärä_yksiköt

	myyntikate = liikevaihto - tuotteiden_tuottohinta

	print(myyntikate)

	assert myyntikate == 660000

	# Now do some other bullshit here maybe???

	# Laske tilikauden liikevoitto (EBIT).

	muut_kulut = henkilöstökulut + kone_ja_logistiikkakulut

	liikevoitto = myyntikate - muut_kulut - tilikauden_poistot

	print("Liikevoitto: "+str(liikevoitto))

	assert liikevoitto == 130000

	# Nettotulos is just the liikevoitto - rahoituskulut (aka interest on loans)

	lainat_yhteensä = pitkäaikaiset_lainat + lyhytaikaiset_lainat # This here should be 400000€

	maksettu_takaisin_laina = 150_000

	#  Liikevoitosta vähennetään toiminnan rahoittamiseen liittyvät kulut, minkä jälkeen saadaan voitto ennen veroja. Kun siitä vähennetään yrityksen tuloverot, saadaan tuloslaskelman lopputulos eli tilikauden voitto (tai tappio)


	uusi_otettu_laina = 200_000



	# lainat_uudet = lainat_yhteensä - maksettu_takaisin_laina + uusi_otettu_laina
	lainat_uudet = 125_000



	# rahoituskulut_tilikaudelta = (lainat_uudet + lainat_yhteensä) / 2 * 0.07

	rahoituskulut_tilikaudelta = lainat_yhteensä * 0.07

	print("rahoituskulut_tilikaudelta: "+str(rahoituskulut_tilikaudelta))

	tilikauden_nettotulos = (liikevoitto - rahoituskulut_tilikaudelta) * (1 - yhteisövero)

	print(tilikauden_nettotulos)

	print("poopoo")

	# Rahavirtojen (Cash Flow) laskelmat

	# Laske yrityksen investointien rahavirta (CFinv) tilikauden ajalta.

	# Now let us calculate this bullshit here...

	# Investointien rahavirta kertoo, paljonko yritys on käyttänyt rahavaroja liiketoimintaa ylläpitäviin tai kasvattaviin investointeihin.

	# Tilikauden poistot ovat 200000 € ja yritys investoi tilikauden aikana uuteen tuotantolaitteistoon 250000 € edestä. Omistajilleen Biohajotus Oy maksaa verrattain matalien palkkojen tasapainottamiseksi tilikaudella osinkoja 80000 € edestä.

	tuotantolaitteisto_investoinnit = 250000

	# Rahoituksen rahavirta.

	# Rahoituksen rahavirta kertoo, paljonko yritys on tosiasiallisesti maksanut osinkoja, maksanut lainoja takaisin tai turvautunut ulkopuolisiin rahoituslähteisiin.

	osingot = 80_000 # 80k in dividends to employees.

	rahoitukset_rahavirta = uusi_otettu_laina - osingot - lyhytaikaiset_lainat # The business pays back the lyhytaikaiset lainat at the end of the year
	print(rahoitukset_rahavirta)

	# käyttöpääoman muutos

	# Käyttöpääoma=Vaihtuvat vastaavat (current assets)−Lyhytaikaiset velat (current liabilities)

	'''
	In your case, current assets include:

	Raaka-ainevarasto (raw materials inventory)

	Valmisvarasto (finished goods inventory)

	Myyntisaamiset (accounts receivable)

	Rahat ja pankkisaamiset (cash and equivalents)
	'''

	vaihtuvat_vastaavat = raaka_ainevarasto + valmisvarasto + myyntisaamiset + rahat_ja_pankkisaamiset

	käyttöpääoma_alussa = vaihtuvat_vastaavat - (lyhytaikaiset_lainat + ostovelat)

	# Now do the shit...

	print("Käyttöpääoma alussa: "+str(käyttöpääoma_alussa))

	# Now at the end...




	# yksiköt_lopussa = myyntimäärä_yksiköt

	annokset_alussa = 55000
	annoksien_ostomäärä = 70000 
	annoksien_käyttömäärä = 100_000

	annoksien_loppumäärä = annokset_alussa + annoksien_ostomäärä - annoksien_käyttömäärä

	print(annoksien_loppumäärä)

	annoksien_loppumäärän_arvo = annoksien_loppumäärä * raaka_aine_ostohinta

	valmisvarasto_lopussa = 170000

	valmisvarasto_lopussa_arvo = valmisvarasto_lopussa * raaka_aine_ostohinta # myyntihinta

	# Rahat ja pankkisaamiset eivät muutu

	rahat_ja_pankkisaamiset_lopussa = rahat_ja_pankkisaamiset

	lyhytaikaiset_lainat_lopussa = 125000 # Given in text...

	ostovelat_lopussa = 6090
	myyntisaamiset_lopussa = 56760 # This here is given in the text too..


	# Now do the final calculation here...

	# Now replicate what we did in the start here:

	'''
	vaihtuvat_vastaavat = raaka_ainevarasto + valmisvarasto + myyntisaamiset + rahat_ja_pankkisaamiset

	käyttöpääoma_alussa = vaihtuvat_vastaavat - (lyhytaikaiset_lainat + ostovelat)
	'''

	käyttöpääoma_lopussa = annoksien_loppumäärän_arvo + valmisvarasto_lopussa_arvo + myyntisaamiset_lopussa + rahat_ja_pankkisaamiset_lopussa - (lyhytaikaiset_lainat_lopussa + ostovelat_lopussa)

	# Now calculate difference:
	print("annoksien_loppumäärän_arvo: "+str(annoksien_loppumäärän_arvo))
	print("annoksien_loppumäärän_arvo + valmisvarasto_lopussa + myyntisaamiset_lopussa + rahat_ja_pankkisaamiset_lopussa == "+str(annoksien_loppumäärän_arvo + valmisvarasto_lopussa + myyntisaamiset_lopussa + rahat_ja_pankkisaamiset_lopussa))
	print("WC_end: "+str(käyttöpääoma_lopussa))

	d_käyttäpääoma = käyttöpääoma_alussa - käyttöpääoma_lopussa

	print("Käyttöpääoman muutos: "+str(d_käyttäpääoma))



	# Käyttöpääoma is defined as Käyttöpääoma = Vaihto-omaisuus + Myyntisaamiset - Ostovelat

	#  

	# First calculate vaihto-omaisuus alussa

	# Vaihto-omaisuus is defined as Vaihto-omaisuus = Materiaalivarast + Väli- ja valmisvarasto
	# Tilikauden alussa yrityksellä on varastossa 55000 annosta raaka-ainetta.

	materiaalivarasto_alussa = (annokset_alussa * raaka_aine_ostohinta)
	valmisvarasto_alussa = valmisvarasto
	vaihto_omaisuus_alussa = materiaalivarasto_alussa + valmisvarasto

	myyntisaamiset_alussa = 38700

	ostovelat_alussa = 10440

	käyttöpääoma_alussa = vaihto_omaisuus_alussa + myyntisaamiset_alussa - ostovelat_alussa










	# Now calculate the thing at the end...

	# Tilikauden aikana Biohajotus Oy ostaa 70000 annosta raaka-ainetta hintaan 0.87 €/annos. Yritys jalostaa tilikauden aikana raaka-aineesta yhteensä 100000 litraa Ekopoltetta. Ekopoltetta myös myydään 220000 litraa, keskimääräiseen myyntihintaan 3.87 €/litra. Liiketoiminnan muut kustannukset ovat yhteensä 330000 €, joista 264000 € muodostuu henkilöstökuluista ja loput 66000 € jalostuskoneiston ylläpitokuluista sekä logistiikastakuluista. 

	ostetut_annokset = 70_000
	käytetut_annokset = 100_000 # We used up 100 000 units of the stuff in production...

	annokset_lopussa = (annokset_alussa + ostetut_annokset) - käytetut_annokset
	myydyt_annokset = 220000
	valmisvarasto_lopussa = (valmisvarasto_alussa + (käytetut_annokset - myydyt_annokset) * raaka_aine_ostohinta)
	assert valmisvarasto_lopussa >= 0 # Should be nonnegative value...

	materiaalivarasto_lopussa = (annokset_lopussa * raaka_aine_ostohinta)

	# myyntisaamiset_lopussa

	# myyntisaamiset_lopussa

	vaihto_omaisuus_lopussa = materiaalivarasto_lopussa + valmisvarasto_lopussa

	käyttöpääoma_lopussa = vaihto_omaisuus_lopussa + myyntisaamiset_lopussa - ostovelat_lopussa

	print("Difference bullshit: "+str(käyttöpääoma_alussa - käyttöpääoma_lopussa))

	d_käyttöpääoma = int(käyttöpääoma_lopussa - käyttöpääoma_alussa)

	# Now calculate FC_ops

	# I should use this here maybe????

	'''
	
	Käyttökate
	+ Käyttöpääoma kauden alussa
	- Käyttöpääoma kauden lopussa
	- Korot
	- Verot
	= Liiketoiminnan rahavirta

	'''

	# rahoituskulut_tilikaudelta = lainat_yhteensä * 0.07

	# First calculate the käyttökate thing..

	'''
	Liikevaihto
	- Myytyjen tuotteiden materiaalikustannus
	= Myyntikate
	- Liiketoiminnan muut kustannukset
	= Käyttökate (EBITDA)

	'''
	# muut_kulut = henkilöstökulut + kone_ja_logistiikkakulut
	# muut_kustannukset = henkilöstökulut + kone_ja_logistiikkakulut

	muut_kustannukset = 330000 # Given in the text because fuck you
	assert myyntikate == 660000
	käyttökate = myyntikate - muut_kustannukset

	korot = (pitkäaikaiset_lainat + lyhytaikaiset_lainat) * 0.07 # Just interest on the loans we have

	verot = liikevoitto * yhteisövero

	CF_ops = käyttökate + käyttöpääoma_alussa - käyttöpääoma_lopussa - korot - verot # Liiketoiminnan rahavirta = CF_ops

	# Now calculate the stuff here:

	print("CF_ops: "+str(CF_ops))

	'''
	Liiketoiminnan rahavirta kertoo, paljonko yritys on liiketoimintansa avulla pystynyt tuottamaan rahavaroja toimintaedellytysten säilyttämiseen ja uusien investointien tekemiseen, sekä tuoton maksamiseen oman pääoman sijoittajille ja lainojen takaisinmaksuun ulkopuolisiin rahoituslähteisiin turvautumatta. 


	'''

	d_käyttöpääoma = käyttöpääoma_alussa - käyttöpääoma_lopussa

	käyttökate = myyntikate - muut_kustannukset  # your calculation looks good

	korot = (pitkäaikaiset_lainat + lyhytaikaiset_lainat) * 0.07

	verot = liikevoitto * yhteisövero  # this is expense, may not match cash taxes paid exactly

	CF_ops = (660000 - 330000) - (-108090) - ((pitkäaikaiset_lainat + lyhytaikaiset_lainat) * 0.07) - (130000 * 0.2)

	print("CF_ops: ", CF_ops)


	'''
	

	Rahoitusomaisuus koostuu rahoista ja pankkisaamisista sekä tilisaamisista, kuten myyntisaamiset.

	Myyntisaamiset ovat yrityksen taseeseen kirjattavia saatavia, jotka syntyvät, kun asiakas ostaa tavaroita tai palveluja luotolla mutta ei ole vielä maksanut niistä.
	Rahoitusarvopaperit ovat sellaisia likvidejä arvopapereita, jotka ovat nopeasti muutettavissa rahaksi, esimerkiksi julkisesti noteeratut osakkeet.
	Rahavarat ja pankkisaamiset koostuvat yrityksen likvideistä varoista, kuten käteisestä ja pankkitileillä olevista varoista, jotka ovat nopeasti käytettävissä.

	'''

	# rahoitusarvopaperit_alussa = 0
	# rahoitusarvopaperit_lopussa = 851400 # This is because we sold the shit

	rahat_ja_pankkisaamiset_lopussa = rahat_ja_pankkisaamiset + 851400  # This is because we sold the shit (220000 liters * 3.87)

	rahoitusomaisuus_alussa = myyntisaamiset_alussa#  + rahat_ja_pankkisaamiset

	rahoitusomaisuus_lopussa = myyntisaamiset_lopussa#  + rahat_ja_pankkisaamiset_lopussa


	d_rahoitusomaisuus = rahoitusomaisuus_lopussa - rahoitusomaisuus_alussa
	# assert abs(d_rahoitusomaisuus) == abs(56760 - 38700)
	print("d_rahoitusomaisuus: "+str(d_rahoitusomaisuus))


	# Taseen loppusumma on toinen nimitys luvulle vastaavat yhteensä, joka on aina yhtä suuri kuin luku vastattavat yhteensä.

	'''
	Step-by-step:
	Sum all assets at the end of the period:

	Pysyvät vastaavat (Fixed assets / Non-current assets), e.g., käyttöomaisuus (production equipment, machines, etc.)

	Vaihtuvat vastaavat (Current assets):

	Raaka-ainevarasto (Raw material inventory) at end

	Valmisvarasto (Finished goods inventory) at end

	Myyntisaamiset (Accounts receivable) at end

	Rahat ja pankkisaamiset (Cash and bank balances) at end

	Add all these together → this gives Varat loppusumma.

	'''

	raaka_ainevarasto_alussa = 47850

	raaka_ainevarasto_lopussa = 25000 * 0.87 # there are 25000 units of stuff left in the thing...

	valmisvarasto_alussa = 147900

	valmisvarasto_lopussa = valmisvarasto_lopussa_arvo

	varat_alussa = (800000 + raaka_ainevarasto_alussa + valmisvarasto_alussa + myyntisaamiset_alussa + rahat_ja_pankkisaamiset)

	varat_lopussa = (800000 + raaka_ainevarasto_lopussa + valmisvarasto_lopussa + myyntisaamiset_lopussa + rahat_ja_pankkisaamiset_lopussa)


	diff_varat = varat_lopussa - varat_alussa

	d_rahoitusomaisuus += diff_varat

	print("d_rahoitusomaisuus final: "+str(d_rahoitusomaisuus))



	'''
	Rahavarojen muutos
	 Liiketoiminnan rahavirta
	+ Investointien rahavirta
	+ Rahoituksen rahavirta
	= Rahavarojen muutos
	+ Rahat ja pankkisaamiset kauden alussa
	= Rahat ja pankkisaamiset kauden lopussa 
	'''


	rahavarojen_muutes = 










	return

if __name__=="__main__":
	calcs()
	exit(0)
