from bs4 import BeautifulSoup
import requests

def get_morse_code_ja():
    URL = "https://morsedecoder.com/ja/"
    response = requests.get(url=URL)
    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.find_all(name="table", class_="table")[0]
    td = table.find_all(name="td")
    morse_code_dict = {}
    for i, code in enumerate(td):
        if i % 2 ==0:
            text = code.text
        else:
            morse_code_dict[text] = code.text
    return morse_code_dict

