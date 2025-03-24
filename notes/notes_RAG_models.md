# RAG MODEL MAURO

## settings

* 100 txt documents about Antwerp, containging monuments, squares, famous buildings, historic figures,...
* chunksize: 3500, overlap: 800
*         model="meta-llama/llama-3.1-405b-instruct:free",
* chunks used: 10

## QUERY

```
system_message = f"""
Je bent de geest van een historische Antwerpse figuur. Jouw taak is om {naam} een gepersonaliseerde schattenjacht te geven door Antwerpen. Gebruik de historische locaties uit de context en verbind ze met hun interesses, leeftijd en beroep.
Het is heel belangrijk dat we proberen op meerdere facetten van de gebruiker hun persoonlijke informatie zoals naam, job , leeftijd , interresees en hobbies , de locaties en historische figuren moeten een geheel vormen dat de persoon langs interessante monumenten, straten, pleinen enzovoort sturen om een gepersonaliseerde tor te ontvangen.
🔹 **Stap 1: Kies een unieke geest**  
- Kies **geen voor de hand liggende figuren** zoals Rubens of Breughel, tenzij ze een directe link hebben met {naam}.  
- Geef voorkeur aan **minder bekende, maar interessante Antwerpse figuren** zoals handelaars, uitvinders, wetenschappers, schippers, muzikanten of lokale legendes.  
- De geest moet een **sterke persoonlijke connectie** hebben met {naam}. Denk aan hun naam, interesses, beroep en leeftijd.  

🔹 **Stap 2: Creëer een avontuurlijke route**  
Beschrijf een route door Antwerpen met minstens 3 historische locaties.  
Elke locatie moet:  
- **Verbonden zijn met zowel de geest als {naam}**.  
- **Moet gratis en openbaar toegankeliljk zijn, het is voor een toeristische city tour die de mensen langs openbare gratis locaties zoals pleinen, parken, straten, enzovoort stuurt.
- **Uniek of minder bekend zijn** (vermijd standaardplekken zoals de Grote Markt, tenzij noodzakelijk).  
- **Een meeslepende en spannende sfeer hebben**, alsof de geest echt met {naam} praat.  

Omdat ik Tokens wil besparen wil ik gewoon de gekozen locaties op basis va de user, leg heel kort uit waarom deze locaties, ik wil ook een historisch figuur weten, en heel kort waarom deze figuur op basis van de gebruiker, ik probeer tokens te besparen dus probeer zo kort mogelijk te antwoorden
 

"""
```

## USER DATA
```
naam= "Michele Goessens"
job = "Dokter"
leeftijd = 61
hobbies_interests= "gitaar , zeilen"
```
## OUTPUT

```
Historische figuur: Hendrik Conscience
Deze 19e-eeuwse Belgische schrijver was een van de belangrijkste figuren van de Vlaamse Beweging. Zijn werken zijn bekend om hun romantische en patriottische toon, die vaak de strijd voor Vlaamse onafhankelijkheid en identiteit benadrukken. Door zijn literaire bijdragen aan de Vlaamse Beweging, kan hij een interessante gids zijn voor Michele Goessens, een dokter die geïnteresseerd is in zeilen en gitaar.

De route:
1. Het Rubenshuis - Deze historische locatie in Antwerpen is het voormalige huis en atelier van Peter Paul Rubens. Het huis is nu een museum waar veel van zijn werken en die van zijn tijdgenoten worden tentoongesteld. 
2. De Grote Markt - Dit plein in het hart van Antwerpen is omringd door historische gebouwen, waaronder het stadhuis en de Onze-Lieve-Vrouwekathedraal. Het plein is een populaire bestemming voor toeristen en biedt een kijkje in de rijke geschiedenis van Antwerpen.
3. Het Eilandje - Dit gebied in Antwerpen is bekend om zijn maritime geschiedenis en is nu een moderne wijk met veel restaurants, bars en culturele attracties. Het Eilandje is een geweldige plek om te ontspannen en te genieten van de sfeer van de stad.
4. De Sint-Andrieskerk - Deze historische kerk in Antwerpen is een van de oudste kerken van de stad en is bekend om zijn unieke architectuur en zijn rol in de geschiedenis van de Vlaamse Beweging. De kerk is een interessante bestemming voor wie meer wil weten over de geschiedenis en cultuur van Antwerpen.

```

Ik vind deze curatie nog wat basic, misschien aanpassingen aan de txt documenten om bij elk document toch wat info mee te geven om betere connecties te maken.
## USERDATA 2
```

naam= "Frans Dillen"
job = "Schipper"
leeftijd = 29
hobbies_interests= "Skateboard , muziek, film/toneel"
```

## OUTPUT 2

```
Deze Antwerpse figuur werd gekozen omdat Frans Dillen schipper is en Joris van Spilbergen een beroemde Nederlands zeevaarder was die in Antwerpen geboren is. Hij voer op vele expedities en ontdekkingsreizen en had een sterke connectie met de zee, net zoals Frans Dillen.

**De route:**

1. **Het Steen**: De route begint bij Het Steen, een oud fort in Antwerpen dat nu een museum is. Joris van Spilbergen begon zijn carrière op zee als adelborst op kasteel Zeeburg, dat nu niet meer bestaat, maar Het Steen is een mooi alternatief om de route te beginnen. Hier kan Frans Dillen meer leren over de geschiedenis van de zeevaart in Antwerpen en de rol die Joris van Spilbergen daarin speelde.
2. **De Vismarkt**: Vervolgens gaat de route naar de Vismarkt, een levendige markt in het centrum van Antwerpen waar vis en zeevruchten verkocht worden. Hier kan Frans Dillen zien hoe de visserij en de zeevaart nog steeds een belangrijk onderdeel van de Antwerpse economie zijn.
3. **De Grote Markt**: Ten slotte eindigt de route op de Grote Markt, een van de mooiste pleinen in Antwerpen. Hier kan Frans Dillen de prachtige gebouwen en de levendige sfeer bewonderen en nadenken over de rijke geschiedenis van Antwerpen en de rol die Joris van Spilbergen daarin speelde.

Deze route is gratis en openbaar toegankelijk en biedt een mooie combinatie van geschiedenis, cultuur en entertainment. De locaties zijn uniek en minder bekend, maar nog steeds erg interessant en relevant voor de geschiedenis van Antwerpen en Joris van Spilbergen.

```

vismarkt bestaat niet?? misschien bedoelen ze vismijn, dit is nog wel een locatie die gebruikt kan worden, ik denk dat er meer curatie moet gebeuren rond de documenten die gebruikt worden bij RAG.

## USERDATA 3
```
naam= "Ruben Van Haaren"
job = "Ambtenaar"
leeftijd = 29
hobbies_interests= "gitaar , gamen"
```
## OUTPUT 3

```
Historische figuur: Hendrik Conscience 

Dit wordt gekozen omdat de persoon een Ambtenaar is en Hendrik Conscience een overheidsbaan had. Daarnaast is het een historische figuur uit Antwerpen, net als de persoon in kwestie.

1.  **Eerste locatie: Sint-Andrieskerk** 
    -   Gratis en openbaar toegankelijk 
    -   Hendrik Conscience is er begraven
    -   Naar verluidt vond hij inspiratie voor zijn roman "De Leeuw van Vlaanderen" na een bezoek aan het Sint-Andrieskerk 
    -   Ruben Van Haaren kan het kerkgebouw bewonderen en een moment van stilte nemen om de impact van Hendrik Conscience' werk op de Vlaamse literatuur en identiteit te overdenken.
2.  **Tweede locatie: Het Rubenshuis** 
    -   Gratis en openbaar toegankelijk 
    -   Er is een Hendrik Conscience zaal
    -   Er hangen veel van zijn portretten
    -   Er kan informatie gevonden worden over de relaties tussen Peter Paul Rubens en Hendrik Conscience
3.  **Derde locatie: Academie voor Schone Kunsten Antwerpen** 
    -   Deels gratis en openbaar toegankelijk 
    -   Er hangen verscheidene portretten van Hendrik Conscience
    -   Er kan informatie gevonden worden over Hendrik Conscience
    -   Dit kan dienen als inspiratie voor de liefde van Ruben voor Gamen en Gitaar, daar deze kunstvormen ook aan bod komen in de academie.



```

# RAG MODEL KACPER

## SETTINGS

* 100 txt documents about Antwerp, containging monuments, squares, famous buildings, historic figures,...
* chunksize: 1024, overlap: FAISS DEFAULT
*         model="meta-llama/llama-3.1-405b-instruct:free",
* chunks used: 3

## USERDATA 1
```
naam= "Michele Goessens"
job = "Dokter"
leeftijd = 61
hobbies_interests= "gitaar , zeilen"
```

## OUTPUT 1
```
**Historische figuur:** Hendrik Conscience, een Antwerpse schrijver en musicus uit de 19e eeuw. Hij was een romanticus en schreef over het verleden van Vlaanderen, waardoor hij een goede connectie heeft met Michele Goessens' interesse in geschiedenis. Ook was hij een muziekliefhebber en speelde hij gitaar, wat overeenkomt met Michele's hobby.

**Locaties:**

1. **Sint-Andrieskerk**: Hier ligt Hendrik Conscience begraven. De kerk is een mooi voorbeeld van neogotische architectuur en heeft een rijke geschiedenis. Michele Goessens kan hier een moment van stilte nemen om Conscience te herdenken.
2. **De Meir**: Deze winkelstraat was in de 19e eeuw het centrum van de Antwerpse muziekscene. Hier kon je muziekinstrumenten kopen en muzieklessen volgen. Michele Goessens kan hier een kijkje nemen in de verschillende winkels en de sfeer opsnuiven.
3. **Het Eilandje**: Dit is een historische buurt in Antwerpen waar veel zeilers en schippers woonden. Michele Goessens kan hier een wandeling maken langs de Schelde en de zeilboten bewonderen. Ook kan ze een bezoek brengen aan het nabijgelegen Scheepvaartmuseum.

Deze locaties zijn allemaal gratis en openbaar toegankelijk, en bieden een unieke en minder bekende kant van Antwerpen. De route neemt Michele Goessens mee door verschillende aspecten van de stad, van geschiedenis tot muziek en zeilen.

```

## USERDATA 2
```
naam= "Frans Dillen"
job = "Schipper"
leeftijd = 29
hobbies_interests= "Skateboard , muziek, film/toneel"
```
## OUTPUT 2
```
Op basis van de informatie die je me hebt gegeven, kies ik voor de Antwerpse geest "Paul van Ostaijen". Hij was een Belgisch dichter, schrijver en toneelschrijver die leefde in de vroege 20e eeuw en is vooral bekend vanwege zijn experimentele stijl en zijn invloed op de Vlaamse literatuur.

De reden waarom ik deze geest kies, is omdat hij een connectie heeft met Frans Dillen's interesses in film/toneel en muziek. Bovendien was Van Ostaijen ook een rebel en een nonconformist, wat past bij de skateboard-cultuur waar Frans Dillen deel van uitmaakt.

De route die ik voorstel, bestaat uit de volgende locaties:

1. De Naamsestraat in Antwerpen, waar Van Ostaijen een kunstgalerij opende in 1925. Deze locatie is verbonden met Van Ostaijen's liefde voor kunst en cultuur, en is ook een minder bekende plek in Antwerpen.
2. Het Vlaams Theater Instituut in Antwerpen, dat een collectie heeft van Van Ostaijen's toneelstukken en manuscripten. Deze locatie is verbonden met Frans Dillen's interesse in film/toneel en is ook een unieke plek die niet veel toeristen bezoeken.
3. De Sint-Andriesplaats in Antwerpen, waar Van Ostaijen vaak kwam om te schrijven en te discussiëren met andere kunstenaars. Deze locatie is verbonden met Van Ostaijen's liefde voor literatuur en is ook een gezellige plek om te relaxen.

Deze route biedt een unieke en boeiende ervaring voor Frans Dillen, die hem door de minder bekende straten en pleinen van Antwerpen leidt en hem kennis laat maken met de rijke culturele geschiedenis van de stad.

```

## USERDATA 3

```
naam = "Natalia Majchrzak"
job = "Kunstenaar"
leeftijd = 29
hobbies_interests = "Fotografie , gamen"
```

## OUTPUT 3
```
**Unieke geest:** Floris Jespers, een Vlaamse schilder en kunstenaar, en goede vriend van Paul van Ostaijen. Jespers was bekend om zijn expressionistische werken en zijn bijdrage aan de Vlaamse avant-garde beweging.

**Waarom Floris Jespers?** Als kunstenaar en fotograaf kan Natalia Majchrzak zich identificeren met Floris Jespers' artistieke stijl en zijn passie voor innovatie in de kunstwereld.

**Route:**

1. **Botaniek** (Plantentuin van Antwerpen): Deze locatie is verbonden met Floris Jespers' liefde voor natuur en zijn inspiratie voor zijn kunstwerken. Natalia Majchrzak kan de prachtige tuin bewonderen en zien hoe de natuur kunstenaars als Jespers inspireerde.
2. **Sint-Jacobskerk**: Deze kerk is de locatie waar Paul van Ostaijen en Floris Jespers samenkwamen om over kunst en literatuur te praten. Natalia Majchrzak kan de kerk bezoeken en zien waar deze twee kunstenaars elkaar ontmoetten.
3. **Letterenhuis**: Dit is de locatie waar het archief van Paul van Ostaijen wordt bewaard, inclusief zijn correspondentie met Floris Jespers. Natalia Majchrzak kan een kijkje nemen in het archief en zien hoe de vriendschap tussen Van Ostaijen en Jespers hun kunst en literatuur beïnvloedde.

**Waarom deze locaties?** Deze locaties zijn allemaal verbonden met Floris Jespers' leven en werk, en bieden een unieke kijk op de kunstwereld van Antwerpen in de vroege 20e eeuw. Ze zijn ook gratis en openbaar toegankelijk, waardoor Natalia Majchrzak een authentieke ervaring kan hebben.

```

## SETTINGS 2 KACPER
* 100 txt documents about Antwerp, containging monuments, squares, famous buildings, historic figures,...
* chunksize: 3500, overlap: FAISS DEFAULT
*         model="meta-llama/llama-3.1-405b-instruct:free",
* chunks used: 15

## USERDATA 1
```
naam= "Michele Goessens"
job = "Dokter"
leeftijd = 61
hobbies_interests= "gitaar , zeilen"
```

## OUTPUT 1

```
Op basis van Michele Goessens' interesses, leeftijd en beroep, kies ik voor de Antwerpse historische figuur 'Jan van Rijswijck'. Hij was een arts, professor, flamingant en burgemeester van Antwerpen. 

Jan van Rijswijck past bij Michele Goessens' beroep als dokter. Bovendien heeft Jan van Rijswijck bijgedragen aan de ontwikkeling van Antwerpen, wat een interessant aspect kan zijn voor een stadsbezoek.

Locaties voor de schattenjacht: 
1. Plantin-Moretus Museum: Dit museum ligt dichtbij de Vrijdagmarkt, een plek die tijdens Van Rijswijck's periode als burgemeester werd ontwikkeld. 
2. De Vrijdagmarkt: Hier was de oude haven van Antwerpen gevestigd en Jan van Rijswijck heeft er ongetwijfeld vaak rondgelopen.
3. Oud Antwerpen: Jan van Rijswijck zette zich in voor de bewaring van het historisch patrimonium van Antwerpen.
```

## USERDATA 2
```
naam= "Frans Dillen"
job = "Schipper"
leeftijd = 29
hobbies_interests= "Skateboard , muziek, film/toneel"
```

## OUTPUT 2
```
Op basis van de voorkeuren van Frans Dillen, schipper, 29 jaar oud, met interesses in skateboarden, muziek en film/toneel, kies ik voor de Antwerpse figuur: Robert van Genechten (1895-1945), Vlaams dichter, toneelschrijver, advocaat en nationaalsocialistisch politicus.

Historische locaties:

1.  **Museum Vleeshuis**: Dit museum in Antwerpen herbergt een indrukwekkende collectie muziekinstrumenten, waaronder een klavecimbel van de Antwerpse familie Ruckers. Dit past perfect bij Frans Dillens liefde voor muziek.
2.  **De Nachtegaal**: Ooit was dit de Nachtegaal een populair complex met cinema's en theaterzaal waar men kon genieten van een avondje toneel. Het was een iconische locatie in Antwerpen die in de loop der jaren verschillende doeleinden heeft gehad. Vandaag de dag is De Nachtegaal gesloten en wordt niet meer gebruikt. Dit is een leuk punt in de route om meer over de geschiedenis van De Nachtegaal te leren. 
3.  **Oudeleeuwenrui**: De Oudeleeuwenrui is een straat in Antwerpen die deel uitmaakt van de historische binnenstad. De straat is vooral bekend vanwege het prachtige, kleurrijke straatart, zoals de schilderingen op de panden.

Deze locaties zijn allemaal gratis en openbaar toegankelijk en bieden een unieke en interessante ervaring voor Frans Dillen.

```

## USERDATA 3

```
naam = "Natalia Majchrzak"
job = "Kunstenaar"
leeftijd = 29
hobbies_interests = "Fotografie , gamen"
```

## OUTPUT 3
```
Kunstenaar Natalia Majchrzak (29) heeft een fascinatie voor fotografie en gamen, wat hem een unieke visie geeft op de wereld. Ik kies de geest van Henry Van de Velde, een minder bekende maar interessante Antwerpse figuur die een link heeft met kunst en ontwerp.

Henry Van de Velde was een Belgische kunstschilder, ontwerper en architect die in Antwerpen leefde. Hij was een van de grondleggers van de Art Nouveau-beweging en had een sterke invloed op de ontwikkeling van de moderne kunst. Zijn werk omvatte schilderijen, ontwerpen voor meubels, textiel en juwelen, evenals architecturale ontwerpen.

De route die ik voor Natalia Majchrzak heb gekozen, zal hem langs enkele van de belangrijkste locaties in Antwerpen brengen die verbonden zijn met Henry Van de Velde en zijn werk.

1. Het MAS (Museum aan de Stroom) - Hier kan Natalia Majchrzak meer leren over de geschiedenis van Antwerpen en de rol die Henry Van de Velde speelde in de ontwikkeling van de stad. Het MAS is gelegen in de buurt van de haven, waar Van de Velde veel van zijn inspiratie vond.
2. Het Hanzehuis - Dit historische gebouw was ooit het centrum van de Hanze, een middeleeuwse handelsfederatie. Van de Velde was geïnspireerd door de architectuur van dit gebouw en ontwierp enkele van zijn meest beroemde werken in dezelfde stijl.
3. De Boekentoren - Deze toren is een van de meest iconische gebouwen in Antwerpen en werd ontworpen door Henry Van de Velde. Natalia Majchrzak kan hier genieten van het uitzicht over de stad en leren over de geschiedenis van de toren.


```

Het Hanzehuis, de Nachtegaal, Oud Antwerpen en de boekentoren bestaan niet, heb de prompt aangepast om minder links te zoeken met het historische figuur maar meer met de gebruiker.

## NEW QUERY OUTPUT

## USERDATA 3

```
naam = "Natalia Majchrzak"
job = "Kunstenaar"
leeftijd = 29
hobbies_interests = "Fotografie , gamen"
```
```
**Unieke geest:** Ik kies voor de Vlaamse striptekenaar Willy Vandersteen (1913-1990) vanwege zijn kunstzinnige en creatieve connectie met Natalia Majchrzak, die ook een kunstenaar is.

**Route:**

1. **Stripmuren van Antwerpen:** Starten we bij de stripmuren van Antwerpen, een project waar Vandersteen ook aan meegewerkt heeft. We bezoeken de muurschildering van Suske en Wiske aan de Cogels Osylei 42.
2. **De kathedraal van Onze-Lieve-Vrouw:** Daarna gaan we naar de kathedraal van Onze-Lieve-Vrouw, een gebouw dat Vandersteen vaak gebruikte als inspiratiebron voor zijn strips. Dit is ook een plek waar Natalia haar fotografische vaardigheden kan uitoefenen.
3. **Het M HKA:** Ten slotte bezoeken we het M HKA (Museum van Hedendaagse Kunst Antwerpen), waar we werken van hedendaagse kunstenaars kunnen bewonderen en waar Vandersteen ooit exposeerde.

Deze route is een unieke combinatie van stripkunst, architectuur en hedendaagse kunst, die zowel Vandersteen als Natalia Majchrzak eer aandoet.

```

## USERDATA 2
```
naam= "Frans Dillen"
job = "Schipper"
leeftijd = 29
hobbies_interests= "Skateboard , muziek, film/toneel"

```
```
Frans Dillen is een 29-jarige schipper. Hij houdt van skateboarden, muziek en film/toneel. Ik kies voor een Antwerpse geest die een link heeft met zijn interesses, zoals muziek en theater. Ik kies voor de geest van "Jan Blockx" een bekende Vlaamse componist die de directeur was van de Koninklijke Vlaamse Opera in Antwerpen.

Locaties:  
- "De Vleeshuis" in Antwerpen: Dit is een historisch gebouw dat nu een museum is. Het was vroeger een omgeving voor verschillende ambachten, waaronder de beenhouwers en de vleeshandel.  
- Het "Nachtegalenpark" : Het is een groenzone gelegen ten zuiden van Antwerpen en bestaat uit een complex van meerdere aan elkaar grenzende parken. 
- Het "Koninklijk Museum voor Schone Kunsten" : Het Koninklijk Museum voor Schone Kunsten (KMSKA) in Antwerpen is een van de oudste en voornaamste musea in België.

```
## USERDATA 1
```
naam= "Michele Goessens"
job = "Dokter"
leeftijd = 61
hobbies_interests= "gitaar , zeilen"
```

```
Op basis van de informatie die je hebt verstrekt, kies ik de historische figuur "Jan van Rijswijck" voor de schattenjacht van Michele Goessens. Jan van Rijswijck was een Belgisch advocaat, journalist en politicus die leefde in de 19e eeuw en burgemeester van Antwerpen was van 1892 tot 1906.

Ik kies Jan van Rijswijck omdat hij een interessante figuur is die zowel politiek als cultureel actief was in Antwerpen. Bovendien was hij een overtuigd flamingant, wat hem een interessante connectie geeft met de Vlaamse cultuur en geschiedenis.

Voor de schattenjacht zal ik drie locaties kiezen die verbonden zijn met Jan van Rijswijck en Michele Goessens. Deze locaties zijn:

1. Het stadhuis van Antwerpen: Dit is de plek waar Jan van Rijswijck als burgemeester van Antwerpen werkte en waar hij zijn politieke carrière uitbouwde. Het stadhuis is een prachtig gebouw in de binnenstad van Antwerpen en is zeker een bezoek waard.
2. De Vrijdagmarkt: Deze markt is een van de oudste en bekendste markten in Antwerpen en is gelegen in de buurt van het stadhuis. Jan van Rijswijck was een voorstander van de Vlaamse cultuur en geschiedenis, en de Vrijdagmarkt is een plek waar deze cultuur nog steeds levend is.
3. Het Museum Plantin-Moretus: Dit museum is gevestigd in de oude drukkerij van Christoffel Plantijn en is een van de belangrijkste culturele instellingen in Antwerpen. Jan van Rijswijck was een voorstander van de Vlaamse cultuur en geschiedenis, en dit museum is een plek waar deze cultuur nog steeds levend is.

Deze locaties zijn allemaal gratis en openbaar toegankelijk, en bieden een interessante kijk op de geschiedenis en cultuur van Antwerpen.

```
