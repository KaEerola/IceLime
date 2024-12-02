import requests

def get_book_data_by_doi(doi):
    url = f"https://api.crossref.org/works/{doi}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data_as_json = response.json()

        item = data_as_json["message"]

        authors = item.get("author", [])
        author_firstname = ""
        author_lastname = ""
        if authors:
            for author in authors:
                if "given" in author and "family" in author:
                    author_firstname = author["given"]
                    author_lastname = author["family"]
                    break

        editors = item.get("editor", [])
        editor_firstname = ""
        editor_lastname = ""
        if editors:
            for editor in editors:
                if "given" in editor and "family" in editor:
                    editor_firstname = editor["given"]
                    editor_lastname = editor["family"]
                    break

        titles = item.get("title", [])
        main_title = titles[0] if titles else ""
        subtitle = item.get("subtitle", [])
        title_full = f"{main_title}: {subtitle[0]}" if subtitle else main_title

        publisher = item.get("publisher", "")

        publication_date_print = item.get("published-print", {}).get("date-parts", [[]])[0]
        year = publication_date_print[0]
        month_int = publication_date_print[1]

        months = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "Novemeber", "December"
        ]

        month = months[month_int - 1]

        return [author_firstname, author_lastname, title_full, publisher, year, month, editor_firstname, editor_lastname]

    except requests.exceptions.RequestException as e:
        return {"error": "Failed to fetch the data, please check the DOI."}

def get_article_data_by_doi(doi):
    url = f"https://api.crossref.org/works/{doi}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data_as_json = response.json()

        item = data_as_json["message"]

        authors = item.get("author", [])
        author_firstname = ""
        author_lastname = ""
        if authors:
            for author in authors:
                if "given" in author and "family" in author:
                    author_firstname = author["given"]
                    author_lastname = author["family"]
                    break

        journal = item.get("container-title", "")[0]
        volume = item.get("volume", "")

        titles = item.get("title", [])
        main_title = titles[0] if titles else ""
        subtitle = item.get("subtitle", [])
        title_full = f"{main_title}: {subtitle[0]}" if subtitle else main_title

        publisher = item.get("publisher", "")

        publication_date_print = item.get("published-print", {}).get("date-parts", [[]])[0]
        year = publication_date_print[0]
        month_int = publication_date_print[1]

        months = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "Novemeber", "December"
        ]

        month = months[month_int - 1]

        return [author_firstname, author_lastname, title_full, publisher, year, month, journal, volume]

    except requests.exceptions.RequestException as e:
        return {"error": "Failed to fetch the data, please check the DOI."}




