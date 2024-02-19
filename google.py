import requests
from bs4 import BeautifulSoup


def search(task):
    URL = "https://www.google.com/search?q=" + task

    header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"

    }

    response = requests.get(URL, headers=header)
    soup = BeautifulSoup(response.content, "html.parser")
    result = soup.find(class_="hgKElc").getText()
    return result
