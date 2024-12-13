import requests

def get_book_data_by_doi(doi):
    url = f"https://api.crossref.org/works/{doi}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data_as_json = response.json()

        item = data_as_json["message"]

        authors = item.get("author", [])
        author_list = []
        if authors:
            for author in authors:
                if "given" in author and "family" in author:
                    fullname = f"{author['given']} {author['family']}"
                    author_list.append(fullname)

        editors = item.get("editor", [])
        editor_list = []
        if editors:
            for editor in editors:
                if "given" in editor and "family" in editor:
                    fullname = f"{editor['given']} {editor['family']}"
                    editor_list.append(fullname)

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

        month = months[month_int - 1] if month_int else ""

        return [author_list,
                title_full,
                publisher,
                year,
                month,
                editor_list]

    except requests.exceptions.RequestException:
        return {"error": "Failed to fetch the data, please check the DOI."}

def get_article_data_by_doi(doi):
    url = f"https://api.crossref.org/works/{doi}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data_as_json = response.json()

        item = data_as_json["message"]

        authors = item.get("author", [])
        author_list = []
        if authors:
            for author in authors:
                if "given" in author and "family" in author:
                    fullname = f"{author['given']} {author['family']}"
                    author_list.append(fullname)

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

        return [author_list,
                title_full,
                publisher,
                year,
                month,
                journal,
                volume]

    except requests.exceptions.RequestException:
        return {"error": "Failed to fetch the data, please check the DOI."}

def get_inproceeding_data_by_doi(doi):
    url = f"https://api.crossref.org/works/{doi}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data_as_json = response.json()

        item = data_as_json["message"]

        authors = item.get("author", [])
        author_list = []
        if authors:
            for author in authors:
                if "given" in author and "family" in author:
                    fullname = f"{author['given']} {author['family']}"
                    author_list.append(fullname)

        editors = item.get("editor", [])
        editor_list = []
        if editors:
            for editor in editors:
                if "given" in editor and "family" in editor:
                    fullname = f"{editor['given']} {editor['family']}"
                    editor_list.append(fullname)

        titles = item.get("title", [])
        main_title = titles[0] if titles else ""
        subtitle = item.get("subtitle", [])
        title_full = f"{main_title}: {subtitle[0]}" if subtitle else main_title
        booktitle = item.get("container-title", "")[0]
        volume = item.get("volume", "")
        publisher = item.get("publisher", "")

        publication_date_print = item.get("published-print", {}).get("date-parts", [[]])[0]
        year = publication_date_print[0]
        month_int = publication_date_print[1]

        months = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "Novemeber", "December"
        ]

        month = months[month_int - 1]

        return [author_list,
                title_full,
                publisher,
                year,
                month,
                editor_list,
                booktitle,
                volume]

    except requests.exceptions.RequestException:
        return {"error": "Failed to fetch the data, please check the DOI."}




