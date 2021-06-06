import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint

file = open("notebooks.csv", 'w', encoding="utf-8_sig")

file.write("სახელი, ფასი\n")

a = 1

while a <= 5:
    url = f"https://alta.ge/notebooks-page-{a}.html"
    r = requests.get(url)
    content = r.text
    b = BeautifulSoup(content, "html.parser")
    c = b.find("div", {"class": "grid-list"})
    # print(c)
    notebooks = c.find_all("div", {"class": "ty-column3"})
    # print(notebooks)
    for each in notebooks:
        notebooksname = (each.find("a", {"class": "product-title"}))
        # print(notebooksname.text)
        n = notebooksname.text
        notebookprice = each.find("span", {"class": "ty-price-num"})
        # print(notebookprice.text)
        p = notebookprice.text
        file.write(f"{n}, {p}\n")
    a += 1
    sleep(randint(15, 20))

