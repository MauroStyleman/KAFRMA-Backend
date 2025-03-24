def generate_story_message(name, job, age, hobbies):
    return f"""
    **Gebruik enkel info uit de documenten**

   Je bent de geest van een historische Antwerpse figuur. Jouw taak is om {name} een gepersonaliseerde en meeslepende tour door Antwerpen te geven. Deze tour moet een sterke verbinding hebben met hun hobby's en beroep en zich uitsluitend baseren op de locaties en personen uit de documenten.
    De reis moet aanvoelen als een tijdloos avontuur, waarin de geest en {name} samen dwalen door het verleden, terwijl de geschiedenis zich voor hun ogen ontvouwt

**Stap 1: Kies een unieke geest en relevante locaties**
-Kies een minder bekende, maar boeiende Antwerpse figuur als gids. Vermijd clichéfiguren zoals Rubens of Breughel, tenzij er een directe link is met de hobbies: {hobbies} of het beroep: {job} van {name}.
-De geest moet een persoonlijke connectie hebben met {name}, gebaseerd op hun naam, hobby's ({hobbies}), beroep ({job}).
-Gebruik alleen locaties uit de documenten, en geef ze exact weer zoals ze daar genoemd worden (te vinden achter naam:).
-Selecteer 3 tot 6 locaties die  enkel relevant zijn  voor {name} met zijn hobbies: {hobbies} en/of het beroep: {job}.
-De verbinding tussen de locaties moet logisch en verhalend zijn, met een duidelijke rode draad die zowel de geest als {name} betrekt.
 

**Stap 2: Vertel een avontuurlijk en interactief verhaal**
    - **Het verhaal begint met een introductie waarin de geest zich aan {name} voorstelt en uitlegt waarom hij of zij is verschenen.**
    - **De introductie moet mysterieus, meeslepend en persoonlijk zijn en direct een link leggen met {name}.**
    - **De geest moet expliciet verwijzen naar de hobby's ({hobbies}) en/of het beroep ({job}) van {name}, zodat de gebruiker meteen voelt dat er een diepere connectie is.**
    - **Pas daarna leidt de geest {name} door de verschillende locaties.**
    - **Elke locatie moet  verbonden zijn met de hobby's ({hobbies}) en/of het beroep ({job}) van {name}. De locatiekeuze moet dus  relevant zijn voor {name}, waardoor de ervaring persoonlijk en betekenisvol aanvoelt.**
    - **Vermijd een droge opsomming van feiten**—maak de geschiedenis tastbaar en meeslepend, alsof {name} het zelf beleeft.**  
    - **Gebruik echte historische gebeurtenissen** om een levendig beeld te schetsen.**  
    - **Laat de geest interactief zijn**—hij kan {name} uitdagen om geheimen te ontrafelen.** 
    -**Laat de geest spreken op een manier die past bij de leeftijd en belevingswereld van {name} ({age} jaar), zodat de interactie natuurlijk en herkenbaar aanvoelt.**    
    - **Bij de laatste locatie moet de geest een afsluitend gevoel creëren.** Dit kan door een reflectie, een conclusie of een symbolisch afscheid, zodat {name} voelt dat de reis compleet is.  

**Stap 3: JSON-uitvoer**  

  **BELANGRIJK:**  
- **Antwoord ALLEEN met een geldig JSON-object.**  
- **GEEN markdown** (```json of ```) gebruiken.  
- **GEEN extra uitleg buiten het JSON-object.**  

**JSON-formaat:**  
{{  
  "historische_figuur": {{
    "naam": "Naam van de figuur",  
    "beschrijving": "Korte uitleg waarom deze figuur is gekozen en waarom hij/zij {name} begeleidt."
    "geslacht": "Man/Vrouw",
  }},  
    "verhaal": "Introductie van het verhaal: waarom {name} deze geest ontmoet, wat hun connectie is, en waarom ze samen deze reis maken.",
  "locaties": [  
    {{  
      "naam": "Naam van de locatie (MOET exact uit de documenten komen als te vinden achter naam: }})",  
      "wiki_naam": "Naam zoals in Wikipedia (indien beschikbaar) vinden achter wiki_naam: ",
      "beschrijving": "De geest vertelt hier verder het verhaal: wat gebeurde hier op deze locatie? Wat is de connectie met de geest? Wat is de connectie met {name}?"
    }}  
  ]  
}}  
"""


def generate_wordle(location, location_info, user_interests, user_job, location_story):
    return f"""
        Kies een woord ALLEEN MAAR UIT DE LIJST van woorden, zorg ervoor dat het woord een link heeft met {location},{location_info} en {location_story}
        LIJST VAN MOGELIJKSE WOORDEN: 
        "aanga", "aarde", "aards", "aardt", "abdij", "abdis", "abeel", "abten", "abuis",
    "grave", "hoven", "molen", "actes", "actie", "actio", "actor", "actum", "adelt", 
    "aders", "afbak", "afkom", "afleg", "aflos", "afnam", "afsta", "aftak", "aften", 
    "afval", "afzag", "afzet", "agaat", "agave", "agens", "agnes", "agora", "ajour", 
    "akbar", "akela", "akker", "akten", "aktes", "alaaf", "alpen", "dente", "aldus", 
    "aleer", "grote", "algen", "alien", "alken", "allee", "allen", "aller", "alles", 
    "mater", "almen", "alras", "alsem", "alsof", "alten", "amine", "amorf", "andel", 
    "ander", "andes", "angel", "angst", "angus", "animo", "anjer", "anker", "annen", 
    "antal", "pieck", "aorta", "apart", "appen", "apsis", "poort", "arcen", "arend", 
    "argon", "aride", "arken", "armee", "armen", "armer", "armoe", "arren", "artes", 
    "artis", "aruba", "asgat", "assen", "asser", "asses", "asten", "aster", "asurn", 
    "atoom", "avant", "azijn", "azuur", "peter", "baans", "baant", "baars", "baart", 
    "bacil", "baden", "bahco", "bajes", "baken", "bakra", "balts", "banda", "bande", 
    "banen", "bange", "bapao", "barak", "baren", "barok", "baron", "barre", "basen", 
    "bases", "basil", "basis", "baste", "batch", "baten", "baton", "bazel", "monde", 
    "bebop", "bedde", "bedek", "beden", "beeft", "beeld", "beemd", "begaf", "begin", 
    "beide", "beken", "bekom", "beleg", "belet", "beman", "benam", "bende", "benen", 
    "bengt", "benig", "benul", "beoog", "beren", "berge", "bergt", "beril", "berin", 
    "besef", "besta", "beste", "beten", "beter", "beton", "beurs", "beurt", "beval", 
    "bevek", "bevel", "beven", "bezag", "bezat", "bezet", "bezie", "bezig", "bezit", 
    "bezon", "bidet", "horen", "biels", "bijen", "bijna", "bijou", "biken", "gates", 
    "bivak", "blaak", "blaam", "zegge", "bleef", "bleek", "bleke", "bliek", "blijk", 
    "blikt", "blink", "bloed", "bloei", "bloem", "bloks", "bloos", "bloot", "blust", 
    "bocht", "bodem", "boden", "bodes", "boeit", "boeke", "bogen", "bolle", "bomen", 
    "bonen", "boogt", "booms", "boomt", "boord", "boort", "boren", "borgt", "boson", 
    "boten", "boude", "boute", "herop", "bouwe", "boven", "braam", "brads", "water", 
    "brand", "brede", "breed", "breid", "brein", "brent", "breuk", "breur", "broed", 
    "broei", "broes", "broom", "brouw", "bruis", "brute", "buren", "buret", "burgh", 
    "buste", "buten", "buurt", "buxus", "cadet", "canto", "caput", "cargo", "casco", 
    "casus", "cauda", "celle", "meren", "cesar", "chaam", "chaos", "chemo", "chiro", 
    "cijns", "cilia", "cisco", "civic", "clair", "clans", "clave", "clubs", "codex", 
    "cokes", "colli", "collo", "colon", "discs", "congo", "conti", "conto", "conus", 
    "corps", "corso", "corte", "coups", "cours", "crime", "laude", "cumul", "cunet", 
    "curie", "curve", "cycli", "daden", "dader", "daken", "dalai", "dalen", "daler", 
    "danig", "danse", "dante", "dazen", "debat", "debet", "deden", "dieze", "dries", 
    "drift", "eiken", "deels", "deens", "erven", "facto", "gaard", "gagel", "degen", 
    "groot", "hagen", "haven", "heide", "hilde", "hoeve", "hoogt", "deken", "kling", 
    "klomp", "kreek", "kring", "kroon", "delen", "linie", "marke", "marne", "maten", 
    "meern", "merel", "misse", "dempt", "denen", "hoorn", "denis", "denke", "oever", 
    "denon", "noord", "velde", "olmen", "panne", "depot", "depri", "derby", "derde", 
    "reede", "deren", "derft", "ronde", "venen", "sluis", "steen", "stijl", "tijds", 
    "tjalk", "tunen", "deugd", "vaart", "veste", "vlier", "voort", "waard", "wanne", 
    "weere", "weide", "werft", "wever", "wilde", "woude", "dezen", "dezer", "dezes", 
    "zicht", "zwaan", "dicht", "diene", "diens", "dient", "diepe", "diept", "diere", 
    "diets", "dijde", "dijen", "diode", "docht", "doden", "doend", "doffe", "dogma", 
    "dolby", "dolen", "domus", "doods", "dooit", "doolt", "doorn", "doper", "dorps", 
    "dorre", "doven", "dover", "draad", "draaf", "draak", "drain", "drake", "drama", 
    "drang", "drank", "dreft", "dreig", "driel", "dring", "droes", "drost", "drugs", 
    "druif", "duale", "dubio", "duidt", "duldt", "dunde", "dunst", "duren", "dwang", 
    "ebben", "echec", "echte", "echts", "edele", "edict", "edoch", "eeklo", "eelde", 
    "eerde", "eerst", "effen", "egels", "eggen", "eicel", "eider", "eifel", "eigen", 
    "einde", "eisen", "eiser", "eiste", "eject", "eland", "elect", "elfde", "elite", 
    "ellen", "elles", "elven", "emirs", "emmen", "enden", "enige", "enkel", "enken", 
    "enorm", "plein", "enten", "enzym", "eonen", "epiek", "erfde", "komen", "staan", 
    "vanaf", "erika", "erken", "erker", "ermee", "ernst", "ertoe", "ervan", "essen", 
    "ester", "eters", "ethos", "ethyl", "ethyn"
    
     **BELANGRIJK:**  
- **Antwoord ALLEEN met een geldig JSON-object.**  
- **Gebruik ALTIJD dubbele quotaties " " , NOOIT enkele quotaties ' ' ook niet in de content
- **GEEN markdown** (```json of ```) gebruiken.  
- **GEEN WOORDEN DIE NIET UIT DE LIJST KOMEN, ALLEEN MAAR WOORDEN UIT DE LIJST KIEZEN ALS WORDLE
- **GEEN extra uitleg buiten het JSON-object.**  
                **JSON-formaat:**  
{{  
  "puzzle": {{
    "puzzle_type": "wordle",  
    "puzzle": "tips om het woord te vinnden aan de hand van de locatie",
    "answer": "Het gekozen 5-letter woord uit de lijst"
  }}
}}    
     
    """


def generate_puzzle_message(location, location_info, user_interests, user_job, location_story):
    return f"""
        **Gebruik enkel info uit de documenten**

                Je bent een mysterieuze gids die historische puzzels maakt over {location}.  
                De locatie is **{location}** en je genereert een puzzel die aansluit bij de rijke geschiedenis en unieke kenmerken van deze locatie.  
                De puzzel moet **uitsluitend gebaseerd zijn op de locatie zelf** en haar kenmerken.  

                **Instructies voor puzzels:**  
                1. **Kies een puzzeltype** (anagram, multiple_choice) dat het beste past bij de geschiedenis en het thema van de locatie: {location}.  
                2. **Gebruik de volgende informatie om de puzzel te personaliseren:**  
                   - **Locatie info:** {location_info}  
                   - **Verhaal dat de gebruiker net gelezen heeft over de locatie:** {location_story}  
                   - **Extra info uit historische teksten over de locatie.** Gebruik deze om de puzzel uitdagend te maken.  

                **Formaat per puzzeltype:**
                - **Anagram:** Geef **1 woord dat NIET gemixt is** het woord is liefst gerelateerd aan een kunstwerk, tentoonstelling, of belangrijk aspect van de locatie, het moet niet gemixt worden omdat we dit nog zelf doen.
                - **Multiple Choice:** Geef één **correcte optie** en drie **verkeerde opties**. De vraag moet gaan over de geschiedenis van de locatie, maar moet ook aansluiten bij de interesses van de gebruiker.
                
                **Belangrijk:**
                -Probeer 50% van de tijd een anagram puzzle te geven, 50% een multiple choice.
                - **De puzzel mag NIET direct over de naam van de locatie ({location}) gaan**, maar moet focussen op **wat deze plek uniek maakt**.  
                - **Vermijd vragen over het beroep of de hobby’s van de gebruiker.** De puzzel draait alleen om de locatie en haar kenmerken.  
                - **Maak de puzzel uitdagend**—niet te eenvoudig of vanzelfsprekend.  
                - Het resultaat moet **alleen als JSON** worden gegeven zonder extra tekst erboven of eronder.
                  
                  **BELANGRIJK:**  
- **Antwoord ALLEEN met een geldig JSON-object.**  
- **Gebruik ALTIJD dubbele quotaties " " , NOOIT enkele quotaties ' ' ook niet in de content
- **GEEN markdown** (```json of ```) gebruiken.  
- **GEEN extra uitleg buiten het JSON-object.**  
                **JSON-formaat:**  
{{  
  "puzzle": {{
    "puzzle_type": "type puzzle, (anagram, multiple-choice)",  
    "puzzle": "de tekstuele puzzle, bij een anagram geef je wat uitleg over het woord dat geraden wordt om het iets makkelijker te maken maar je geeft GEEN anagram, enkel wat uitleg om het woord te vinden, wij zullen zelf het anagram maken aan de hand van answer.. ",
    "answer": "het correcte antwoord, wanneer dit multiple choice is geef je het antwoord helemaal niet zomaar de optie geven, dus niet A B C of D maar het antwoord. Als het een anagram is geef je hier het correcte gezochte woord.",
    "multiple-choice": {{
        "answerA": "optieA",
        "answerB": "optieB",
        "answerC": "optieC",
        "answerD": "optieD"
    }}
  }}
}}
"""


def generate_hint(location, question, answer, hint_level):
    return f"""
    De speler bevindt zich op de locatie "{location}" en heeft de volgende vraag gekregen:  
    "{question}" met als correct antwoord: "{answer}".  
    De speler weet het antwoord niet en vraagt om een hint.

    Er zijn 3 hintniveaus, waarbij elke hint steeds explicieter wordt:  
    - **Hint level 1:** Een subtiele aanwijzing die de speler op het juiste spoor zet, zonder het antwoord direct weg te geven.  
    - **Hint level 2:** Een duidelijke hint die de speler sterk in de richting van het antwoord helpt.  
    - **Hint level 3:** Een bijna volledig antwoord, waarbij de speler nog maar een kleine stap hoeft te zetten.  

    Voor deze vraag heeft de speler een hint van niveau {hint_level} gevraagd.  

    **BELANGRIJK:**  
    - **Antwoord ALLEEN met een geldig JSON-object.**  
    - **Gebruik ALTIJD dubbele aanhalingstekens (" "), NOOIT enkele (' ').**  
    - **GEEN markdown (```json of ```) gebruiken.**  
    - **GEEN extra uitleg buiten het JSON-object.**  

    **JSON-formaat:**  
    {{
        "hint": "JOUW HINT HIER"  
    }}  

    Geef nu een geschikte hint op basis van het gekozen hintniveau.
    """


def generate_image_with_context(location):
    return f"""
        Ik wil dat je in de **gegeven context** zoekt naar een **afbeelding die past bij de {location}** die de gebruiker heeft genoemd.
        - Zoek **expliciet** naar een URL in die een afbeelding van deze locatie weergeeft.  
        - Als er meerdere afbeeldingen worden genoemd, kies de **één random** afbeelding.
        - Geef **exact één multiple-choice vraag** die direct verband houdt met de tekst in de **Context Afbeelding:** sectie.
        - Stel **geen vraag over de persoon die op de afbeelding staat** (bijvoorbeeld: 'Wie staat er op dit standbeeld?').
        - Stel in plaats daarvan een vraag over de **context van de afbeelding**.
        - Geef **vier antwoordopties**, waarvan **één correct antwoord** is.
        - Geef aan **welke optie correct is**.

        **BELANGRIJK:**  
        - **Antwoord ALLEEN met een geldig JSON-object.**  
        - **Gebruik ALTIJD dubbele aanhalingstekens (" "), NOOIT enkele (' ').**  
        - **GEEN markdown (```json of ```) gebruiken.**  
        - **GEEN extra uitleg buiten het JSON-object.**

        **JSON-formaat:**  
    {{
        "puzzle": {{
            "puzzle_type": "image",
            "image_url": "DE GEVONDEN AFBEELDING URL HIER",
            "question": "EEN UNIEKE EN RELEVANTE VRAAG OVER DE AFBEELDING HIER",
            "multiple-choice": {{
                "answerA": "optieA",
                "answerB": "optieB",
                "answerC": "optieC",
                "answerD": "optieD"
            }},
            "answer": "DE JUISTE KEY VAN DE CORRECTE ANTWOORDOPTIE HIER" 
        }}
    }}
    """
