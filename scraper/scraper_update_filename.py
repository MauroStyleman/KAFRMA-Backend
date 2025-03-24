## This will update the filenames in location html_scraper so it match the name like wikipedia

import requests
import os
from bs4 import BeautifulSoup

## wikipages that needed to be updated
wiki_pages = [
    "Abraham_Ortelius.txt",
    "Anna_Bijns.txt",
    "Gouden_Eeuw_(Antwerpen).txt",  # Antwerp in the 16th Century
    "Kathedraal_van_Antwerpen.txt",
    "Christoffel_Plantijn.txt",
    "Falconklooster.txt",
    "Frans_Hals.txt",
    "Hendrik_Conscience.txt",
    "Hendrik_van_Zutphen.txt",
    "Hendrik_Voes.txt",
    "Geschiedenis_van_Antwerpen.txt",
    "Jacob_van_Liesvelt.txt",
    "Jan_Karel_della_Faille.txt",
    "Jan_van_Essen.txt",
    "Jan_van_Rijswijck.txt",
    "Joachim_Sterck_van_Ringelbergh.txt",
    "Joris_van_Spilbergen.txt",
    "Karel_de_Stoute.txt",
    "Maria_Baers.txt",
    "Max_Elskamp.txt",
    "Peter_Paul_Rubens.txt",
    "Sint-Andries_(Antwerpen).txt",
    "Sint-Carolus_Borromeuskerk.txt",
    "Sint-Pauluskerk_(Antwerpen).txt"
]


target_directory = os.path.join("../data/locations", "antwerp", "html_scraper")

for filename in wiki_pages:
    name = filename.removesuffix(".txt")

    print(f"Fetching Wikipedia page: {name}")

    # Bouw de URL op met behulp van een f-string
    url = f"https://nl.wikipedia.org/wiki/{name}"

    # Haal de pagina op
    response = requests.get(url)

    if response.status_code == 200:
        # Parse de HTML met BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Zoek de div met id "mw-content-text" waarin de hoofdinhoud zit
        content_div = soup.find("div", id="mw-content-text")

        if content_div:
            # Haal de tekst op, met een scheidingsteken tussen de blokken
            text = content_div.get_text(separator="\n")

            # Stel de gewenste opslaglocatie in
            directory = os.path.join("../data/locations", "antwerp", "html_scraper")

            # Maak de map aan als deze nog niet bestaat
            if not os.path.exists(directory):
                os.makedirs(directory)

            # Definieer het volledige pad naar het bestand
            new_file_path = os.path.join(target_directory, filename)

            with open(new_file_path, "w", encoding="utf-8") as file:
                file.write(text)

            print("De tekst is succesvol opgeslagen")
        else:
            print("Kon de hoofdinhoud niet vinden op de pagina.")
    else:
        print(f"Fout bij het ophalen van de pagina: {response.status_code}")
