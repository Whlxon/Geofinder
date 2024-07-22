import pygame as pg 

pg.init()

#on import le point de la souris
s_point = pg.image.load('other/point.png')
s_p_rect = s_point.get_rect()

#on import la carte de l'amerique du nord
amerique_n = pg.image.load('maps/Amerique_n.png')

#on importe l'image de validation lorsqu'onn place bien un pays
validation = pg.image.load('flags/validé.png')

#on import la carte de l'asie
asie_c = pg.image.load('maps/Asia.png')
a_x, a_y = 0, 0

#on import la carte du continent européen
europe = pg.image.load('maps/europe.png')
e_x, e_y = 0, 0

#on import les drapeaux des pays de l'europe
belgique = pg.image.load('flags/flags_europe/Belgium.png')
belgium_rect = belgique.get_rect()
belgium_rect.x, belgium_rect.y = 1000, 0

france = pg.image.load('flags/flags_europe/France.png')
france_rect = france.get_rect()
france_rect.x, france_rect.y = 1000, 42

swisse = pg.image.load('flags/flags_europe/Swiss.png')
swisse_rect = swisse.get_rect()
swisse_rect.x, swisse_rect.y = 1000, 84

finland = pg.image.load('flags/flags_europe/Finland.png')
finland_rect = finland.get_rect()
finland_rect.x, finland_rect.y = 1000, 126

Danemark = pg.image.load('flags/flags_europe/Danemark.png')
Danemark_rect = Danemark.get_rect()
Danemark_rect.x, Danemark_rect.y = 1000, 168

Norvège = pg.image.load('flags/flags_europe/Norvège.png')
Norvège_rect = Norvège.get_rect()
Norvège_rect.x, Norvège_rect.y = 1000, 210

Pays_bas = pg.image.load('flags/flags_europe/Pays-Bas.png')
Pays_bas_rect = Pays_bas.get_rect()
Pays_bas_rect.x, Pays_bas_rect.y = 1000, 252

Islande = pg.image.load('flags/flags_europe/Islande.png')
Islande_rect = Islande.get_rect()
Islande_rect.x, Islande_rect.y = 1000, 294

Italie = pg.image.load('flags/flags_europe/Italie.png')
Italie_rect = Italie.get_rect()
Italie_rect.x, Italie_rect.y = 1000, 336

Bulgarie = pg.image.load('flags/flags_europe/Bulgarie.png')
Bulgarie_rect = Bulgarie.get_rect()
Bulgarie_rect.x, Bulgarie_rect.y = 1000, 378

Sweden = pg.image.load('flags/flags_europe/Sweden.png')
Sweden_rect = Sweden.get_rect()
Sweden_rect.x, Sweden_rect.y = 1000, 420

Royaume_Unis = pg.image.load('flags/flags_europe/Royaume-Unis.png')
Royaume_U_rect = Royaume_Unis.get_rect()
Royaume_U_rect.x, Royaume_U_rect.y = 1000, 462

Grèce = pg.image.load('flags/flags_europe/Grèce.png')
grèce_rect = Grèce.get_rect()
grèce_rect.x, grèce_rect.y = 1000, 504

Bielorussie = pg.image.load('flags/flags_europe/Biélorussie.png')
bielorussie_rect = Bielorussie.get_rect()
bielorussie_rect.x, bielorussie_rect.y = 1000, 546

Pologne = pg.image.load('flags/flags_europe/Pologne.png')
pologne_rect = Pologne.get_rect()
pologne_rect.x, pologne_rect.y = 1000, 588

Roumanie = pg.image.load('flags/flags_europe/Roumanie.png')
roumanie_rect = Roumanie.get_rect()
roumanie_rect.x, roumanie_rect.y = 1000, 630

Ukraine = pg.image.load('flags/flags_europe/Ukraine.png')
ukraine_rect = Ukraine.get_rect()
ukraine_rect.x, ukraine_rect.y = 1000, 672

Allemagne = pg.image.load('flags/flags_europe/Allemagne.png')
allemagne_rect = Allemagne.get_rect()
allemagne_rect.x, allemagne_rect.y = 1000, 704

Espagne = pg.image.load('flags/flags_europe/Espagne.png')
espagne_rect = Espagne.get_rect()
espagne_rect.x, espagne_rect.y = 1000, 746

andore = pg.image.load('flags/flags_europe/andore.png')
andore_rect = andore.get_rect()
andore_rect.x, andore_rect.y = 1000, 788

albanie = pg.image.load('flags/flags_europe/albanie.png')
albanie_rect = albanie.get_rect()
albanie_rect.x, albanie_rect.y = 1000, 830

estonie = pg.image.load('flags/flags_europe/estonie.png')
estonie_rect = estonie.get_rect()
estonie_rect.x, estonie_rect.y = 1000, 872

lituanie = pg.image.load('flags/flags_europe/lituanie.png')
lituanie_rect = lituanie.get_rect()
lituanie_rect.x, lituanie_rect.y = 1000, 914

letonie = pg.image.load('flags/flags_europe/letonie.png')
letonie_rect = letonie.get_rect()
letonie_rect.x, letonie_rect.y = 1042, 0

montenegro = pg.image.load('flags/flags_europe/montenegro.png')
mtnegro_rect = montenegro.get_rect()
mtnegro_rect.x, mtnegro_rect.y = 1042, 42

vatican = pg.image.load('flags/flags_europe/vatican.png')
vatican_rect = vatican.get_rect()
vatican_rect.x, vatican_rect.y = 1042, 84

portugal = pg.image.load('flags/flags_europe/portugal.png')
portugal_rect = portugal.get_rect()
portugal_rect.x, portugal_rect.y = 1042, 126

Irlande = pg.image.load('flags/flags_europe/irlande.png')
irlande_rect = Irlande.get_rect()
irlande_rect.x, irlande_rect.y = 1042, 168

Luxembourg = pg.image.load('flags/flags_europe/luxembourg.png')
luxembourg_rect = Luxembourg.get_rect()
luxembourg_rect.x, luxembourg_rect.y = 1042, 210

Macedoine_n = pg.image.load('flags/flags_europe/macedoine du nord.png')
macedoine_rect = Macedoine_n.get_rect()
macedoine_rect.x, macedoine_rect.y = 1042, 252

slovaquie = pg.image.load('flags/flags_europe/slovaquie.png') 
slovaquie_rect = slovaquie.get_rect()
slovaquie_rect.x, slovaquie_rect.y = 1042, 294

bosnie = pg.image.load('flags/flags_europe/bosnie.png')
bosnie_rect = bosnie.get_rect()
bosnie_rect.x, bosnie_rect.y = 1042, 336

hongrie = pg.image.load('flags/flags_europe/hongrie.png')
hongrie_rect = hongrie.get_rect()
hongrie_rect.x, hongrie_rect.y = 1042, 378

autriche  = pg.image.load('flags/flags_europe/autriche.png')
autriche_rect = autriche.get_rect()
autriche_rect.x, autriche_rect.y = 1042, 420

r_tcheque = pg.image.load('flags/flags_europe/Rép tchèque.png')
r_tcheque_rect = r_tcheque.get_rect()
r_tcheque_rect.x, r_tcheque_rect.y = 1042, 462

croatie  = pg.image.load('flags/flags_europe/croatie.png')
croatie_rect = croatie.get_rect()
croatie_rect.x, croatie_rect.y = 1042, 504

moldavie  = pg.image.load('flags/flags_europe/moldavie.png')
moldavie_rect = moldavie.get_rect()
moldavie_rect.x, moldavie_rect.y = 1042, 546

kaliningrad  = pg.image.load('flags/flags_europe/kaliningrad.png')
kaliningrad_rect = kaliningrad.get_rect()
kaliningrad_rect.x, kaliningrad_rect.y = 1042, 588

crimé = pg.image.load('flags/flags_europe/crimé.png')
crimé_rect = crimé.get_rect()
crimé_rect.x, crimé_rect.y = 1042, 630

slovenie = pg.image.load('flags/flags_europe/slovenie.png')
slovenie_rect = slovenie.get_rect()
slovenie_rect.x, slovenie_rect.y = 1042, 672

serbie = pg.image.load('flags/flags_europe/serbie.png')
serbie_rect = serbie.get_rect()
serbie_rect.x, serbie_rect.y = 1042, 714

kosovo = pg.image.load('flags/flags_europe/kosovo.png')
kosovo_rect = kosovo.get_rect()
kosovo_rect.x, kosovo_rect.y = 1042, 756

turkie = pg.image.load('flags/flags_europe/turkie.png')
turkie_rect = turkie.get_rect()
turkie_rect.x, turkie_rect.y = 1042, 798

pays =      [belgique,       france,       swisse,      finland,   Danemark,         Norvège,      Pays_bas,     Islande,       Italie,     Bulgarie,      Sweden,     Royaume_Unis,     Grèce,     Bielorussie,      Pologne,      Roumanie,      Ukraine,       Allemagne,      Espagne,      andore,     albanie,      estonie,       lituanie,      letonie,    montenegro,    vatican,      portugal,      Irlande,       Luxembourg,     Macedoine_n,      slovaquie,      bosnie,     hongrie,      autriche,      r_tcheque,      croatie,      moldavie,      kaliningrad,      crimé,       slovenie,     serbie,       kosovo,     turkie   ]
pays_rect = [belgium_rect, france_rect, swisse_rect, finland_rect, Danemark_rect, Norvège_rect, Pays_bas_rect, Islande_rect, Italie_rect, Bulgarie_rect, Sweden_rect, Royaume_U_rect, grèce_rect, bielorussie_rect, pologne_rect, roumanie_rect, ukraine_rect, allemagne_rect, espagne_rect, andore_rect, albanie_rect, estonie_rect, lituanie_rect, letonie_rect, mtnegro_rect, vatican_rect, portugal_rect, irlande_rect, luxembourg_rect, macedoine_rect,  slovaquie_rect, bosnie_rect, hongrie_rect, autriche_rect, r_tcheque_rect, croatie_rect, moldavie_rect, kaliningrad_rect, crimé_rect, slovenie_rect, serbie_rect, kosovo_rect, turkie_rect]
pays_d_x =  [(318, 358),    (207, 343),  (374, 415),    (629, 702), (423, 456),    (405, 477),    (354, 381),    (140, 194),  (442, 513),   (714, 788),   (494, 552),   (208, 278),    (672, 719),  (714, 802),      (530, 684),   (684, 788),    (773, 915),    (395, 484),    (72, 183),    (238, 255),  (640, 669),   (669, 712),    (660, 703),    (671, 728),  (619, 640),   (459, 485),    (22, 52),     (129, 174),     (356, 371),      (671, 707),     (592, 633),    (569, 627),  (601, 661),    (503, 560),    (501, 555),    (552, 582),    (777, 819),    (613, 656),     (898, 932),   (509, 543),  (631, 690),   (656, 682),  (901, 986)]
pays_d_y =  [(504, 530),    (565, 728),  (620, 651),    (159, 227), (353, 397),    (212, 270),    (450, 487),    (101, 133),  (736, 793),   (716, 758),   (176, 239),   (430, 486),    (826, 862),  (385, 463),      (433, 531),   (608, 686),    (490, 571),    (483, 552),    (770, 864),   (746, 759),  (791, 829),   (266, 310),    (354, 404),    (309, 352),  (742, 766),   (765, 786),   (777, 809),    (397, 431),     (540, 556),      (772, 795),     (567, 591),    (690, 735),  (609, 647),    (595, 634),    (526, 572),    (661, 683),    (569, 611),    (391, 406),     (611, 630),   (652, 680),  (698, 734),   (748, 767),  (768, 823)]
pays_l =    []

for i in range(len(pays)):
    pays_l.append(False)

#on importe tout les drapeaux d'asie
afghanistan = pg.image.load('flags/flags_asia/Afghanistan.png')
afghanistan_rect = afghanistan.get_rect()
afghanistan_rect.x, afghanistan_rect.y = 0, 666

abhazie = pg.image.load('flags/flags_asia/Abhazie.png')
abhazie_rect = abhazie.get_rect()
abhazie_rect.x, abhazie_rect.y = 42, 666

arabie_saoudite = pg.image.load('flags/flags_asia/Arabie_saoudite.jfif')
arabie_rect = arabie_saoudite.get_rect()
arabie_rect.x, arabie_rect.y =  84, 666

armenie = pg.image.load('flags/flags_asia/Armenie.png')
armenie_rect = armenie.get_rect()
armenie_rect.x, armenie_rect.y = 126, 666

artsakh  = pg.image.load('flags/flags_asia/Artsakh.png')
artsakh_rect = artsakh.get_rect()
artsakh_rect.x, artsakh_rect.y = 168, 666

azerbaijan = pg.image.load('flags/flags_asia/Azerbaijan.png')
azerbaijan_rect = azerbaijan.get_rect()
azerbaijan_rect.x, azerbaijan_rect.y = 210, 666

bahrein = pg.image.load('flags/flags_asia/bahrein.png')
bahrein_rect = bahrein.get_rect()
bahrein_rect.x, bahrein_rect.y = 252, 666

bangladesh = pg.image.load('flags/flags_asia/bangladesh.png')
bangladesh_rect = bangladesh.get_rect()
bangladesh_rect.x, bangladesh_rect.y = 294, 666

biramnie = pg.image.load('flags/flags_asia/Birmanie.png')
biramnie_rect = biramnie.get_rect()
biramnie_rect.x, biramnie_rect.y = 336, 666

burnei = pg.image.load('flags/flags_asia/Burnei.png')
burnei_rect = burnei.get_rect()
burnei_rect.x, burnei_rect.y = 378, 666

buthan  = pg.image.load('flags/flags_asia/Buthan.png')
buthan_rect = buthan.get_rect()
buthan_rect.x, buthan_rect.y = 420, 666

cambodge = pg.image.load('flags/flags_asia/Cambodge.png')
cambodge_rect = cambodge.get_rect()
cambodge_rect.x, cambodge_rect.y = 958, 666

chine  = pg.image.load('flags/flags_asia/Chine.png')
chine_rect = chine.get_rect()
chine_rect.x, chine_rect.y = 958, 624

corée_n  = pg.image.load('flags/flags_asia/Corée du nord.png')
corée_n_rect = corée_n.get_rect()
corée_n_rect.x, corée_n_rect.y = 958, 582

corée_s  = pg.image.load('flags/flags_asia/Corée du sud.png')
corée_s_rect = corée_s.get_rect()
corée_s_rect.x, corée_s_rect.y = 958, 540

georgie = pg.image.load('flags/flags_asia/Georgie.png')
georgie_rect = georgie.get_rect()
georgie_rect.x, georgie_rect.y = 958, 498

hong_kong  = pg.image.load('flags/flags_asia/Hong Kong.png')
hong_kong_rect = hong_kong.get_rect()
hong_kong_rect.x, hong_kong_rect.y = 958, 456

inde = pg.image.load('flags/flags_asia/Inde.png')
inde_rect = inde.get_rect()
inde_rect.x, inde_rect.y = 958, 414

indonesie = pg.image.load('flags/flags_asia/Indonesie.png')
indonesie_rect = indonesie.get_rect()
indonesie_rect.x, indonesie_rect.y = 958, 372

iran = pg.image.load('flags/flags_asia/Iran.png')
iran_rect = iran.get_rect()
iran_rect.x, iran_rect.y = 958, 330

iraq = pg.image.load('flags/flags_asia/Iraq.png')
iraq_rect = iraq.get_rect()
iraq_rect.x, iraq_rect.y = 958, 288

israel = pg.image.load('flags/flags_asia/Israel.png')
israel_rect = israel.get_rect()
israel_rect.x, israel_rect.y = 958, 246

japon = pg.image.load('flags/flags_asia/Japon.png')
japon_rect = japon.get_rect()
japon_rect.x, japon_rect.y = 958, 204

jordanie = pg.image.load('flags/flags_asia/Jordanie.png')
jordanie_rect =jordanie.get_rect()
jordanie_rect.x, jordanie_rect.y = 958, 162

kazakhstan = pg.image.load('flags/flags_asia/Kazakhstan.png')
kazakhstan_rect = kazakhstan.get_rect()
kazakhstan_rect.x, kazakhstan_rect.y = 916, 666

koweit = pg.image.load('flags/flags_asia/Koweit.png')
koweit_rect = koweit.get_rect()
koweit_rect.x, koweit_rect.y = 916, 624

laos = pg.image.load('flags/flags_asia/Laos.png')
laos_rect = laos.get_rect()
laos_rect.x, laos_rect.y = 916, 540

liban = pg.image.load('flags/flags_asia/Liban.png')
liban_rect = liban.get_rect()
liban_rect.x, liban_rect.y = 916, 498

malaisie = pg.image.load('flags/flags_asia/Malaisie.png')
malaisie_rect = malaisie.get_rect()
malaisie_rect.x, malaisie_rect.y = 916, 414

maldive = pg.image.load('flags/flags_asia/Maldive.png')
maldive_rect = maldive.get_rect()
maldive_rect.x, maldive_rect.y = 916, 372

mongolie = pg.image.load('flags/flags_asia/Mongolie.png')
mongolie_rect = mongolie.get_rect()
mongolie_rect.x, mongolie_rect.y = 916, 330

nepal = pg.image.load('flags/flags_asia/Nepal.png')
nepal_rect = nepal.get_rect()
nepal_rect.x, nepal_rect.y = 916, 246

ouzbekistan = pg.image.load('flags/flags_asia/Ouzbekistan.png')
ouzbekistan_rect = ouzbekistan.get_rect()
ouzbekistan_rect.x, ouzbekistan_rect.y = 916, 204

pakistan = pg.image.load('flags/flags_asia/Pakistan.png')
pakistan_rect = pakistan.get_rect()
pakistan_rect.x, pakistan_rect.y = 916, 162

palestine = pg.image.load('flags/flags_asia/Palestine.png')
palestine_rect = palestine.get_rect()
palestine_rect.x, palestine_rect.y = 0, 624

philippines = pg.image.load('flags/flags_asia/philippines.png')
philippines_rect = philippines.get_rect()
philippines_rect.x, philippines_rect.y = 42, 624

qatar = pg.image.load('flags/flags_asia/Qatar.png')
qatar_rect = qatar.get_rect()
qatar_rect.x, qatar_rect.y = 84, 624

russie = pg.image.load('flags/flags_asia/russie.png')
russie_rect = russie.get_rect()
russie_rect.x, russie_rect.y = 126, 624

singapour = pg.image.load('flags/flags_asia/Singapour.png')
singapour_rect = singapour.get_rect()
singapour_rect.x, singapour_rect.y = 168, 624

sri_lanka = pg.image.load('flags/flags_asia/Sri Lanka.png')
sri_lanka_rect = sri_lanka.get_rect()
sri_lanka_rect.x, sri_lanka_rect.y = 210, 624

syrie = pg.image.load('flags/flags_asia/Syrie.png')
syrie_rect = syrie.get_rect()
syrie_rect.x, syrie_rect.y = 252, 624

taiwan = pg.image.load('flags/flags_asia/taiwan.png')
taiwan_rect = taiwan.get_rect()
taiwan_rect.x, taiwan_rect.y = 294, 624

thailand = pg.image.load('flags/flags_asia/thailand.png')
thailand_rect = thailand.get_rect()
thailand_rect.x, thailand_rect.y = 336, 624

timor = pg.image.load('flags/flags_asia/Timor.png')
timor_rect = timor.get_rect()
timor_rect.x, timor_rect.y = 378, 624

turkmenistan = pg.image.load('flags/flags_asia/Turkmenistan.png')
turkmenistan_rect = turkmenistan.get_rect()
turkmenistan_rect.x, turkmenistan_rect.y = 0, 582

vietnam = pg.image.load('flags/flags_asia/Vietnam.png')
vietnam_rect = vietnam.get_rect()
vietnam_rect.x, vietnam_rect.y = 42, 582

yemen = pg.image.load('flags/flags_asia/Yemen.png')
yemen_rect = yemen.get_rect()
yemen_rect.x, yemen_rect.y = 84, 582

asie =      [   afghanistan,     abhazie,  arabie_saoudite, armenie,      azerbaijan,      bahrein,      bangladesh,       biramnie,      burnei,      buthan,     cambodge,      chine,      corée_n,       corée_s,      georgie,     hong_kong,      inde,      indonesie,       iran,      iraq,      israel,     japon,      jordanie,      kazakhstan,      koweit,      laos,      liban,      malaisie,      maldive,      mongolie,       nepal,     ouzbekistan,       pakistan,     palestine,       philippines,      qatar,     russie,      singapour,      sri_lanka,      syrie,      taiwan,      thailand,       timor,      turkmenistan,     vietnam,      yemen]
asie_rect = [afghanistan_rect, abhazie_rect, arabie_rect, armenie_rect, azerbaijan_rect, bahrein_rect, bangladesh_rect, biramnie_rect, burnei_rect, buthan_rect, cambodge_rect, chine_rect, corée_n_rect, corée_s_rect, georgie_rect, hong_kong_rect, inde_rect, indonesie_rect, iran_rect, iraq_rect, israel_rect, japon_rect, jordanie_rect, kazakhstan_rect, koweit_rect, laos_rect, liban_rect, malaisie_rect, maldive_rect, mongolie_rect, nepal_rect, ouzbekistan_rect, pakistan_rect, palestine_rect, philippines_rect, qatar_rect, russie_rect, singapour_rect, sri_lanka_rect, syrie_rect, taiwan_rect, thailand_rect, timor_rect, turkmenistan_rect, vietnam_rect, yemen_rect]
asie_d_x =  [    (257, 272),    (115, 123),   (102, 121),  (130, 141),    (147, 161),     (169, 174),    (423, 435),     (461, 474),    (582, 589),  (421, 434),   (514, 528),   (494, 516),  (669, 681),  (665, 678),    (125, 133),   (579, 587),   (339, 353),   (499, 599),  (204, 214), (132, 143), (69, 75),   (745, 756), (87, 100),       (279, 289),    (151, 157),  (502, 514), (72, 79),    (585, 595),   (329, 337),   (529, 541),   (369, 380),    (261, 272),      (298, 310),    (69, 76),        (624, 636),    (175, 182),  (473, 488),  (511, 522),     (363, 375),    (98, 112),   (619, 631),   (495, 506),  (663, 674),     (238, 249),     (540, 551),  (164, 176)]
asie_d_y =  [    (383, 397),    (309, 315),   (411, 428),  (327, 336),    (326, 339),     (429, 434),    (444, 457),     (452, 464),    (574, 578),  (420, 431),   (520, 534),   (364, 383),  (318, 330),  (344, 357),    (313, 324),   (457, 465),   (426, 438),   (612, 664),  (401, 411), (394, 404), (390, 396), (344, 354), (386, 395),     (243, 256),    (408, 415),  (468, 482), (376, 382),  (579, 589),   (606, 612),   (281, 292),   (409, 418),    (323, 334),      (397, 410),    (390, 396),      (490, 502),    (439, 445),  (119, 133),  (595, 605),     (554, 566),    (358, 368),  (448, 459),   (511, 521),  (655, 663),     (342, 352),     (510, 520),  (494, 503)]
asie_l =    []

for i in range(len(asie)):
    asie_l.append(False)


#on import tout les drapeaux de l'amerique du nord
canada = pg.image.load('flags/flags_amerique_n/canada.png')
canada_rect = canada.get_rect()
canada_rect.x, canada_rect.y = 0, 770

état_Unis = pg.image.load(('flags/flags_amerique_n/État-Unis.png'))
état_Unis_rect = état_Unis.get_rect()
état_Unis_rect.x, état_Unis_rect.y = 0, 730

haiti = pg.image.load('flags/flags_amerique_n/haiti.png')
haiti_rect = haiti.get_rect()
haiti_rect.x, haiti_rect.y = 0, 690

panama = pg.image.load('flags/flags_amerique_n/Panama.png')
panama_rect = panama.get_rect()
panama_rect.x, panama_rect.y = 0, 650

mexique = pg.image.load('flags/flags_amerique_n/Mexique.png')
mexique_rect = mexique.get_rect()
mexique_rect.x, mexique_rect.y = 0, 610

groenland = pg.image.load('flags/flags_amerique_n/groenland.png')
groenland_rect = groenland.get_rect()
groenland_rect.x, groenland_rect.y = 0, 570

honduras = pg.image.load('flags/flags_amerique_n/Honduras.png')
honduras_rect = honduras.get_rect()
honduras_rect.x, honduras_rect.y = 0, 530

gautemala = pg.image.load('flags/flags_amerique_n/Gautemala.png')
gautemala_rect = gautemala.get_rect()
gautemala_rect.x, gautemala_rect.y = 0, 490

el_salvador = pg.image.load('flags/flags_amerique_n/El salvador.png')
el_salvador_rect = el_salvador.get_rect()
el_salvador_rect.x, el_salvador_rect.y = 0, 450

cuba = pg.image.load('flags/flags_amerique_n/cuba.png')
cuba_rect = cuba.get_rect()
cuba_rect.x, cuba_rect.y = 0, 410

belize = pg.image.load('flags/flags_amerique_n/Belize.png')
belize_rect = belize.get_rect()
belize_rect.x, belize_rect.y = 0, 370

costa_rica = pg.image.load('flags/flags_amerique_n/Costa Rica.png')
costa_rica_rect = costa_rica.get_rect()
costa_rica_rect.x, costa_rica_rect.y = 0, 330

jamaique = pg.image.load('flags/flags_amerique_n/Jamaique.png')
jamaique_rect = jamaique.get_rect()
jamaique_rect.x, jamaique_rect.y = 0, 290

r_dominicaine = pg.image.load('flags/flags_amerique_n/Rép dominicaine.png')
r_domi_rect = r_dominicaine.get_rect()
r_domi_rect.x, r_domi_rect.y = 0, 250

trinité_tobago = pg.image.load('flags/flags_amerique_n/Trinité et tobago.png')
trinité_rect = trinité_tobago.get_rect()
trinité_rect.x, trinité_rect.y = 0, 210

nicaragua = pg.image.load('flags/flags_amerique_n/nicaragua.png')
nicaragua_rect = nicaragua.get_rect()
nicaragua_rect.x, nicaragua_rect.y = 0, 170

amerique =      [   canada,     état_Unis,      haiti,       panama,     mexique,      groenland,      honduras,      gautemala,      el_salvador,      cuba,      belize,      costa_rica,      jamaique,   r_dominicaine, trinité_tobago,  nicaragua]
amerique_rect = [canada_rect, état_Unis_rect, haiti_rect, panama_rect, mexique_rect, groenland_rect, honduras_rect, gautemala_rect, el_salvador_rect, cuba_rect, belize_rect, costa_rica_rect, jamaique_rect, r_domi_rect,   trinité_rect, nicaragua_rect]
amerique_d_x =  [ (314, 330),   (352, 368),   (652, 663),  (576, 586),  (352, 367),    (569, 583),    (512, 522),     (465, 473),     (484, 493),     (603, 612), (487, 494),   (539, 550),     (607, 614),    (672, 680),   (690, 697),     (529, 536)]
amerique_d_y =  [ (223, 238),   (458, 470),   (636, 647),  (788, 796),  (651, 664),    (31, 43),      (730, 737),     (728, 737),     (741, 751),     (633, 640), (701, 711),   (773, 784),     (667, 674),    (633, 640),   (712, 722),     (747, 757)]
amerique_l =    []

for i in range(len(amerique)):
    amerique_l.append(False)

print(f"RAPPORT:\n -Variable amerique:{len(amerique)}\n -Variable amerique_rect: {len(amerique_rect)}\n -Variable, amerique_d_x: {len(amerique_d_x)}\n -Variable amerique_d_y: {len(amerique_d_y)}\n -Variable amerique_l: {len(amerique_l)}")
