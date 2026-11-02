# Contenido de la demo Hotel Oriente (Teruel) (es/en/fr/de). Hechos de hotelorientedeteruel.com leidos el 02/11/2026 (ver berawa/sources.json). Sin precios ni valoraciones.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran el alojamiento real.','en':' Images are illustrations and do not show the actual property.','fr':' Les images sont des illustrations et ne montrent pas l’établissement réel.','de':' Die Bilder sind Illustrationen und zeigen nicht die tatsächliche Unterkunft.'}
H={'es':['Habitación doble','Habitación triple e individual'],'en':['Double room','Triple and single rooms'],'fr':['Chambre double','Chambres triple et individuelle'],'de':['Doppelzimmer','Dreibett- und Einzelzimmer']}
RD={
'es':['Con dos camas individuales o una cama de matrimonio, televisión de pantalla plana, baño completo con secador de pelo, teléfono y wifi.','Las triples, con tres camas individuales o una doble y una individual; las individuales, con TV de pantalla plana, baño completo y secador.'],
'en':['With two single beds or a double bed, flat-screen TV, full bathroom with hairdryer, telephone and wifi.','Triples have three single beds or a double and a single; singles have a flat-screen TV, full bathroom and hairdryer.'],
'fr':['Avec deux lits simples ou un lit double, TV à écran plat, salle de bains complète avec sèche-cheveux, téléphone et wifi.','Les triples ont trois lits simples ou un double et un simple ; les individuelles, TV à écran plat, salle de bains complète et sèche-cheveux.'],
'de':['Mit zwei Einzelbetten oder einem Doppelbett, Flachbild-TV, Bad mit Föhn, Telefon und WLAN.','Dreibettzimmer mit drei Einzelbetten oder einem Doppel- und einem Einzelbett; Einzelzimmer mit Flachbild-TV, Bad und Föhn.']}
ART={
'hero':('skyline',8811,['#2b1f24','#b07a5a','#f0e0d4','#6a5560','#46363d','#1d1519']),
'intro':('arches',8812,['#f3edea','#fbf8f6','#7c3f45','#5f5258','#2b1f24']),
'r1':('columns',8821,['#efe7e3','#d79e8c','#7c3f45','#5f5258','#2b1f24']),
'r2':('arches',8822,['#2b1f24','#bb8463','#f3e5da','#75606a','#4d3c43','#1f171b']),
'g1':('waves',8831,['#2b1f24','#b07a5a','#f0e0d4','#6a5560','#46363d','#1d1519']),
'g2':('hills',8832,['#ebe5e1','#ecd5c7','#d79e8c','#928789','#6a6062','#463e40']),
'g3':('columns',8833,['#f3edea','#fbf8f6','#7c3f45','#5f5258','#2b1f24']),
'g4':('skyline',8834,['#2b1f24','#bb8463','#f3e5da','#75606a','#4d3c43','#1f171b'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Oriente · Hotel de tres estrellas en el centro de Teruel',see_rooms='Ver habitaciones',hero_k='Teruel · Av. Sagunto, 7',hero_t='Tu hotel en el centro de Teruel',hero_s='Un hotel de tres estrellas con alma y encanto, con atención personalizada a cada cliente.',
 intro_t='Como en casa',intro_p1='El Hotel Oriente está en pleno centro de Teruel. Su equipo, amable y cualificado, te ayuda con cualquier duda y te da toda la información turística que necesites.',
 intro_p2='Cada mañana, el restaurante propone un desayuno bufet. Hay sala fitness equipada, salón de lectura y bar-cafetería; la recepción abre de 7 a 23 h.',
 stats=['3 estrellas','Centro de Teruel','Desayuno bufet','Parking'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Individuales, dobles, triples y familiares, todas con aire acondicionado o calefacción y un obsequio infantil de bienvenida.',
 svcs=['Desayuno bufet en el restaurante','Gimnasio equipado y salón de lectura','Parking, con limpieza gratuita del parabrisas','Aparcamiento gratuito de bicicletas en garaje','Cunas y camas supletorias bajo petición','Late check-out según disponibilidad'],
 loc_p='Av. Sagunto, 7 · 44002 Teruel. Teléfono: 978 60 15 50. Correo: recepcion@hotelorientedeteruel.com.',
 chips=['¿Qué habitaciones tenéis?','¿Hay desayuno?','¿Tenéis parking?','¿Cómo reservo?']),
'en':dict(title='Hotel Oriente · Three-star hotel in central Teruel',see_rooms='See rooms',hero_k='Teruel · Av. Sagunto, 7',hero_t='Your hotel in central Teruel',hero_s='A three-star hotel with soul and charm, with personal attention for every guest.',
 intro_t='Feel at home',intro_p1='Hotel Oriente is right in the centre of Teruel. Its friendly, qualified team helps with any question and gives you all the tourist information you need.',
 intro_p2='Every morning the restaurant serves a buffet breakfast. There is a fully equipped fitness room, a reading lounge and a bar-café; reception is open from 7 to 23 h.',
 stats=['3 stars','Central Teruel','Buffet breakfast','Parking'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='Single, double, triple and family rooms, all with air conditioning or heating and a welcome gift for children.',
 svcs=['Buffet breakfast in the restaurant','Equipped gym and reading lounge','Parking, with free windscreen cleaning','Free bicycle parking in the garage','Cots and extra beds on request','Late check-out subject to availability'],
 loc_p='Av. Sagunto, 7 · 44002 Teruel. Phone: +34 978 60 15 50. Email: recepcion@hotelorientedeteruel.com.',
 chips=['Which rooms do you have?','Is there breakfast?','Do you have parking?','How do I book?']),
'fr':dict(title='Hotel Oriente · Hôtel trois étoiles au centre de Teruel',see_rooms='Voir les chambres',hero_k='Teruel · Av. Sagunto, 7',hero_t='Votre hôtel au centre de Teruel',hero_s='Un hôtel trois étoiles plein d’âme et de charme, avec une attention personnalisée pour chaque client.',
 intro_t='Comme à la maison',intro_p1='L’Hotel Oriente est en plein centre de Teruel. Son équipe aimable et qualifiée répond à toutes vos questions et vous donne toutes les informations touristiques utiles.',
 intro_p2='Chaque matin, le restaurant propose un petit-déjeuner buffet. Salle de fitness équipée, salon de lecture et bar-cafétéria ; réception ouverte de 7 h à 23 h.',
 stats=['3 étoiles','Centre de Teruel','Petit-déjeuner buffet','Parking'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Individuelles, doubles, triples et familiales, toutes avec climatisation ou chauffage et un cadeau de bienvenue pour les enfants.',
 svcs=['Petit-déjeuner buffet au restaurant','Salle de sport équipée et salon de lecture','Parking, avec nettoyage gratuit du pare-brise','Stationnement gratuit des vélos au garage','Lits bébé et lits d’appoint sur demande','Départ tardif selon disponibilité'],
 loc_p='Av. Sagunto, 7 · 44002 Teruel. Téléphone : +34 978 60 15 50. E-mail : recepcion@hotelorientedeteruel.com.',
 chips=['Quelles chambres avez-vous ?','Y a-t-il un petit-déjeuner ?','Avez-vous un parking ?','Comment réserver ?']),
'de':dict(title='Hotel Oriente · Drei-Sterne-Hotel im Zentrum von Teruel',see_rooms='Zimmer ansehen',hero_k='Teruel · Av. Sagunto, 7',hero_t='Ihr Hotel im Zentrum von Teruel',hero_s='Ein Drei-Sterne-Hotel mit Seele und Charme und persönlicher Betreuung jedes Gastes.',
 intro_t='Wie zu Hause',intro_p1='Das Hotel Oriente liegt mitten im Zentrum von Teruel. Das freundliche, qualifizierte Team hilft bei allen Fragen und gibt alle touristischen Informationen.',
 intro_p2='Jeden Morgen gibt es im Restaurant ein Frühstücksbuffet. Dazu ein ausgestatteter Fitnessraum, ein Leseraum und eine Bar-Cafeteria; die Rezeption ist von 7 bis 23 Uhr geöffnet.',
 stats=['3 Sterne','Zentrum von Teruel','Frühstücksbuffet','Parkplatz'],nav_rooms='Zimmer',rooms_t='Zimmer',rooms_s='Einzel-, Doppel-, Dreibett- und Familienzimmer, alle mit Klimaanlage oder Heizung und einem Willkommensgeschenk für Kinder.',
 svcs=['Frühstücksbuffet im Restaurant','Fitnessraum und Leseraum','Parkplatz mit kostenloser Scheibenreinigung','Kostenlose Fahrradstellplätze in der Garage','Kinderbetten und Zustellbetten auf Anfrage','Später Check-out je nach Verfügbarkeit'],
 loc_p='Av. Sagunto, 7 · 44002 Teruel. Telefon: +34 978 60 15 50. E-Mail: recepcion@hotelorientedeteruel.com.',
 chips=['Welche Zimmer gibt es?','Gibt es Frühstück?','Gibt es einen Parkplatz?','Wie kann ich buchen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
RE='https://www.hotelorientedeteruel.com/disponibilidad.html';RN='https://www.hotelorientedeteruel.com/EN/availability.html'
BOOK=dict(mode='engine',url=dict(es=RE,en=RN,fr=RN,de=RN))
D=dict(name='Hotel Oriente',ac='#2b1f24',ac2='#7c3f45',ac2_a11y='#6a353a',book=BOOK,around=[],foot=FOOT,
 address='Av. Sagunto, 7 · 44002 Teruel',phones=['+34 978 60 15 50'],emails=['recepcion@hotelorientedeteruel.com'],maps='Hotel Oriente, Avenida Sagunto 7, 44002 Teruel',t=T)
META=dict(repo='demo-hotel-oriente-teruel',name='Hotel Oriente',legal_name='SOMNUS TERUEL SL, NIF B88855159 (aviso legal de su web)',registry_ids=['B88855159'],
 url='https://www.hotelorientedeteruel.com/',domain='hotelorientedeteruel.com',municipality='Teruel',province='Teruel',sector='hotel de tres estrellas en el centro de Teruel',
 read_at='2026-11-02T09:20:00+01:00',created_at='2026-11-02T09:19:00+01:00',built_at='2026-11-02T09:30:00+01:00',audit_date='2026-11-02T09:20:00+01:00',
 rating=dict(value=4.2,coincide=['tel','web'],date='2026-10-29',url='https://www.google.com/maps/place/Hotel+Oriente/@40.3365733,-1.104636,17z'),
 book=dict(mode='engine',url=RE,note='motor booking-channel de su propia web: disponibilidad.html (es) y EN/availability.html (en; el motor solo tiene ES y EN, se usa EN para fr/de). HTTP 200 los dos (02/11/2026 09:22).'),first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tenéis?','K01'),('¿Qué tienen las habitaciones?','K02'),('¿Hay desayuno?','K03'),('¿Tenéis parking?','K04'),('¿Tenéis gimnasio?','K05'),('¿A qué hora abre la recepción?','K06'),('¿Dónde estáis?','K07'),('¿Cómo reservo?','K08'),('¿Podéis confirmarme disponibilidad para mañana?','K08'),('¿Puedo salir más tarde?','K09'),('¿Vengo en bici, dónde la dejo?','K10'),('¿Cuál es vuestro teléfono?','K11'),('¿Tenéis cunas?','K12'),('¿Cuánto cuesta la noche?',None),('¿Tenéis piscina?',None)],
'en':[('Which rooms do you have?','K01'),('What do the rooms include?','K02'),('Is there breakfast?','K03'),('Do you have parking?','K04'),('Do you have a gym?','K05'),('When is reception open?','K06'),('Where are you?','K07'),('How do I book?','K08'),('Can you confirm availability for tomorrow?','K08'),('Can I check out late?','K09'),('Where can I leave my bike?','K10'),('What is your phone number?','K11'),('Do you have cots?','K12'),('How much is a night?',None),('Do you have a pool?',None)],
'fr':[('Quelles chambres avez-vous ?','K01'),('Que comprennent les chambres ?','K02'),('Y a-t-il un petit-déjeuner ?','K03'),('Avez-vous un parking ?','K04'),('Avez-vous une salle de sport ?','K05'),('Quand la réception est-elle ouverte ?','K06'),('Où êtes-vous ?','K07'),('Comment réserver ?','K08'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K08'),('Puis-je partir plus tard ?','K09'),('Où laisser mon vélo ?','K10'),('Quel est votre numéro de téléphone ?','K11'),('Avez-vous des lits bébé ?','K12'),('Combien coûte la nuit ?',None),('Avez-vous une piscine ?',None)],
'de':[('Welche Zimmer gibt es?','K01'),('Was bieten die Zimmer?','K02'),('Gibt es Frühstück?','K03'),('Gibt es einen Parkplatz?','K04'),('Gibt es einen Fitnessraum?','K05'),('Wann ist die Rezeption geöffnet?','K06'),('Wo liegt das Hotel?','K07'),('Wie kann ich buchen?','K08'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K08'),('Kann ich später auschecken?','K09'),('Wo kann ich mein Fahrrad lassen?','K10'),('Wie ist Ihre Telefonnummer?','K11'),('Haben Sie Kinderbetten?','K12'),('Was kostet eine Nacht?',None),('Haben Sie einen Pool?',None)]}
