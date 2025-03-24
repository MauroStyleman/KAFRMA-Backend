import requests
import os
from bs4 import BeautifulSoup

name = "Royal_Antwerp_FC"

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
        file_path = os.path.join(directory, f"{name}.txt")

        # Schrijf de tekst naar het bestand
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text)

        print("De tekst is succesvol opgeslagen")
    else:
        print("Kon de hoofdinhoud niet vinden op de pagina.")
else:
    print(f"Fout bij het ophalen van de pagina: {response.status_code}")
