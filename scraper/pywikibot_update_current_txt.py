import pywikibot
import os


wiki = pywikibot.Site("nl", "wikipedia")
source_directory = os.path.join("../data/locations", "antwerp", "html_scraper")
target_directory = os.path.join("../data/locations", "antwerp", "pywikibot")

os.makedirs(target_directory, exist_ok=True)

missing_pages = []

for filename in os.listdir(source_directory):
    if filename.endswith(".txt"):
        page_name = filename.replace(".txt", "")

        print(f"Fetching Wikipedia page: {page_name}")
        page = pywikibot.Page(wiki, page_name)

        if page.exists():
            new_text = page.text

            new_file_path = os.path.join(target_directory, filename)

            with open(new_file_path, "w", encoding="utf-8") as file:
                file.write(new_text)

            print(f"Saved: {new_file_path}")
        else:
            print(f"Page not found: {page_name}")
            missing_pages.append(page_name)

if missing_pages:
    print("\nSummary: The following Wikipedia pages were NOT found:")
    for missing in missing_pages:
        print(f"- {missing}")
else:
    print("All pages were found and saved successfully!")

print("Processing complete!")
