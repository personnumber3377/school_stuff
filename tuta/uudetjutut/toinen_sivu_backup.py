
'''

Jatketaan Biohajotus Oy:n toiminnan tarkastelua katetuottolaskelmallisesta perspektiivistä.

Biohajotus Oy on toistaiseksi myynyt vuosittain vaihtelevia määriä Ekopoltetta, mutta tutkimusbudjetin takaamisen kannalta olisi eduksi, jos myyntimäärät olisivat tasaisempia. Omistajat ovat tämän nojalla aloittaneet neuvottelut pidempiaikaisista sopimuksia joidenkin vakioasiakkaiden kanssa, jotta tulevien vuosien tuotantotahtia olisi helpompi optimoida. Samalla myös kiinteät kustannukset putoaisivat, koska logistiikka yksinkertaistuisi ja asiakashankintaan kuluisi vähemmän työtunteja. Polttoainaemarkkinoilla yleisen standardin mukaisesti tuotteina sopimuksissa toimisivat 200 litran teräksiset polttoainetynnyrit, jotka täytetään Ekopoltteella.

Ensimmäisistä sopimusneuvotteluista palattuaan Biohajotus Oy:n myyntiedustaja toteaa, että tämänhetkisten sopimusehdotusten toteutuessa tyypillisen toimintavuoden luvut näyttäisivät seuraavanlaisilta: asiakkaille toimitettu tynnyrimäärä on 1310 kpl, myyntihinta on 740 €/kpl, myyntikatetuottoprosentti 75 %, ja liiketoiminnan muut kustannukset 329000 €.




'''


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

'''

Muutaman vuotta myöhemmin tuotantoa on onnistuneesti saatu optimoitua sopimusten mukaisten myyntimäärien ja toimitusaikojen pohjalta. Rahavirrat näyttävät omistajien silmään varsin mukavilta, ja Biohajotus Oy voi nyt keskittyä visionsan kannalta ensisijaisiin laitekehitystavoiteisiinsa. Satsaukset tutkimukseen vaikuttavatkin tuottaneen tulosta, kun vastikään yritykseen palkatun tuotantotalouden diplomi-insinöörin Powerpoint-esitys osoittaa markkinoiden olevan valmis uudelle prototyypille. Laitekehitysosaston mukaan edellisenä vuotena suunnitellulla sargassolevää hyödyntävällä tuotantoyksiköllä kyettäisiin valmistamaan Ekopoltetta energiatiheämpää polttoainetta vain marginaalisesti heikommalla raaka-aineen hyötysuhteella. Teknologian mahdollistaman tuotelanseerauksen, EkopoltePlus -lentopetrolin, myös arvioitaisiin herättävän alan isompien toimijoiden kiinnostusta. 

Tuotannon aloittaminen vaatisi 330000 € investoinnin tuotantolaitteistoihin. Markkinatutkimuksen perusteella Biohajotus Oy:n johto odottaa EkopoltePlussan myyntimäärän olevan 120000 litraa ensimmäisenä vuotena, ja kysynnän vuosittainen kasvu saavuttaisi seuraavina tilikausina jopa 5.7 %. EkopoltePlussan suuremman energiatiheyden johdosta myös keskimääräisen myyntihinnan arvioidaan olevan huomattavasti alkuperäistä Ekopoltetta korkeammalla, noin 3.73 €/litra. Tuotantoprosessin suuremman vety- ja fosforikulutuksen johdosta kuitenkin ravinneannosten kokoa on kasvatettava siten, että myös tuotteen raaka-ainekustannukset nousisivat tasolle 1.25 €/tuotettu litra. Yksinomaan EkopoltePlus-tuotantoon liittyvien muiden kustannusten odotetaan olevan noin 170000 €/vuosi. 

Pääoman keskimääräinen tuottovaatimus on Biohajotus Oy:lle investointipäätöksen tekohetkellä 9.5 %. Käyttöpääoman sitoutumista ei tarvitse ottaa huomioon. Tuotantolaitteiston eliniäksi arvioidaan noin viisi vuotta, ja se poistetaan tänä aikana tasapoistoin, jonka jälkeen voidaan olettaa, että tuotantolaitteisto on käyttökelvoton ja arvoton. Hinnoissa ei tarvitse huomioida arvonlisäveroa, yhteisövero on 20 %. 

Tehtävissä arvioidaan investoinnin kannattavuutta viiden vuoden ajanjaksolla, jossa investointi tehdään vuonna 0 ja tuotanto on käynnissä vuosina 1-5.

'''

def sum_term(WACC, FCF_t, t):
	return FCF_t / (1 + WACC)**t

def toinen_sivu():
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

	# ====================================================================================================
	# ====================================================================================================
	# ====================================================================================================

	# Let's first establish some basic numbers first...

	investoinnit = 0 # we do not do investments during PRODUCTION YEARS!!!

	liikevaihto = myyntimäärä_litraa * myyntihinta_per_litra
	myytyjen_tuotteiden_materiaalikustannus = myyntimäärä_litraa * raaka_ainekustannukset
	käyttökate = liikevaihto - myytyjen_tuotteiden_materiaalikustannus - muut_kustannukset

	vuotuiset_poistot = tuotannon_aloittamisen_kustannus / tuotantolaitteiston_elinikä # Poistot joka vuodelta. Tämä on tuotantolaitteiston kustannus jaettuna vuosien määrä

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

	FCF_t = (liikevoitto) * (1 - yhteisövero) + vuotuiset_poistot #  + käyttöpääoma_kauden_alussa - käyttöpääoma_kauden_lopussa + investointien_rahavirta # We can safely ignore these.

	NPV = sum(sum_term(WACC, FCF_t, t) for t in range(1,6)) + sum_term(WACC, FCF_0, 0) # 1 2 3 4 and 5
	print("NPV (Nettonykyarvo): "+str(NPV))



	return


if __name__=="__main__":
	# calcs()
	toinen_sivu()
	exit(0)

