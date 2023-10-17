
import requests
import bs4

result = requests.get("https://www.unitbv.ro/contact/comunitatea-unitbv/2201-burduhos-bogdan-gabriel.html")

soup = bs4.BeautifulSoup(result.text, "lxml")

select_paragraf =soup.select("span")
print(select_paragraf)
# print(select_paragraf[0].getText())


