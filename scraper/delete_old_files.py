import os

files_to_delete = [
    "Abraham_Ortelius",
    "Anna_Bijns",
    "Gouden_Eeuw_(Antwerpen)",  # Antwerp in the 16th Century
    "Kathedraal_van_Antwerpen",
    "Christoffel_Plantijn",
    "Falconklooster",
    "Frans_Hals",
    "Hendrik_Conscience",
    "Hendrik_van_Zutphen",
    "Hendrik_Voes",
    "Geschiedenis_van_Antwerpen",
    "Jacob_van_Liesvelt",
    "Jan_Karel_della_Faille",
    "Jan_van_Essen",
    "Jan_van_Rijswijck",
    "   Joachim_Sterck_van_Ringelbergh",
    "Joris_van_Spilbergen",
    "Karel_de_Stoute",
    "Maria_Baers",
    "Max_Elskamp",
    "Peter_Paul_Rubens",
    "Sint-Andries_(Antwerpen)",
    "Sint-Carolus_Borromeuskerk",
    "Sint-Pauluskerk_(Antwerpen)"
]

directory = os.path.join("../data/locations", "antwerp", "html_scraper")

for file_name in files_to_delete:
    file_path = os.path.join(directory, f"{file_name}")

    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        except PermissionError:
            print(f"Permission denied when trying to delete: {file_path}")
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")
    else:
        print(f"File not found: {file_path}")

print("File deletion process complete.")
