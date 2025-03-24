## Use this because this can also access meta data and infoboxes found in the wikipedia page
import pywikibot
import os

name="Royal_Antwerp_FC"
site = pywikibot.Site('nl', 'wikipedia')
page = pywikibot.Page(site, name)

if page.exists():
    text = page.text

    directory = os.path.join("../data/locations", "antwerp", "pywikibot")

    if not os.path.exists(directory):
        os.makedirs(directory)

    file_path = os.path.join(directory, f"{name}.txt")

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)

    print("De tekst is succesvol opgeslagen")
else:
    print("Pagina niet gevonden")
