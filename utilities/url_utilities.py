def load_urls_from_file(file_path: str):
    url = []
    try:
        with open(file_path) as f:
            url.append(f.readline())
            return url
    except:
        return url


def load_page(url: str):
    # TODO:  add the code that reads the url
    return True


def scrape_page(page_contents: str):
    # TODO:  analyze the text
    return True
