import wikipediaapi
import os
name="Koninklijke_Vlaamse_Opera"
wiki = wikipediaapi.Wikipedia(user_agent= 'ghost',language='nl')
page = wiki.page(name)

if page.exists():
    text = page.text
    directory = os.path.join("../data/locations", "antwerp", "wikipediaapi")

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
    print("Pagina niet gevonden")
