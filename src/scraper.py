import requests

def get_book_data_by_doi(doi):
    url = f"https://api.crossref.org/works/{doi}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data_as_json = response.json()

        item = data_as_json["message"]
        authors = item.get("author", [])
        title = item.get("title", [])[0]
        subtitle = item.get("subtitle", [])[0]
        publisher = item.get("publisher", "")
        publication_date_print = item.get("published-print", {}).get("date-parts", [[]])[0]

        year = publication_date_print[0]
        month_int = publication_date_print[1]

        months = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "Novemeber", "December"
        ]

        month = months[month_int - 1]

        author = authors[0]

        author_firstname = author.get("given")
        author_lastname = author.get("family")

        title_full = f"{title}: {subtitle}"

        return [author_firstname, author_lastname, title_full, publisher, year, month]

    except requests.exceptions.RequestException as e:
        return {"error": "Failed to fetch the data, please check the DOI."}



