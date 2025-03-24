import requests

# MediaWiki API
def get_wiki_info(title):
    url = "https://nl.wikipedia.org/w/api.php"

    if title.__contains__(" "):
        title = title.replace(" ", "_")

    params = {
        "action": "query",
        "format": "json",
        "titles": title,
        "prop": "extracts|images",
        "exintro": True,
        "explaintext": True,

    }

    response = requests.get(url, params=params)
    data = response.json()

    if "query" in data and "pages" in data["query"]:
        pages = data["query"]["pages"]


        page_id = next(iter(pages))
        page = pages[page_id]
        print(page)

        summary = page.get("extract") or None
        if summary.count("\n") > 3:
            summary = None

        image_urls = []
        if "images" in page:
            for image in page["images"]:
                image_title = image["title"]
                image_info_params = {
                    "action": "query",
                    "format": "json",
                    "titles": image_title,
                    "prop": "imageinfo",
                    "iiprop": "url"
                }
                image_info_response = requests.get(url, params=image_info_params)
                image_info_data = image_info_response.json()
                image_info_page = image_info_data["query"]["pages"]
                image_info = next(iter(image_info_page.values()))

                if "imageinfo" in image_info:
                    image_urls.append(image_info["imageinfo"][0]["url"])

        return {
            "title": title,
            "summary": summary,
            "image_urls": image_urls
        }

    return {"error": "Page not found"}


