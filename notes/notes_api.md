# API  

## Hoe

```
uvicorn rag_frans.api:app --reload
```

## generate-tour

### V1.0

#### 1.

```
POST http://127.0.0.1:8000/generate-tour
Content-Type: application/json

{
  "name": "Frans Dillen",
  "job" : "Schipper",
  "age" : 29,
  "hobbies": "Muziek, Cartoons"
}
```

```
{
  "historische_figuur": {
    "naam": "Jan van Gent",
    "beschrijving": "Jan van Gent was een fictieve schipper en componist die in de 17e eeuw leefde. Hij combineerde zijn liefde voor muziek met zijn maritieme beroep. Hij zeilde op de Schelde en componeerde liederen geïnspireerd door de haven, de zee en het leven aan boord. Hij zou onder andere de liederen van de beiaard van de Onze-Lieve-Vrouwekathedraal hebben opgetekend."
  },
  "verhaal": "Frans, als de geest van Jan van Gent stap ik aan boord van jouw schip, niet in het vlees, maar in de herinnering. Ik, een schipper met een passie voor muziek, neem je mee op een ontdekkingsreis door mijn Antwerpen. We beginnen aan de Schelde, waar de muziek van de haven en de zeilboten mijn ziel voedde. Laten we de geschiedenis opzoeken, want ik heb ergens een lied verborgen, een melodie van ontdekkingen. We bezoeken de Onze-Lieve-Vrouwekathedraal, waar de klanken van de beiaard als een symfonie van de stad weerklinken. We gaan kijken naar het Museum Plantin-Moretus, waar de gedrukte pagina's de woorden en melodieën van mijn tijd bewaarden. Kijk goed, want in deze plaatsen liggen aanwijzingen verborgen, als noten in een partituur, wachtend om ontcijferd te worden. Laten we op ontdekking gaan!",
  "locaties": [
    {
      "naam": "De Scheldekaaien",
      "beschrijving": "Het kloppende hart van mijn havenstad.",
      "historisch_event": "De Schelde was in de 17e eeuw de levensader van Antwerpen, een bruisende haven waar schepen van over de hele wereld aanmeerden. Ik, Jan van Gent, was hier vaak te vinden, observerend de drukte en de sfeer die me inspireerden tot mijn composities.",
      "puzzel_aanwijzing": "Zoek naar de gravering van een schip op een oude steen, met daaronder een reeks van cijfers en een scheepsroer."
    },
    {
      "naam": "Onze-Lieve-Vrouwekathedraal",
      "beschrijving": "De majestueuze toren, een symbool van Antwerpen en een bron van muzikale inspiratie.",
      "historisch_event": "De beiaard van de kathedraal was voor mij een bron van inspiratie. Ik was vaak te vinden op de Grote Markt waar ik luisterde naar de klanken van de beiaardier. Ik noteerde de melodieën op papier en componeerde mijn eigen muziek geïnspireerd door de klanken die de wind meegaf..",
      "puzzel_aanwijzing": "Zoek in de kathedraal naar een versierde steen met een gravure van een muziekinstrument (beiaardklok), met daaronder een kruis met de letters 'JvG'."
    },
    {
      "naam": "Museum Plantin-Moretus",
      "beschrijving": "Een oord van woorden, letters en verhalen, waar mijn composities misschien wel bewaard worden.",
      "historisch_event": "In de 17e eeuw was het huis en de drukkerij van Plantin-Moretus het centrum van de drukkunst en de intellectuele wereld van Antwerpen. Ik kwam hier regelmatig om mijn composities te laten afdrukken en te delen met de wereld.",
      "puzzel_aanwijzing": "Zoek in het museum naar een oud gedrukt blad met inscripties. De afbeeldingen van de letters bevatten een geheimschrift."
    }
  ]
}
```

#### 2.

```
POST http://127.0.0.1:8000/generate-tour
Content-Type: application/json

{
  "name": "Natalia Majchrzak",
  "job": "Kunstenaar",
  "age": 27,
  "hobbies": "Film"
}
```
```
{
  "historische_figuur": {
    "naam": "Jan Sterck",
    "beschrijving": "Een humanist uit de 16e eeuw die rondreisde door Europa om zijn kennis te verspreiden. Zijn interesse in educatie en studie sluiten aan bij Natalia's interesses in het leren en het ontdekken van nieuwe perspectieven."
  },
  "verhaal": "Hallo Natalia! Ik ben Jan Sterck, een geest uit de 16e eeuw. Ik was een humanist uit Antwerpen, een stad van kennis en kunst, net als jij. Ik reisde door Europa om mijn ideeën over onderwijs en studie te delen. Ik zie dat je geïnteresseerd bent in film. Dat klinkt mij geweldig! Ik heb de wereld, en ook de mensen, van dichtbij bekeken. Ik wil je graag meenemen op een reis door mijn Antwerpen. Ik wil je graag laten kennismaken met plekken die voor mij betekenis hadden, en waar we wellicht een puzzel kunnen oplossen? Klaar voor een avontuur?\n\nOnze eerste stop is het *Museum Vleeshuis*. In mijn tijd was dit een levendige plek vol handel en ambacht. De klank van de stad was essentieel, en ik kan je vertellen, ik hield van de klanksymphoniën van de stad! Ik vond het belangrijk om te leren. In het museum vind je een indrukwekkende verzameling muziekinstrumenten waar de Antwerpse klank centraal stond. Ik was altijd op zoek naar de essentie, de kern van zaken. Misschien zit er in de klanken van de instrumenten, of hun geschiedenis, een eerste aanwijzing voor ons geheime doel, Natalia.\n\nLaten we nu naar het *Nachtegalenpark* gaan. Dit was in mijn tijd nog geen park, maar de omgeving van Antwerpen was al wel een plek van schoonheid en rust, een plek om te reflecteren. Ik hield ervan om het leven te overdenken. Ik herinner me de rustgevende omgeving van de omliggende parken, ze herinneren me aan de kracht van de natuur. In het park zie je vaak mensen met interesse in architectuur, het thema van Van de Velde komt hier veel voor, en wie weet, is er wel meer te ontdekken...\n\nOnze laatste stop is *het KMSKA*. De grootste schatten van de kunst herbergen dit museum. Als kunstenaar, zoals jij, vind ik dit een plek vol inspiratie. Zeker voor mij, die zo hield van het verzamelen van kennis. In de uitgebreide renovatie van het museum ligt de sleutel tot het oplossen van het mysterie van het museum. Vroeger werd er een standbeeld geplaatst, en sindsdien zijn er enkele vegen op de vloer zichtbaar geworden, is dit een aanwijzing voor het mysterie? Kijk goed om je heen. Ik ben er zeker van dat de kunstwerken en mijn verhaal hier samenkomen...\n\nDenk aan mijn woorden, verzamel de aanwijzingen en ontdek de geheimen van Antwerpen!",
  "locaties": [
    {
      "naam": "Museum Vleeshuis",
      "beschrijving": "Een museum over klank en de geschiedenis van de stad, relevant voor iemand die de essentie en de klank van de stad wil begrijpen.",
      "historisch_event": "Het museum bevat een rijke collectie muziekinstrumenten.",
      "puzzel_aanwijzing": "Kijk naar de klank van de instrumenten, hun geschiedenis en de bouwstenen van de stad."
    },
    {
      "naam": "Nachtegalenpark",
      "beschrijving": "Een park waar de schoonheid en de reflectie van de natuur centraal staat.",
      "historisch_event": "Het park is vernoemd naar een 'nachtegaal' op de hoek van verschillende steenwegen, die in mijn tijd populair was bij koppels.",
      "puzzel_aanwijzing": "Zoek naar de schoonheid van ontwerper Van de Velde en de geschiedenis van de omgeving."
    },
    {
      "naam": "KMSKA",
      "beschrijving": "Een museum vol kunstschatten, een bron van inspiratie.",
      "historisch_event": "Het standbeeld van Willem van Oranje en Filips van Marnix van Sint-Aldegonde werd geplaatst in 2012.",
      "puzzel_aanwijzing": "De zwarte vegen op de witte vloeren: symbolen van de kunstwerken en de betekenis van de renovatie van het museum."
    }
  ]
}
```

#### 3.
```
POST http://127.0.0.1:8000/generate-tour
Content-Type: application/json

{
  "name": "Michele Goessens",
  "job": "Arts",
  "age": 61,
  "hobbies": "Gitaar, Zeilen"
}
```

```
{
  "historische_figuur": {
    "naam": "Jan van de Velde",
    "beschrijving": "Jan van de Velde (1868-1938) was een invloedrijke Antwerpse architect en ontwerper, bekend om zijn bijdragen aan de Art Nouveau-stijl en zijn sterke band met de culturele kringen van zijn tijd. Gezien jouw interesses in gitaar en zeilen, is hij een uitstekende keuze. Hij was namelijk betrokken bij het ontwerp van het interieur van de eerste elektrische treinstellen (AM35) en enkele rijtuigen, wat ook overeenkomt met je interesse in zeilen, daarbij was hij een productief ontwerper en kunstenaar, net als jijzelf met jouw gitaarspel."
  },
  "verhaal": "Michele, mijn naam is Jan van de Velde. Welkom in mijn Antwerpen! Ik ben vereerd je hier te mogen begeleiden. Bereid je voor op een reis door de tijd, langs plekken die mijn leven hebben gevormd en die jouw interesses zullen raken. We beginnen onze tocht bij het KMSKA, een plek waar ik de schoonheid van de kunst kan delen en waar je als kunstkenner je hart kunt ophalen. Vervolgens bezoeken we de Erfgoedbibliotheek Hendrik Conscience, een schatkamer van kennis en de plek waar mijn intellectuele vrienden en ik onze ideeёn deelden. Daarna reizen we door naar het Vleeshuis, een plek waar we terug kunnen keren in de tijd middels muziek instrumenten. Daarna gaan we naar het Nachtegalenpark, een oase van rust, waar we kunnen wegdromen bij de natuur in de stad, net als de rust die je vindt op het zeilboot. En ten slotte, de Onze-Lieve-Vrouwekathedraal - waar je met je liefde voor kunst en de indrukwekkende architectuur van Antwerpen zal genieten. Volg me, en laten we samen de geheimen van de stad ontdekken!",
  "locaties": [
    {
      "naam": "Koninklijk Museum voor Schone Kunsten Antwerpen (KMSKA)",
      "beschrijving": "Het KMSKA, heropend na renovatie, is een tempel van kunst, ideaal voor een kunstliefhebber als jij, Michele. Denk eens aan alle inspiratie die je hier kunt opdoen voor je gitaarmuziek, door de kleuren, de lijnen, de emoties die de kunstwerken oproepen – het is allemaal voer voor je creativiteit.",
      "historisch_event": "Na de Tweede Wereldoorlog werd de collectie van het museum uitgebreid met moderne kunstwerken uit binnen- en buitenland. In 2022 heropende het museum na een ingrijpende renovatie zijn deuren.",
      "puzzel_aanwijzing": "Zoek in de galerij naar een schilderij waar een muziekinstrument op te zien is. Wat is het lied dat de schilder wilde vertellen?"
    },
    {
      "naam": "Erfgoedbibliotheek Hendrik Conscience",
      "beschrijving": "Deze bibliotheek is een ware schatkamer van kennis en bevat de oudste boeken van Antwerpen. Mijn vrienden en ik kwamen hier vaak om ideeёn uit te wisselen en te discussiëren over architectuur en design. Dit zullen we aanwenden ter voorbereiding van zeiltochten, het is een plek des tijds. ",
      "historisch_event": "De bibliotheek werd opgericht in 1899 toen de stad Antwerpen het literair archief van Hendrik Conscience kocht.",
      "puzzel_aanwijzing": "In de oudste collectie, zoek naar de paginanummering die verwijst naar een verborgen passage die de sleutel bevat. De zoektocht is een afspiegeling van de complexiteit van het zeilen."
    },
    {
      "naam": "Vleeshuis",
      "beschrijving": "Het Vleeshuis, met zijn unieke collectie muziekinstrumenten, is een plek die mijn liefde voor ambacht en detail weerspiegelt. De klank van de stad weerklinkt door de eeuwen heen. Probeer de melodie te achterhalen die de instrumenten je willen vertellen.",
      "historisch_event": "Het Vleeshuis ontleent zijn naam aan de vleeshal die hier van in de 16e eeuw tot in 1889 stond en herbergt een uitgebreide verzameling muziekinstrumenten. ",
      "puzzel_aanwijzing": "Luister goed naar de klokken. Welke melodie wordt er gespeeld? Welke afspraak moet er worden nagekomen?"
    },
    {
      "naam": "Nachtegalenpark",
      "beschrijving": "Het Nachtegalenpark is een oase van rust en schoonheid, een plek om de hectiek van de stad te vergeten en de stilte te zoeken. Net als jij op je zeilboot, Michele, laat dit park je wegdromen en genieten van de natuur.",
      "historisch_event": "De parken werden in 1910 door de gemeente Antwerpen verworven.",
      "puzzel_aanwijzing": "Zoek onder de oudste boom in het park naar een tekening, een schets van een boot, en de route die ze moet varen."
    },
    {
      "naam": "Onze-Lieve-Vrouwekathedraal",
      "beschrijving": "De kathedraal is een toonbeeld van menselijke creativiteit en vakmanschap, een plek waar kunst, architectuur en geschiedenis samenkomen. Bewonder de majestueuze architectuur. Denk aan de duizenden arbeiders die aan dit monument hebben gewerkt, en de vele kunstenaars die hun talenten hebben geëxposeerd.",
      "historisch_event": "De bouw van de huidige kathedraal begon in 1352 en duurde tot 1521.",
      "puzzel_aanwijzing": "Aan de voet van het standbeeld van Rubens, zoek naar de datum die de kunstenaar met zijn werk heeft ingeleid. Welk geheim wordt daar onthuld?"
    }
  ]
}
```

#### 4.

```
POST http://127.0.0.1:8000/generate-tour
Content-Type: application/json

{
  "name": "Kacper Chrolowski",
  "job": "Astronoom",
  "age": 24,
  "hobbies": "Cartoons"
}
```

```
{
  "historische_figuur": {
    "naam": "Lodewijk Sterck",
    "beschrijving": "Lodewijk Sterck, een 16e-eeuwse Antwerpse humanist, was een groot liefhebber van astronomie en cartografie. Op 24-jarige leeftijd, dezelfde leeftijd als Kacper, reisde hij door Europa om zijn kennis te delen, wat relevant is voor Kacper's leeftijd, beroep en interesses.",
    "rol_voor_kacper": "Lodewijk zal je begeleiden op een reis door de tijd, waarbij je de invloed van de sterren op het leven in Antwerpen leert kennen en puzzels oplost die verwijzen naar je passie voor cartoons en je beroep als astronoom."
  },
  "verhaal": "Welkom, Kacper! Ik ben Lodewijk Sterck, een humanist uit het Antwerpen van weleer. Stel je voor: ik reisde door Europa, net als jij nu kunt doen in de tijd! In mijn jeugd, net als jij nu, was ik gefascineerd door de sterren. Volg mij op een tocht langs enkele bijzondere plekken. Onderweg zul je aanwijzingen vinden die je zullen helpen een geheim te ontrafelen dat verborgen ligt in de kosmische symboliek en je liefde voor cartoons. Klaar voor een avontuur door tijd en ruimte?",
  "locaties": [
    {
      "naam": "Onze-Lieve-Vrouwekathedraal",
      "beschrijving": "De Kathedraal domineerde het Antwerpse stadsbeeld. De toren stond symbool voor de verbinding tussen hemel en aarde, een perfecte start voor Kacpers sterrenkundige reis.",
      "historisch_event": "De kathedraal, vaak afgebeeld in Suske en Wiske strips, was een belangrijk punt voor de religieuze beleving en symboliseerde de verbinding met het Hogere. Een plaats waar Lodewijk in extase de sterrenhemel observeerde in zijn filosofische bespiegelingen.",
      "puzzel_aanwijzing": "Kijk naar de gebrandschilderde ramen. Welke cartoonfiguren lijken op de heiligen en engelen? Vind het fragment dat 'het licht' toont."
    },
    {
      "naam": "Erfgoedbibliotheek Hendrik Conscience",
      "beschrijving": "Hier bewaart men eeuwenoude boeken en kaarten. Kacper, als astronoom, zal hier patronen kunnen herkennen.",
      "historisch_event": "In de bibliotheek zijn oude astronomische teksten te vinden. Lodewijk zou hier uren hebben doorgebracht, zich verdiepend in de kennis van de Grieken en Romeinen. De bibliotheek kan ook een connectie maken met de stripreeks; Suske en Wiske bezochten deze plaats ook in een album.",
      "puzzel_aanwijzing": "Zoek naar het oudste astronomische manuscript. De tekeningen op de pagina's bevatten een geheime code, herken jij de cartoonachtige symbolen?"
    },
    {
      "naam": "Rubenshuis",
      "beschrijving": "Het huis van Rubens en het museum geven inzicht in de kunst van die tijd. De planeten en het universum waren ook thema's in werken uit die tijd.",
      "historisch_event": "Rubens' werken bevatten vaak symboliek die met de kosmos verbonden zijn, iets waar Lodewijk ook in geïnteresseerd was. Daarnaast zijn er links met het verhaal door de aanwezigheid van Suske en Wiske.",
      "puzzel_aanwijzing": "Bekijk 'De opstanding van Christus' en let op de compositie en lichtval. Wat vertelt dit over de verborgen krachten? Vergelijk het met de dynamiek van je favoriete cartoons."
    },
    {
      "naam": "Marnixplaats",
      "beschrijving": "Het Marnixplein een ode aan Filips van Marnix van Sint-Aldegonde, een geleerde en politicus uit de tijd van Lodewijk. Marnix was een veelzijdig man, net zoals de cartoons die verschillende thema's proberen te bespreken. ",
      "historisch_event": "Filips van Marnix was burgemeester van Antwerpen in een periode dat er grote veranderingen plaatsvonden. Dit plein is een herinnering aan deze periode.",
      "puzzel_aanwijzing": "Kijk naar de beelden op het plein. Kun je de verbinding vinden tussen deze figuren en de karakters in je favoriete cartoons? Zoek naar het verborgen symbool."
    }
  ]
}
```
### mogelijkse verbeteringen

Hangt af van hoe we de puzzle generator gaan implementeren, welke info er daar nodig is om goede puzzles te genereren.

Voor de rest kunnen we de locaties en geest altijd verbeteren door onze txt documenten voor RAG te verbeteren, uitbreiden,... .

### V2.0

verbeteringen aan Rag model en prompt zorgen voor een beter verhaal

```
POST http://127.0.0.1:8000/generate-tour
Content-Type: application/json

{
  "name": "Kacper Chrolowski",
  "job": "Astronoom",
  "age": 24,
  "hobbies": ["Astronomie, Muziek"]
}
```

```
{
  "historische_figuur": {
    "naam": "Joachim Sterck van Ringelbergh",
    "beschrijving": "Joachim Sterck van Ringelbergh, een Antwerpse pedagoog, astroloog en wiskundige uit de 16e eeuw, was de eerste die het woord 'encyclopedie' in de moderne betekenis gebruikte. Zijn brede kennis en interesse sluiten perfect aan bij de interesses van Kacper."
  },
  "verhaal": "Welkom, Kacper! Ik ben de geest van Joachim Sterck van Ringelbergh. Ik was een man van vele talenten, net als jij. Ik zag de wereld door de ogen van een geleerde, maar mijn blik was altijd gericht op de sterren, net jouw passie voor astronomie. Laat me je meenemen op een reis door mijn Antwerpen, waar we de geheimen van het verleden zullen ontrafelen en de wonderen van de kosmos zullen herontdekken.",
  "locaties": [
    {
      "naam": "Falconpoort",
      "beschrijving": "Onze reis begint bij de Falconpoort, de enige overgebleven herinnering aan het Falcontinnenklooster. Dit klooster werd gesticht door Falco de Lampage, een man die in de munt van Antwerpen werkte, net zoals ik mijn kennis verspreidde. Het klooster was een toevluchtsoord en een centrum van kennis, net als de plek waar je jouw sterren bestudeert, Kacper. Kijk goed naar de poort, want hier begint het mysterie.",
      "historisch_event": "Het Falcontinnenklooster was een plaats van toevlucht en studie. In de 16e eeuw, tijdens de anti-Spaanse opstanden, raakten de zusters een belangrijk deel van hun domein kwijt. Later, in 1784, werd het klooster definitief gesloten door keizer Jozef II.",
      "puzzel_aanwijzing": "De naam 'Falconpoort' is een anagram. Bekijk de letters aandachtig. Wat zou een andere belangrijke plek zijn die met kennis te maken heeft, net als dit klooster?"
    },
    {
      "naam": "Hendrik Conscienceplein",
      "beschrijving": "Van de Falconpoort reizen we naar het Hendrik Conscienceplein. Hier vind je de Erfgoedbibliotheek. In mijn tijd was het verzamelen van kennis en boeken net zo belangrijk als de sterren bestuderen. Het plein is vernoemd naar Hendrik Conscience, een schrijver die de geschiedenis van Vlaanderen vastlegde. Ik ben benieuwd wat voor schatten de bibliotheek voor jou te bieden heeft, Kacper.",
      "historisch_event": "In 1899 kocht de stad Antwerpen het literaire archief van Hendrik Conscience, waarmee de basis werd gelegd voor het Letterenhuis. In 1972 werd het plein het eerste autovrije plein van de stad.",
      "puzzel_aanwijzing": "Op het plein vind je een standbeeld van Hendrik Conscience. Welke belangrijke gebeurtenis in de geschiedenis van Antwerpen staat symbool voor de man die het standbeeld eer?"
    },
    {
      "naam": "Sint-Pauluskerk",
      "beschrijving": "Onze volgende bestemming is de Sint-Pauluskerk, een laatgotische kerk in het hart van het oude Antwerpen. Ik, als man van de renaissance, waardeerde de kunst en architectuur. Deze kerk herbergt een rijk kunstpatrimonium, waaronder de 'Vijftien mysteries van de Rozenkrans', die verhalen vertellen over het leven van Jezus en Maria, net als de mythen aan de hemel.",
      "historisch_event": "De Sint-Pauluskerk werd in de 16e eeuw gebouwd als dominicaner kloosterkerk, ter vervanging van een gebouw uit 1276. De kerk overleefde een brand in 1968, waarbij omwonenden veel kunstwerken wisten te redden.",
      "puzzel_aanwijzing": "In de kerk vind je de kunstwerken van Rubens. Kijk goed naar de symboliek van de schilderijen. Wat is de boodschap die de kunstenaar ons wil meegeven? Kies het juiste antwoord uit de volgende opties:\n\na) De vluchtigheid van het leven\n b) De schoonheid van de natuur\n c) De macht van de kerk"
    },
    {
      "naam": "Rubenshuis",
      "beschrijving": "We bezoeken nu het Rubenshuis, waar de meester Peter Paul Rubens woonde en werkte. Net als Rubens ben ik een liefhebber van kennis en kunst. Zijn atelier was een centrum van creativiteit. Laat de kracht van de creatie aan jou worden overgebracht.",
      "historisch_event": "Rubens was een hofschilder van de aartshertogen Albrecht van Oostenrijk en Isabella van Spanje. Zijn atelier was in de 17e eeuw een bloeiend centrum van kunst.",
      "puzzel_aanwijzing": "Bekijk de details van het huis. Welk motto of citaat vertelt over het leven van Rubens en ook over het leven van intellectuelen in die tijd? Wat is hier de boodschap?"
    },
    {
      "naam": "MAS (Museum aan de Stroom)",
      "beschrijving": "We eindigen onze reis in het MAS, het Museum aan de Stroom. Hier worden de schatten van Antwerpen en de wereld bewaard, van kunst tot maritieme objecten. Kijk naar de ster op het plein, en de kunstcollecties van over de hele wereld. Laat je inspireren door de diversiteit en de verbinding tussen de stad en hun cultuur. Het is een plaats waar kennis en cultuur samenkomen, net als de sterren en jouw muziek.",
      "historisch_event": "Het MAS werd in 2011 geopend en herbergt kunst, culturele tradities en geschiedenis van Antwerpen en de rest van de wereld. Het museumplein heeft een mozaïek van Luc Tuymans, genaamd 'Dead Skull'.",
      "puzzel_aanwijzing": "Buiten het museum staat het kunstwerk ‘Groetend Admiraal Koppel’. Wat is de betekenis van het kunstwerk, en hoe verwijst het naar de verbindingen van de wereld met Antwerpen?"
    }
  ]
}
```

## generate-puzzle

Op elke locatie word er 1 maal een puzzle gegenereerd, we geven wat info mee uit de generate-tour response als ook info over de gebruiker

```
POST http://127.0.0.1:8000/generate-puzzle
Content-Type: application/json

{
  "location": "Sint-Pauluskerk",
  "location_info": "De Sint-Pauluskerk was in de 16e eeuw een centrum van protestantse invloed. Het gebouw werd meermaals geplunderd, maar de kunstvoorwerpen werden gered, wat de band met de vorige locatie versterkt en tevens een parallel vormt met een recente periode van verlies en wederopbouw.",
  "user_interests" : ["Geschiedenis", "Voetbal"],
  "user_job" : "Ambtenaar",
  "location_story" : "Hier zie je de kerk tegenover je, Kacper. Stap naar binnen, als je durft, dit was een kloosterkerk, een plek van intellectueel leven waar de Dominicanen een bron van kennis vormden. De kerk heeft een turbulente geschiedenis en werd door brand zwaar beschadigd, maar de kunstschatten zijn desondanks bewaard gebleven, net als de kennis van het tijdperk. Ik was hier vaak te vinden, gefascineerd door de sterke geestelijke uitstraling."
}
```

### riddle response

```
{
  "puzzle": {
    "puzzle_type": "riddle",
    "puzzle": "Ik was een broeinest van intellect en geloof, maar mijn muren getuigen van vuur en geweld. Hoewel kunstschatten werden gered, herberg ik de herinnering aan een tijd van macht en verlies. Wat ben ik?",
    "answer": "Sint-Pauluskerk",
    "multiple-choice": {}
  }
}
```
### multiple-choice response
```
{
  "puzzle": {
    "puzzle_type": "multiple-choice",
    "puzzle": "De Sint-Pauluskerk stond tijdens de 16e eeuw bekend om zijn protestantse invloed. Gezien je liefde voor voetbal en oog voor geschiedenis, welke gebeurtenis in die tijd zou je het meest hebben aangegrepen?",
    "answer": "De kunstroof door de geuzen",
    "multiple-choice": {
      "answerA": "De kunstroof door de geuzen",
      "answerB": "De opening van de eerste voetbalclub in Antwerpen",
      "answerC": "De bouw van een nieuwe torenspits",
      "answerD": "De benoeming van een nieuwe pastoor"
    }
  }
}
```

### anagram response

Hierbij wordt het woord gescrambled in de frontend aangezien het model hier zo goed als altijd fouten in maakt.

```
{
  "puzzle": {
    "puzzle_type": "anagram",
    "puzzle": "Gegeven de kerk's kloostergeschiedenis en de kostbare kunstschatten die bewaard zijn gebleven, welke staat symbool voor het intellectuele en spirituele aspect van de kerk?",
    "answer": "Kennis",
    "multiple-choice": null
  }
}
```

## Hint

Er zijn 3 degradaties van hints, de eerste degradate is nog heel vaag, onduidelijk, bij de tweede degradatie wordt er al een grotere hint gegeven en bij de laatste degradatie wordt het antwoord soms al verklapt door hoe duidelijk de hint is.
we geven aan de api call de vraag en het antwoord mee alsook de degradatie

```
POST http://127.0.0.1:8000/hint
Content-Type: application/json

{
  "location": "De Plantentuin",
  "question": "De Orangerie in de Plantentuin van Antwerpen bevat borstbeelden van bekende figuren. Welke van de volgende figuren is daar NIET vertegenwoordigd?",
  "answer": "Peter Paul Rubens",
  "hint_level": 1
}
```
### hint level 1
```
{
  "hint": "De figuren in de Orangerie zijn vaak verbonden met de wetenschap en de plantkunde."
}
```

### hint level 2
```
{
  "hint": "De Orangerie bevat borstbeelden van figuren die iets met de plantentuin te maken hadden, of die in het verleden invloed hadden op de stad Antwerpen. De genoemde figuur had weinig tot geen verband met beide."
}
```

### hint level 3

```
{
  "hint": "De Orangerie bevat borstbeelden van beroemde personen, maar de schilder van onder andere 'De Kruisafneming' en 'De opstanding van Christus' is er niet te vinden."
}
```
